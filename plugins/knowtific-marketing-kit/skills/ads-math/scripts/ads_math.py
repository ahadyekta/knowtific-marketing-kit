#!/usr/bin/env python3
"""Ads maths for service businesses.

Works out affordable and break-even cost per lead from job economics,
a testing budget, a feasibility check from CPC and landing page conversion,
and a verdict on current results.

Percentages are whole numbers: --close-rate 25 means 25%.
"""
import argparse
import json
import sys


def pct(value, name):
    if value is None:
        return None
    if value < 0 or value > 100:
        sys.exit(f"error: --{name} must be between 0 and 100 (got {value})")
    return value / 100.0


def money(x):
    return None if x is None else round(x, 2)


def calculate(a):
    margin = pct(a.margin, "margin")
    close = pct(a.close_rate, "close-rate")
    share = pct(a.spend_share, "spend-share")
    lp_cvr = pct(a.lp_cvr, "lp-cvr")

    if a.job_value <= 0:
        sys.exit("error: --job-value must be positive")
    if close == 0:
        sys.exit("error: --close-rate must be above 0")

    gross_profit = a.job_value * margin
    affordable_cpa = gross_profit * share
    breakeven_cpa = gross_profit
    affordable_cpl = affordable_cpa * close
    breakeven_cpl = breakeven_cpa * close
    leads_per_job = 1 / close

    out = {
        "inputs": {
            "job_value": a.job_value,
            "margin_pct": a.margin,
            "close_rate_pct": a.close_rate,
            "spend_share_pct": a.spend_share,
        },
        "per_job": {
            "gross_profit": money(gross_profit),
            "leads_needed_per_job": round(leads_per_job, 2),
        },
        "targets": {
            "affordable_cost_per_customer": money(affordable_cpa),
            "breakeven_cost_per_customer": money(breakeven_cpa),
            "affordable_cpl": money(affordable_cpl),
            "breakeven_cpl": money(breakeven_cpl),
            "breakeven_roas": round(1 / margin, 2) if margin else None,
            "target_roas": round(a.job_value / affordable_cpa, 2) if affordable_cpa else None,
        },
        "testing": {
            "spend_per_ad_set_min": money(affordable_cpl * 3),
            "spend_per_ad_set_max": money(affordable_cpl * 5),
            "daily_budget_5_day_test": money(affordable_cpl * 4 / 5),
        },
    }

    if a.repeat_value:
        ltv_profit = (a.job_value + a.repeat_value) * margin
        out["ltv"] = {
            "twelve_month_value": money(a.job_value + a.repeat_value),
            "affordable_cpl_on_ltv": money(ltv_profit * share * close),
            "note": "Only use the LTV ceiling if the business can wait to earn the repeat value back.",
        }

    if a.cpc is not None and lp_cvr:
        expected_cpl = a.cpc / lp_cvr
        needed_cvr = a.cpc / affordable_cpl if affordable_cpl else None
        out["feasibility"] = {
            "cpc": a.cpc,
            "lp_cvr_pct": a.lp_cvr,
            "expected_cpl": money(expected_cpl),
            "expected_cost_per_customer": money(expected_cpl / close),
            "within_target": expected_cpl <= affordable_cpl,
            "lp_cvr_needed_for_target_pct": round(needed_cvr * 100, 2) if needed_cvr else None,
        }

    if a.spend is not None and a.leads is not None:
        actual_cpl = a.spend / a.leads if a.leads else None
        actual_cpa = a.spend / a.jobs if a.jobs else None
        if a.leads == 0:
            if a.spend < affordable_cpl * 3:
                status = "keep_testing"
                verdict = "No leads yet, but spend is under 3x the affordable CPL. Keep testing."
            elif a.spend <= affordable_cpl * 5:
                status = "check_tracking"
                verdict = (
                    "No leads after 3-5x the affordable CPL. Check tracking and the form work, "
                    "then give it until 5x before stopping."
                )
            else:
                status = "stop_or_fix"
                verdict = "No leads after more than 5x the affordable CPL. Stop this ad set or fix the landing page and offer."
        elif a.jobs is not None and a.jobs == 0 and a.leads >= leads_per_job * 2:
            status = "fix_follow_up"
            verdict = (
                "Leads are coming in but none have closed. Check lead quality, response speed "
                "and follow-up before spending more."
            )
        elif a.jobs and (a.spend / a.jobs) > breakeven_cpa:
            status = "fix_or_stop"
            verdict = (
                "Cost per job is above break-even even though leads arrive. Improve close rate "
                "(speed, follow-up, quote) or lead quality before scaling."
            )
        elif a.jobs and (a.spend / a.jobs) > affordable_cpa:
            status = "keep_testing"
            verdict = "Cost per job is above target but still profitable. Improve close rate or CPL before scaling."
        elif actual_cpl <= affordable_cpl:
            status = "scale"
            verdict = "On or under target CPL. Increase budget gradually (about 20-30% every few days)."
        elif actual_cpl <= breakeven_cpl:
            status = "keep_testing"
            verdict = "Above target but still profitable. Keep testing new creative and improve the landing page."
        else:
            status = "fix_or_stop"
            verdict = "Above break-even CPL. Fix the offer or landing page, or stop this ad set."

        out["current"] = {
            "spend": a.spend,
            "leads": a.leads,
            "jobs": a.jobs,
            "actual_cpl": money(actual_cpl),
            "actual_cost_per_customer": money(actual_cpa),
            "actual_close_rate_pct": round(a.jobs / a.leads * 100, 1) if (a.jobs is not None and a.leads) else None,
            "status": status,
            "verdict": verdict,
            "small_sample": a.leads < 10,
        }

    return out


