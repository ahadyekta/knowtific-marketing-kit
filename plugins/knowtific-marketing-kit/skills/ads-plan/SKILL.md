---
name: ads-plan
description: Plans and manages a client's paid ads: platform choice and order (Google Search first for urgent local services, Meta for demand creation), tracking prerequisites, Meta campaign/ad set structure (ABO, one concept per ad set, 3–10 ads, budgets, audiences, placements, naming), Google Search structure (keywords, negatives, assets, location), a 4-week test plan, and the weekly review that applies kill/keep/scale rules to an export with ad_set_review.py. Use when setting up or restructuring ads, asking "how should we run Meta/Google ads", or each week to review ad results.
argument-hint: "[setup | weekly-review]"
---

# Ads plan

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/ads.md` in full, and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/tools.md` for ad account connections.

## Before anything: prerequisites
1. **Economics.** Run `ads-math` (or read `marketing/economics.md`) for the target cost per lead/sale and per customer.
2. **Tracking.** Meta pixel + Conversions API, Google Ads conversions (forms and calls), GA4 events, UTMs. If missing, the first task is fixing tracking.
3. **Landing page.** A dedicated page per offer (run `lp-review`).
4. **Follow-up.** Leads answered within minutes (see funnel-build).
If any is missing, say so plainly and put it first in the plan.

## Mode 1: Setup / restructure

1. **Platform mix and order** for this client, with reasons and a budget split.
2. **Meta structure:**
   - Campaign: objective (Sales or Leads), naming
   - Budget type: ABO (ad set budgets, budget sharing off) unless the account has lots of data
   - Ad sets: one concept each, 3–10 genuinely different ads; daily budget per ad set (about A$50–75/day per ad set, or whatever reaches 3–5× target cost per lead in about 5 days; run `ads-math`); audience (custom audiences + lookalike ~3% → broad when data exists; interests only with no data; location radius = service area); placements; optimisation and bid strategy (highest volume to start)
   - Naming convention: `Audience | Creative type | Week`
3. **Google Search structure** (local services): campaigns by service theme, phrase/exact keywords with suburb and intent modifiers, negative keyword list, location targeting (presence), assets (call, location, sitelinks, callouts, snippets), landing page per theme, bidding plan, brand campaign if needed.
4. **Creative plan:** first ad sets drawn from `ad-concepts` (spread across the concept checklist), creative diversity, partnership ads from creators.
5. **4-week test plan:** week-by-week new ad sets, budgets, and the decision rule (judge after 3–5× target cost per result).
6. **Measurement:** custom columns to set in Ads Manager; weekly review day; what goes in the weekly report.

Save to `marketing/ads/ads-plan.md`.

## Mode 2: Weekly review

1. **Get the data.** If a Meta or Google Ads connection is available, read last 7 days (and 30 days) at ad set and ad level. Otherwise ask for an Ads Manager CSV export at ad set level (name, amount spent, results, link clicks, impressions, frequency, value if e-commerce), or a Google Ads campaign or ad group report (the script skips the report-title rows and reads "A$" amounts).
2. **Run the rules:**
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/ads-plan/scripts/ad_set_review.py" export.csv --target 40 [--close-rate 25 --target-customer 200] [--target-roas 2.5]
```
(Windows: `python` or `py`.) `--target` is the affordable cost per lead or sale from `ads-math`; `--close-rate` is leads → customers as a whole number (25 = 25%). The script prints which columns it used; check they're right.
3. **Interpret:** what to scale, keep testing, fix (landing page/offer) or turn off; fatigue warnings; patterns by audience and creative type (from naming); for Google, search terms to add as negatives or new keywords.
4. **Next week's tests:** 2–3 new ad sets based on what's winning (new hooks and angles on winning concepts; one wild-card concept). Use `ad-concepts` for the creative and briefs.
5. **Log it** in `marketing/ads/log.md`: date, decisions, tests launched, results.
6. **Changes:** list exact budget/pause changes for the user to make. Only make changes through a connection if the user explicitly asks for that specific change now. Never create or publish ads via automation.

Feed the summary into `weekly-report`.

## Rules
- Service businesses: judge on cost per customer, not just cost per lead.
- Under ~10 results, treat numbers as directional.
- Respect platform policies (special ad categories for housing, employment, credit; health claims).
