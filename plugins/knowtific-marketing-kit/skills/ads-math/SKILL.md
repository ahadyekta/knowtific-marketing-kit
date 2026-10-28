---
name: ads-math
description: Calculates the affordable cost per lead, cost per customer, break-even ROAS and test budget for a client's paid ads from job value, margin and close rate, and judges existing ad results against those targets. Use before launching ads, when setting an ad budget, when the user asks whether a cost per lead is good, or when deciding to scale or kill an ad set.
---

# Ads maths

## Inputs
Read `marketing/economics.md` if it exists. Otherwise ask for:
- Average job value (AUD)
- Gross margin % (after materials and labour)
- Close rate % (leads → paying jobs)
- Share of gross profit the owner will spend to win a job (default 30% if unknown; say so)
- Optional: 12-month repeat/referral value, landing page conversion rate, cost per click, current spend/leads/jobs

## Run the calculator

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/ads-math/scripts/ads_math.py" \
  --job-value 2500 --margin 40 --close-rate 25 --spend-share 30 \
  [--repeat-value 800] [--lp-cvr 8] [--cpc 3.5] \
  [--spend 1200 --leads 22 --jobs 5]
```

All percentages are whole numbers (25 = 25%). Use `--json` for machine-readable output. Don't do this maths in your head; run the script. On Windows, if `python3` isn't found, use `python` or `py` instead.

## Explain the result in plain English
1. **Affordable CPL** and **max CPL (break-even)**: what a lead can cost and still make money.
2. **Testing budget**: how much to spend per ad set before judging (3–5× target CPL), and the daily budget for a 5-day test.
3. **Feasibility check** if CPC and landing page conversion were given: expected CPL vs target. If expected CPL is above target, say which lever fixes it fastest (landing page conversion, close rate, offer, or job value via bundles).
4. **Verdict on current results** if spend/leads/jobs were given: scale / keep testing / fix landing page or follow-up / stop.
5. One next action.

## Update the project
Offer to write the target figures into `marketing/economics.md` (Targets section).

## Notes
- Service businesses: cost per customer matters more than cost per lead. A cheap lead that never closes is expensive.
- If repeat value is given, also show the LTV-based ceiling, and note that it only makes sense if the business can wait to earn it back.
- Leads are judged over enough volume. Under ~10 leads, treat numbers as directional.