def print_text(r):
    t = r["targets"]
    p = r["per_job"]
    s = r["testing"]
    print("ADS MATHS")
    print(f"  Gross profit per job:        ${p['gross_profit']:,.2f}")
    print(f"  Leads needed per job:        {p['leads_needed_per_job']}")
    print()
    print("TARGETS")
    print(f"  Affordable cost per customer: ${t['affordable_cost_per_customer']:,.2f}")
    print(f"  Break-even cost per customer: ${t['breakeven_cost_per_customer']:,.2f}")
    print(f"  Affordable CPL:               ${t['affordable_cpl']:,.2f}")
    print(f"  Break-even CPL:               ${t['breakeven_cpl']:,.2f}")
    print(f"  Break-even ROAS:              {t['breakeven_roas']}")
    print(f"  Target ROAS:                  {t['target_roas']}")
    print()
    print("TESTING")
    print(f"  Spend per ad set before judging: ${s['spend_per_ad_set_min']:,.2f} to ${s['spend_per_ad_set_max']:,.2f}")
    print(f"  Daily budget for a 5-day test:   ${s['daily_budget_5_day_test']:,.2f}")

    if "ltv" in r:
        l = r["ltv"]
        print()
        print("LIFETIME VALUE")
        print(f"  12-month value:               ${l['twelve_month_value']:,.2f}")
        print(f"  Affordable CPL on LTV:        ${l['affordable_cpl_on_ltv']:,.2f}")
        print(f"  Note: {l['note']}")

    if "feasibility" in r:
        f = r["feasibility"]
        print()
        print("FEASIBILITY")
        print(f"  Expected CPL (CPC ${f['cpc']} / LP conversion {f['lp_cvr_pct']}%): ${f['expected_cpl']:,.2f}")
        print(f"  Expected cost per customer:   ${f['expected_cost_per_customer']:,.2f}")
        print(f"  Within target:                {'yes' if f['within_target'] else 'no'}")
        print(f"  LP conversion needed for target: {f['lp_cvr_needed_for_target_pct']}%")

    if "current" in r:
        c = r["current"]
        print()
        print("CURRENT RESULTS")
        print(f"  Spend ${c['spend']:,.2f} | Leads {c['leads']} | Jobs {c['jobs']}")
        if c["actual_cpl"] is not None:
            print(f"  Actual CPL:                   ${c['actual_cpl']:,.2f}")
        if c["actual_cost_per_customer"] is not None:
            print(f"  Actual cost per customer:     ${c['actual_cost_per_customer']:,.2f}")
        if c["actual_close_rate_pct"] is not None:
            print(f"  Actual close rate:            {c['actual_close_rate_pct']}%")
        print(f"  Status:  {c['status']}")
        print(f"  Verdict: {c['verdict']}")
        if c["small_sample"]:
            print("  Caution: fewer than 10 leads, treat as directional.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--job-value", type=float, required=True, help="Average job value in AUD")
    ap.add_argument("--margin", type=float, required=True, help="Gross margin %% (e.g. 40)")
    ap.add_argument("--close-rate", type=float, required=True, help="Leads to paying jobs %% (e.g. 25)")
    ap.add_argument("--spend-share", type=float, default=30, help="Share of gross profit to spend per job %% (default 30)")
    ap.add_argument("--repeat-value", type=float, help="Extra value per customer over 12 months, AUD")
    ap.add_argument("--lp-cvr", type=float, help="Landing page conversion rate %%")
    ap.add_argument("--cpc", type=float, help="Cost per click, AUD")
    ap.add_argument("--spend", type=float, help="Current ad spend, AUD")
    ap.add_argument("--leads", type=int, help="Current leads")
    ap.add_argument("--jobs", type=int, help="Current jobs won")
    ap.add_argument("--json", action="store_true", help="Print JSON")
    a = ap.parse_args()

    r = calculate(a)
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        print_text(r)


if __name__ == "__main__":
    main()
