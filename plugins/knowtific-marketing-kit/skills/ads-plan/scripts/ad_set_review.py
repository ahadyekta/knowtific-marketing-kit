#!/usr/bin/env python3
"""Weekly ad set review: apply the kill / keep testing / scale rules to an export.

Works with a Meta Ads Manager export (ad set level), a Google Ads report
(campaign or ad group level) or any CSV with similar columns. Report-title rows
above the header (as in Google Ads downloads) are skipped automatically, and
UTF-16 / tab-separated "CSV for Excel" files are read too. Column names are
matched loosely, e.g.:
  name:        "Ad set name", "Ad group", "Ad name", "Campaign name", "Campaign"
  spend:       "Amount spent (AUD)", "Amount spent", "Spend", "Cost"
  results:     "Results", "Leads", "Purchases", "Conversions"
  value:       "Purchases conversion value", "Conv. value", "Conversion value"  (optional, for ROAS)
  clicks:      "Link clicks", "Clicks"                                         (optional)
  impressions: "Impressions", "Impr."                                          (optional)
  frequency:   "Frequency"                                                     (optional, Meta)
  atc:         "Adds to cart", "Add to cart"                                   (optional)
Money values like "A$1,200.50", "$1,200" or "AUD 1200" are all read correctly.

Usage:
  python ad_set_review.py export.csv --target 50
  python ad_set_review.py export.csv --target 40 --close-rate 25 --target-customer 200
  python ad_set_review.py export.csv --target-roas 2.5 [--min-spend 150]
  add --json for machine-readable output.

Percentages are whole numbers: --close-rate 25 means 25%. Close rate here means
LEADS -> CUSTOMERS (the same as marketing/economics.md and ads_math.py).

Rules (from the testing method: judge only after spending 3-5x the target cost per result):
  - On/under target with spend >= 3x target          -> SCALE (raise budget gradually;
                                                         common practice is ~20-30% every few days)
  - On/under target but spend < 3x target            -> PROMISING, keep testing
  - Up to 1.5x target                                -> KEEP TESTING, iterate creative/offer
  - Above 1.5x target, spend under 5x target         -> KEEP TESTING (too early to call; e.g. $50
                                                         target, $250 spent, 3 sales = keep testing)
  - Above 2x target after 5x+ target spend           -> TURN OFF
  - 1.5-2x target after 5x+ target spend             -> KEEP TESTING, but iterate hard or replace
  - No results: spend < 3x -> keep testing; 3-5x -> CHECK tracking, form, page;
    > 5x -> TURN OFF (unless strong upstream signals, then FIX PAGE/OFFER)
  - ROAS mode uses the same 3x / 5x idea, with "target cost per sale" = average order value / target ROAS.
  - Frequency above 3 -> fatigue warning (refresh creative).
"""
import argparse
import csv
import io
import json
import re
import sys

ALIASES = {
    "name": ["ad set name", "adset name", "ad set", "ad group name", "ad group", "ad name",
             "campaign name", "campaign", "name"],
    "spend": ["amount spent (aud)", "amount spent", "amount spent (usd)", "spend", "cost"],
    "results": ["results", "leads", "purchases", "conversions", "website leads", "on-facebook leads", "conv."],
    "value": ["purchases conversion value", "purchase conversion value", "conversion value", "conv. value",
              "all conv. value", "value"],
    "clicks": ["link clicks", "clicks", "outbound clicks"],
    "impressions": ["impressions", "impr."],
    "frequency": ["frequency"],
    "atc": ["adds to cart", "add to cart", "website adds to cart"],
}
# Headers that describe a rate or a cost per something must never be taken as a raw total.
LOOSE_EXCLUDE = ("cost per", "cost /", "per ", "/", "rate", "%", "ctr", "cpm", "cpc", "roas")


def pct_arg(value, name):
    if value is None:
        return None
    if value <= 0 or value > 100:
        sys.exit(f"error: --{name} must be above 0 and at most 100 (got {value})")
    if value < 1:
        sys.exit(f"error: --{name} {value} looks like a decimal. Percentages are whole numbers: "
                 f"did you mean {value * 100:g} (i.e. {value * 100:g}%)?")
    return value


