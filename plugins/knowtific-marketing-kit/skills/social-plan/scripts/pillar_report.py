#!/usr/bin/env python3
"""Monthly pillar review for organic social.

Reads a CSV of posts and compares content pillars so you can decide what to
keep, adjust or replace.

CSV columns (header required; blanks allowed except pillar):
  date,platform,pillar,views,likes,comments,shares,saves,hook_rate,follows,leads

Usage:
  python pillar_report.py this_month.csv [--previous last_month.csv] [--json]

Rules applied:
  - Primary score = shares + saves per 1,000 views (shareability). Only posts with
    views count towards the per-1,000 figures, so a blank views cell can't inflate a pillar.
  - Pillar names are matched ignoring case and extra spaces ("Ratings" = "ratings").
  - Hook rate can be written as 35, 35% or 0.35; all are read as 35%.
  - The account median uses only pillars with at least 3 posts (falls back to all pillars
    if none have 3). A pillar is a "winner" if its score is >= 1.25x that median,
    a "loser" if <= 0.75x.
  - Pillars with fewer than 3 posts are marked "too few posts" (directional only).
  - With --previous: month-over-month change, and pillars that were losers in both months
    are flagged "replace" (two bad months in a row). Practitioner guidance: give a pillar
    3-5 months to find traction before judging it on growth alone.
"""
import argparse
import csv
import json
import statistics
import sys

NUM_FIELDS = ["views", "likes", "comments", "shares", "saves", "hook_rate", "follows", "leads"]
MIN_POSTS = 3


def to_num(v):
    if v is None:
        return None
    v = str(v).strip().replace(",", "").replace("%", "")
    if v in ("", "-", "--"):
        return None
    try:
        return float(v)
    except ValueError:
        return None


def hook_pct(v):
    """Normalise hook rate to a percentage: '35%', '35' and '0.35' all become 35."""
    if v is None:
        return None
    s = str(v).strip()
    had_pct = s.endswith("%")
    x = to_num(s)
    if x is None:
        return None
    if not had_pct and 0 < x <= 1:
        x *= 100
    return x


def key_of(name):
    return " ".join(name.split()).lower()


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "pillar" not in [h.strip().lower() for h in reader.fieldnames if h]:
            sys.exit(f"error: {path} needs a 'pillar' column")
        for raw in reader:
            r = {k.strip().lower(): v for k, v in raw.items() if k}
            pillar = " ".join((r.get("pillar") or "").split())
            if not pillar:
                continue
            row = {"pillar": pillar, "key": key_of(pillar), "platform": (r.get("platform") or "").strip()}
            for fld in NUM_FIELDS:
                row[fld] = hook_pct(r.get(fld)) if fld == "hook_rate" else to_num(r.get(fld))
            rows.append(row)
    if not rows:
        sys.exit(f"error: no posts with a pillar in {path}")
    return rows


def avg(values):
    vals = [v for v in values if v is not None]
    return round(sum(vals) / len(vals), 2) if vals else None


def summarise(rows):
    pillars = {}
    names = {}
    for r in rows:
        pillars.setdefault(r["key"], []).append(r)
        names.setdefault(r["key"], r["pillar"])
    out = {}
    for key, posts in pillars.items():
        with_views = [p for p in posts if p["views"] and p["views"] > 0]
        views_total = sum(p["views"] for p in with_views)
        shares = sum(p["shares"] or 0 for p in with_views)
        saves = sum(p["saves"] or 0 for p in with_views)
        follows = sum(p["follows"] or 0 for p in with_views)
        leads = sum(p["leads"] or 0 for p in posts)
        per_k = (lambda x: round(x / views_total * 1000, 2) if views_total else None)
        view_vals = [p["views"] for p in posts if p["views"] is not None]
        out[key] = {
            "name": names[key],
            "posts": len(posts),
            "posts_without_views": len(posts) - len(with_views),
            "avg_views": avg(view_vals),
            "median_views": round(statistics.median(view_vals), 2) if view_vals else None,
            "avg_hook_rate_pct": avg([p["hook_rate"] for p in posts]),
            "shares_per_1k": per_k(shares),
            "saves_per_1k": per_k(saves),
            "follows_per_1k": per_k(follows),
            "leads": leads,
            "score": per_k(shares + saves),
        }
    return out


