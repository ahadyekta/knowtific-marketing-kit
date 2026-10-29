#!/usr/bin/env python3
"""Funnel maths: what each stage is worth, and what improvements are worth.

Stages:  visitors -> leads (page conversion) -> qualified -> booked/met -> customers (close)

Traffic can be given directly (--visitors) or from ad spend and cost per click
(--spend and --cpc). If you give --visitors and --spend, the implied cost per
click (spend / visitors) is used so that spend or cpc scenarios change traffic.
Percentages are whole numbers (8 = 8%).

IMPORTANT: --close-rate here is BOOKED/QUOTED -> CUSTOMER, the last step only.
If you only know leads -> customers (the close rate in marketing/economics.md and
ads_math.py), leave --qualified and --booked at 100 and use that number.

Examples:
  python funnel_math.py --visitors 1200 --lp-cvr 4 --close-rate 25 --job-value 2500 --margin 40
  python funnel_math.py --spend 1500 --cpc 3 --lp-cvr 4 --qualified 70 --booked 80 --close-rate 35 \
      --job-value 2500 --margin 40 --scenario lp-cvr=8 --scenario close-rate=45 --scenario lp-cvr=8,close-rate=45

Scenarios change one or more inputs and show the difference against the baseline,
so you can see which fix is worth most (page conversion, qualification, show-up, close rate, job value).
"""
import argparse
import copy
import json
import sys

KEYS = ["visitors", "spend", "cpc", "lp_cvr", "qualified", "booked", "close_rate", "job_value", "margin"]
PCT_KEYS = ["lp_cvr", "qualified", "booked", "close_rate", "margin"]


def flag(k):
    return "--" + k.replace("_", "-")


def check_value(k, v, where="argument"):
    """Validate one input. Percentages are whole numbers; catch decimals typed by mistake."""
    if v is None:
        return
    if k in PCT_KEYS:
        if not (0 <= v <= 100):
            sys.exit(f"error: {flag(k)} must be 0-100 (got {v:g} in {where})")
        if 0 < v < 1:
            if k == "lp_cvr":
                print(f"note: treating {flag(k)} {v:g} as {v:g}%. If you meant {v * 100:g}%, type {v * 100:g}.",
                      file=sys.stderr)
            else:
                sys.exit(f"error: {flag(k)} {v:g} looks like a decimal. Percentages are whole numbers: "
                         f"did you mean {v * 100:g} (i.e. {v * 100:g}%)?")
    elif v < 0:
        sys.exit(f"error: {flag(k)} can't be negative (got {v:g} in {where})")
    if k == "cpc" and v == 0:
        sys.exit(f"error: {flag(k)} must be above 0")


def calc(p):
    visitors = p["visitors"]
    if visitors is None:
        if p["spend"] is None or not p["cpc"]:
            sys.exit("error: give --visitors, or --spend and --cpc")
        visitors = p["spend"] / p["cpc"]
    leads = visitors * p["lp_cvr"] / 100
    qualified = leads * p["qualified"] / 100
    booked = qualified * p["booked"] / 100
    customers = booked * p["close_rate"] / 100
    revenue = customers * p["job_value"] if p["job_value"] else None
    gross = revenue * p["margin"] / 100 if (revenue is not None and p["margin"] is not None) else None
    spend = p["spend"]
    r = {
        "visitors": round(visitors, 1),
        "leads": round(leads, 1),
        "qualified_leads": round(qualified, 1),
        "booked": round(booked, 1),
        "customers": round(customers, 2),
        "revenue": round(revenue, 2) if revenue is not None else None,
        "gross_profit": round(gross, 2) if gross is not None else None,
        "lead_to_customer_pct": round(customers / leads * 100, 1) if leads else None,
    }
    if spend:
        r["cost_per_lead"] = round(spend / leads, 2) if leads else None
        r["cost_per_customer"] = round(spend / customers, 2) if customers else None
        if gross is not None:
            r["profit_after_ads"] = round(gross - spend, 2)
            r["roas"] = round(revenue / spend, 2) if revenue else None
    return r