def num(v):
    """Parse a number from an export cell. Returns None for blank, '-' or unreadable values."""
    if v is None:
        return None
    s = str(v).strip()
    if s in ("", "-", "--", "—", "–"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = re.sub(r"[^0-9.\-]", "", s)  # strips A$, AUD, $, commas, %, spaces
    if s in ("", "-", ".", "-."):
        return None
    try:
        x = float(s)
    except ValueError:
        return None
    return -x if neg else x


def map_columns(headers):
    lower = {}
    for h in headers:
        if h and h.strip():
            lower.setdefault(h.strip().lower(), h)
    mapping = {}
    used = set()
    for key, options in ALIASES.items():
        found = None
        for opt in options:
            if opt in lower and lower[opt] not in used:
                found = lower[opt]
                break
        if found is None:
            for lh, orig in lower.items():
                if orig in used or any(x in lh for x in LOOSE_EXCLUDE):
                    continue
                if any(opt in lh for opt in options):
                    found = orig
                    break
        if found is not None:
            mapping[key] = found
            used.add(found)
    return mapping


def read_rows(path):
    with open(path, "rb") as f:
        raw = f.read()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        text = raw.decode("utf-16")
    else:
        text = raw.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()
    sample = "\n".join(lines[:20])
    delim = "\t" if sample.count("\t") > sample.count(",") else ","
    table = list(csv.reader(io.StringIO(text), delimiter=delim))
    # find the first row that looks like a real header (has a name and a spend column)
    for i, row in enumerate(table[:50]):
        cols = map_columns(row)
        if "name" in cols and "spend" in cols:
            headers = row
            body = table[i + 1:]
            dict_rows = [dict(zip(headers, r)) for r in body if any(c.strip() for c in r)]
            return headers, cols, dict_rows
    first = table[0] if table else []
    sys.exit("error: couldn't find a header row with a name column (ad set / ad group / campaign) and a spend "
             f"column (amount spent / spend / cost). First row was: {first}")


def verdict(spend, results, target, upstream):
    if target is None or target <= 0:
        return "NO TARGET", "Give --target (cost per result) or --target-roas."
    if not spend:
        return "NO SPEND", "Nothing spent in this period."
    multiple = spend / target
    if results and results > 0:
        cpr = spend / results
        ratio = cpr / target
        if ratio <= 1:
            if multiple >= 3:
                return "SCALE", ("On or under target after enough spend. Raise budget gradually "
                                 "(common practice: ~20-30% every few days) and watch cost per result.")
            return "PROMISING", f"Under target but only {multiple:.1f}x target spent (judge at 3-5x). Keep testing."
        if ratio <= 1.5:
            return "KEEP TESTING", f"{ratio:.2f}x target: close. Keep testing; iterate hooks, creative or offer."
        if multiple < 5:
            return "KEEP TESTING", (f"{ratio:.2f}x target but only {multiple:.1f}x target spent, too early to call. "
                                    "Keep testing and prepare new creative.")
        if ratio > 2:
            return "TURN OFF", f"{ratio:.2f}x target after {multiple:.1f}x target spend."
        return "KEEP TESTING", (f"{ratio:.2f}x target after {multiple:.1f}x target spend. Not clearly failing, "
                                "but iterate hard (new hooks/offer) or replace it with a new concept.")
    # no results
    if multiple < 3:
        return "KEEP TESTING", f"No results yet, but only {multiple:.1f}x target spent (judge at 3-5x)."
    if upstream:
        return "FIX PAGE/OFFER", "No results but strong clicks or add-to-carts: the ad works; fix landing page, form or offer."
    if multiple <= 5:
        return "CHECK", f"No results after {multiple:.1f}x target. Check tracking, the form and the page, then decide."
    return "TURN OFF", f"No results after {multiple:.1f}x target spend."


def roas_verdict(spend, value, target_roas, target_cpa):
    if not spend:
        return "NO SPEND", "Nothing spent in this period."
    roas = (value or 0) / spend
    multiple = spend / target_cpa if target_cpa else None
    if roas >= target_roas:
        if multiple is not None and multiple < 3:
            return "PROMISING", f"ROAS {roas:.2f} at/above target {target_roas:g}, but too little spend to be sure."
        return "SCALE", f"ROAS {roas:.2f} at or above target {target_roas:g}. Raise budget gradually."
    if multiple is not None and multiple < 3:
        return "KEEP TESTING", f"ROAS {roas:.2f} below target, but too little spend to judge."
    if roas >= 0.75 * target_roas:
        return "KEEP TESTING", f"ROAS {roas:.2f} close to target {target_roas:g}. Iterate creative or offer."
    if multiple is not None and multiple < 5:
        return "KEEP TESTING", f"ROAS {roas:.2f} well below target; judge again before turning off."
    return "TURN OFF", f"ROAS {roas:.2f} well below target {target_roas:g} after enough spend."


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--target", type=float, help="Target cost per result (lead or sale), AUD")
    ap.add_argument("--close-rate", type=float, help="Leads -> customers %% (shows cost per customer)")
    ap.add_argument("--target-customer", type=float, help="Target cost per customer, AUD (optional)")
    ap.add_argument("--target-roas", type=float, help="Judge by ROAS instead of cost per result")
    ap.add_argument("--min-spend", type=float,
                    help="ROAS mode: spend that counts as 3x target cost per sale (default: worked out from "
                         "average order value, or $100)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    a.close_rate = pct_arg(a.close_rate, "close-rate")
    if a.target is None and a.target_roas is None:
        sys.exit("error: give --target (cost per result) or --target-roas")
    if a.target is not None and a.target <= 0:
        sys.exit("error: --target must be positive")
    if a.target_roas is not None and a.target_roas <= 0:
        sys.exit("error: --target-roas must be positive")

    headers, cols, rows = read_rows(a.csv)
    if a.target_roas is None and "results" not in cols:
        sys.exit(f"error: need a results column (results / leads / purchases / conversions). Found: {headers}")
    if a.target_roas is not None and "value" not in cols:
        sys.exit(f"error: ROAS mode needs a conversion value column. Found: {headers}")

    def cell(r, key):
        return r.get(cols[key]) if key in cols else None

    parsed = []
    for r in rows:
        name = (cell(r, "name") or "").strip()
        if not name or name.lower().startswith("total") or name in ("--", "-"):
            continue
        raw_spend = cell(r, "spend")
        spend = num(raw_spend)
        bad_spend = spend is None and raw_spend not in (None, "") and str(raw_spend).strip() not in ("-", "--", "—")
        parsed.append({
            "name": name, "spend": spend if spend is not None else 0.0, "bad_spend": bad_spend,
            "raw_spend": raw_spend,
            "results": num(cell(r, "results")), "value": num(cell(r, "value")),
            "clicks": num(cell(r, "clicks")), "imps": num(cell(r, "impressions")),
            "freq": num(cell(r, "frequency")), "atc": num(cell(r, "atc")),
        })

    # ROAS mode: target cost per sale = average order value / target ROAS
    target_cpa_roas = None
    roas_note = None
    if a.target_roas is not None:
        if a.min_spend:
            target_cpa_roas = a.min_spend / 3
            roas_note = f"judging after ${a.min_spend:,.2f} spend (--min-spend)"
        else:
            tv = sum(p["value"] or 0 for p in parsed)
            tr = sum(p["results"] or 0 for p in parsed)
            if tv and tr:
                aov = tv / tr
                target_cpa_roas = aov / a.target_roas
                roas_note = (f"average order value ${aov:,.2f} -> target cost per sale ${target_cpa_roas:,.2f}; "
                             f"judging after ${target_cpa_roas * 3:,.2f}-${target_cpa_roas * 5:,.2f} spend")
            else:
                target_cpa_roas = 100 / 3
                roas_note = "no results column to work out order value; judging after $100 spend (set --min-spend)"

    out = []
    for p in parsed:
        spend, results = p["spend"], p["results"]
        ctr = (p["clicks"] / p["imps"] * 100) if (p["clicks"] and p["imps"]) else None
        upstream = bool((p["atc"] and p["atc"] > 0) or (ctr and ctr >= 1.5))

        if p["bad_spend"]:
            status, why = "CHECK DATA", f"Couldn't read spend value {p['raw_spend']!r}. Fix the export and re-run."
        elif a.target_roas is not None:
            status, why = roas_verdict(spend, p["value"], a.target_roas, target_cpa_roas)
        else:
            status, why = verdict(spend, results or 0, a.target, upstream)

        item = {
            "ad_set": p["name"],
            "spend": round(spend, 2),
            "results": results,
            "cost_per_result": round(spend / results, 2) if (results and not p["bad_spend"]) else None,
            "spend_vs_target": round(spend / a.target, 2) if a.target else None,
            "roas": round(p["value"] / spend, 2) if (p["value"] is not None and spend) else None,
            "ctr_pct": round(ctr, 2) if ctr is not None else None,
            "frequency": p["freq"],
            "status": status,
            "why": why,
        }
        if a.close_rate and results and not p["bad_spend"]:
            cpcust = spend / (results * a.close_rate / 100)
            item["cost_per_customer"] = round(cpcust, 2)
            if a.target_customer and cpcust > a.target_customer and status == "SCALE":
                item["status"] = "KEEP TESTING"
                item["why"] = ("Cost per lead is fine but estimated cost per customer is above target. "
                               "Check lead quality and close rate before scaling.")
        if p["freq"] and p["freq"] > 3:
            item["warning"] = "Frequency above 3: creative fatigue likely. Refresh creative."
        out.append(item)

    if not out:
        sys.exit("error: no ad set rows found under the header")

    order = {"SCALE": 0, "PROMISING": 1, "KEEP TESTING": 2, "FIX PAGE/OFFER": 3, "CHECK": 4,
             "CHECK DATA": 5, "TURN OFF": 6}
    out.sort(key=lambda x: (order.get(x["status"], 9), -(x["spend"] or 0)))

    if a.json:
        print(json.dumps(out, indent=2))
        return

    counted = [i for i in out if i["status"] != "CHECK DATA"]
    total_spend = sum(i["spend"] for i in counted)
    total_results = sum(i["results"] or 0 for i in counted)
    print("AD SET REVIEW")
    print(f"Columns used: " + ", ".join(f"{k}='{v}'" for k, v in cols.items()))
    if a.target:
        print(f"Target cost per result: ${a.target:,.2f}  (judge after ${a.target * 3:,.2f}-${a.target * 5:,.2f} spend)")
    if a.target_roas:
        print(f"Target ROAS: {a.target_roas:g} ({roas_note})")
    print(f"Total spend ${total_spend:,.2f} | results {total_results:g}"
          + (f" | blended cost per result ${total_spend / total_results:,.2f}" if total_results else "")
          + (f" | {len(out) - len(counted)} row(s) with unreadable spend left out" if len(counted) < len(out) else ""))
    print()
    for i in out:
        cpr = f"${i['cost_per_result']:,.2f}" if i["cost_per_result"] is not None else "-"
        extra = f" | ROAS {i['roas']}" if i.get("roas") is not None else ""
        extra += f" | cost/customer ${i['cost_per_customer']:,.2f}" if i.get("cost_per_customer") else ""
        extra += f" | CTR {i['ctr_pct']}%" if i.get("ctr_pct") is not None else ""
        extra += f" | freq {i['frequency']:g}" if i.get("frequency") is not None else ""
        print(f"[{i['status']}] {i['ad_set']}")
        res = f"{i['results']:g}" if i["results"] is not None else "-"
        print(f"    spend ${i['spend']:,.2f} | results {res} | cost/result {cpr}{extra}")
        print(f"    {i['why']}")
        if i.get("warning"):
            print(f"    WARNING: {i['warning']}")


if __name__ == "__main__":
    main()