def classify(summary):
    eligible = [s["score"] for s in summary.values() if s["score"] is not None and s["posts"] >= MIN_POSTS]
    if not eligible:
        eligible = [s["score"] for s in summary.values() if s["score"] is not None]
    median = round(statistics.median(eligible), 2) if eligible else None
    for s in summary.values():
        if s["posts"] < MIN_POSTS:
            s["status"] = "too few posts"
        elif median is None or s["score"] is None or median == 0:
            s["status"] = "no data"
        elif s["score"] >= 1.25 * median:
            s["status"] = "winner"
        elif s["score"] <= 0.75 * median:
            s["status"] = "loser"
        else:
            s["status"] = "average"
    return median


def pct_change(new, old):
    if new is None or old in (None, 0):
        return None
    return round((new - old) / old * 100, 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("current")
    ap.add_argument("--previous")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    cur = summarise(load(a.current))
    median = classify(cur)
    prev = None
    if a.previous:
        prev = summarise(load(a.previous))
        classify(prev)
        for key, s in cur.items():
            p = prev.get(key)
            s["views_change_pct"] = pct_change(s["avg_views"], p["avg_views"]) if p else None
            s["score_change_pct"] = pct_change(s["score"], p["score"]) if p else None
            if p and s["status"] == "loser" and p.get("status") == "loser":
                s["decision"] = "replace (two bad months)"
            elif s["status"] == "loser":
                s["decision"] = "adjust or watch"
            elif s["status"] == "winner":
                s["decision"] = "keep and do more"
            elif s["status"] == "too few posts":
                s["decision"] = "post more before judging"
            else:
                s["decision"] = "keep"
    else:
        for s in cur.values():
            s["decision"] = {"winner": "keep and do more", "loser": "adjust or watch",
                             "too few posts": "post more before judging"}.get(s["status"], "keep")

    result = {"account_median_score": median, "pillars": {s["name"]: s for s in cur.values()}}
    if a.json:
        print(json.dumps(result, indent=2))
        return

    def fmt(v):
        if v is None:
            return "-"
        if isinstance(v, float) and v >= 100:
            return f"{v:,.0f}"
        return f"{v:g}" if isinstance(v, float) else f"{v}"

    def change(v):
        return "-" if v is None else f"{v:+g}%"

    print("PILLAR REVIEW  (score = shares + saves per 1,000 views)")
    print(f"Account median score: {fmt(median)} (pillars with {MIN_POSTS}+ posts)")
    print()
    hdr = (f"{'Pillar':28} {'Posts':>5} {'Avg views':>10} {'Hook %':>7} {'Shr/1k':>7} {'Sav/1k':>7} "
           f"{'Fol/1k':>7} {'Leads':>6} {'Score':>7}  Status / decision")
    print(hdr)
    print("-" * len(hdr))
    for s in sorted(cur.values(), key=lambda s: (s["posts"] < MIN_POSTS, -(s["score"] or 0))):
        line = (f"{s['name'][:28]:28} {s['posts']:>5} {fmt(s['avg_views']):>10} {fmt(s['avg_hook_rate_pct']):>7} "
                f"{fmt(s['shares_per_1k']):>7} {fmt(s['saves_per_1k']):>7} {fmt(s['follows_per_1k']):>7} "
                f"{int(s['leads']):>6} {fmt(s['score']):>7}  {s['status']} / {s['decision']}")
        print(line)
        if s["posts_without_views"]:
            print(f"{'':28} note: {s['posts_without_views']} post(s) had no views and were left out of the per-1k figures")
        if prev is not None:
            print(f"{'':28} vs last month: avg views {change(s.get('views_change_pct'))}, "
                  f"score {change(s.get('score_change_pct'))}")


if __name__ == "__main__":
    main()