def parse_scenario(text):
    changes = {}
    for part in text.split(","):
        if "=" not in part:
            sys.exit(f"error: scenario '{text}' should look like lp-cvr=8,close-rate=40")
        k, v = part.split("=", 1)
        k = k.strip().replace("-", "_")
        if k not in KEYS:
            sys.exit(f"error: unknown scenario key '{k}'. Use one of: {', '.join(x.replace('_','-') for x in KEYS)}")
        try:
            val = float(v.strip().replace("%", "").replace("$", "").replace(",", ""))
        except ValueError:
            sys.exit(f"error: scenario value '{v.strip()}' for {k.replace('_', '-')} is not a number")
        check_value(k, val, where=f"scenario '{text}'")
        changes[k] = val
    return changes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--visitors", type=float)
    ap.add_argument("--spend", type=float, help="Monthly ad spend, AUD")
    ap.add_argument("--cpc", type=float, help="Cost per click, AUD")
    ap.add_argument("--lp-cvr", type=float, required=True, help="Landing page conversion %%")
    ap.add_argument("--qualified", type=float, default=100, help="%% of leads that are qualified (default 100)")
    ap.add_argument("--booked", type=float, default=100, help="%% of qualified leads that book/meet/get quoted (default 100)")
    ap.add_argument("--close-rate", type=float, required=True,
                    help="%% of booked/quoted that become customers (last step only; see note above)")
    ap.add_argument("--job-value", type=float, help="Average job/order value, AUD")
    ap.add_argument("--margin", type=float, help="Gross margin %%")
    ap.add_argument("--scenario", action="append", default=[], help="e.g. lp-cvr=8 or lp-cvr=8,close-rate=40")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    base = {k: getattr(a, k) for k in KEYS}
    for k in KEYS:
        check_value(k, base.get(k))
    notes = []
    if base["visitors"] is not None and base["spend"]:
        implied = base["spend"] / base["visitors"] if base["visitors"] else None
        if base["cpc"] and implied and abs(base["cpc"] - implied) / implied > 0.05:
            notes.append(f"--visitors and --spend imply a ${implied:,.2f} CPC, not the --cpc ${base['cpc']:,.2f} given; "
                         "using visitors for the baseline.")
        if implied and not base["cpc"]:
            base["cpc"] = round(implied, 4)
    if base["qualified"] < 100 or base["booked"] < 100:
        notes.append("--close-rate is treated as booked/quoted -> customer. If your number is leads -> customers, "
                     "set --qualified and --booked to 100.")
    baseline = calc(base)

    results = {"inputs": base, "baseline": baseline, "scenarios": [], "notes": notes}
    for s in a.scenario:
        p = copy.deepcopy(base)
        changes = parse_scenario(s)
        p.update(changes)
        # spend or cpc changes must change traffic, unless the scenario sets visitors itself
        if ("spend" in changes or "cpc" in changes) and "visitors" not in changes:
            if p["spend"] is None or not p["cpc"]:
                sys.exit("error: spend/cpc scenarios need both a spend and a cpc (or --visitors with --spend)")
            p["visitors"] = None
        r = calc(p)
        diff = {}
        for key in ["leads", "customers", "revenue", "gross_profit", "profit_after_ads"]:
            if r.get(key) is not None and baseline.get(key) is not None:
                diff[key] = round(r[key] - baseline[key], 2)
        results["scenarios"].append({"changes": {k.replace('_', '-'): v for k, v in changes.items()}, "result": r, "difference": diff})

    if a.json:
        print(json.dumps(results, indent=2))
        return

    def show(r):
        lines = [
            f"  Visitors {r['visitors']:,.0f} -> leads {r['leads']:,.1f} -> qualified {r['qualified_leads']:,.1f} "
            f"-> booked {r['booked']:,.1f} -> customers {r['customers']:,.2f}",
        ]
        money = []
        if r.get("revenue") is not None:
            money.append(f"revenue ${r['revenue']:,.0f}")
        if r.get("gross_profit") is not None:
            money.append(f"gross profit ${r['gross_profit']:,.0f}")
        if r.get("cost_per_lead") is not None:
            money.append(f"CPL ${r['cost_per_lead']:,.2f}")
        if r.get("cost_per_customer") is not None:
            money.append(f"cost/customer ${r['cost_per_customer']:,.2f}")
        if r.get("profit_after_ads") is not None:
            money.append(f"profit after ads ${r['profit_after_ads']:,.0f}")
        if money:
            lines.append("  " + " | ".join(money))
        return "\n".join(lines)

    print("FUNNEL MATHS (per month)")
    for n in notes:
        print(f"Note: {n}")
    print("Baseline")
    print(show(baseline))
    for sc in results["scenarios"]:
        ch = ", ".join(f"{k}={v:g}" for k, v in sc["changes"].items())
        print()
        print(f"Scenario: {ch}")
        print(show(sc["result"]))
        d = sc["difference"]
        if d:
            parts = []
            if "leads" in d:
                parts.append(f"{d['leads']:+.1f} leads")
            if "customers" in d:
                parts.append(f"{d['customers']:+.2f} customers")
            money_delta = lambda v: ("+" if v >= 0 else "-") + f"${abs(v):,.0f}"
            if "revenue" in d:
                parts.append(f"{money_delta(d['revenue'])} revenue")
            if "gross_profit" in d:
                parts.append(f"{money_delta(d['gross_profit'])} gross profit")
            if "profit_after_ads" in d:
                parts.append(f"{money_delta(d['profit_after_ads'])} profit after ads")
            print("  vs baseline: " + ", ".join(parts))


if __name__ == "__main__":
    main()
