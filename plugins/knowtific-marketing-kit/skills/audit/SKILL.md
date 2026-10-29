---
name: audit
description: Runs a full marketing audit of a client business across every area (positioning and brand, website and landing pages, funnel and follow-up, tracking, SEO and Google Business Profile, organic social, paid ads, email/SMS, creators and partners, sales support, reviews and reputation, compliance) and produces a scorecard, prioritised fixes and a 30/60/90-day plan that names which skill to run for each step. Use when taking on a new client, when the user says "check everything", "where should we start", or "what's wrong with this company's marketing", or for a quarterly health check.
argument-hint: "[website URL, optional]"
---

# Full marketing audit

## 1. Gather inputs (in parallel where possible)
- `marketing/` folder if present (run `init` first if not, or proceed with what's available and list gaps).
- The codebase (if this is the client's site) and/or the live URL (`$ARGUMENTS`).
- Launch these agents in parallel when available:
  - `site-auditor`: positioning, messaging, CTAs, proof, tracking, technical/SEO basics from the site or code
  - `market-researcher`: 3–5 competitors' claims, offers, review themes, visible ads, and the client's own review themes
  - `landing-page-reviewer`: on the 1–3 most important pages (the ones ads or GBP send traffic to)
  - In each agent prompt, include the project path and/or URL, the `marketing/` files that exist, and these reference paths exactly as written here (agents may not resolve plugin paths themselves): rubric `${CLAUDE_PLUGIN_ROOT}/skills/lp-review/references/checklist.md`, page structures `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md`, compliance `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`.
- Connections, if available (see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/tools.md`): GA4, Google Ads, Meta Ads, Search Console, DataForSEO (rank and keyword gaps), Klaviyo, PageSpeed. Otherwise ask for exports or screenshots and note what wasn't checked.
- Ask the owner the money questions if missing: job value, margin, close rate, lead volume, ad spend, response time.

## 2. Score each area 0–5
Use `${CLAUDE_PLUGIN_ROOT}/skills/audit/references/audit-rubric.md`. For each area give: score, evidence (what you saw), the biggest problem, and the fix.

Areas:
1. Positioning and messaging
2. Offer and lead magnets
3. Website and landing pages
4. Funnel and follow-up (speed to touch, thank-you page, touches, close assets)
5. Tracking and measurement
6. Local SEO and Google Business Profile (or SEO for non-local)
7. Reviews and reputation
8. Organic social
9. Paid ads
10. Email and SMS
11. Creators, partners and events
12. Sales support and process
13. Compliance
14. Brand identity and design

## 3. Prioritise
Rank fixes by **impact × ease**, following the order of operations:
1. Broken basics that leak money now (tracking missing, form broken, slow lead response, no thank-you page, GBP problems)
2. Positioning and offer (everything downstream depends on them)
3. Conversion (landing pages, follow-up, close assets)
4. Demand (ads, SEO, social, creators, outbound)
5. Narrative and scale (campaigns, email calendar, partnerships)

Use `funnel_math.py` (funnel-build skill) to show what the top 2–3 conversion fixes are worth in leads and jobs per month.

## 4. Output
Save to `marketing/audits/audit-YYYY-MM-DD.md`:

```
# Marketing audit: <business> (<date>)

## Summary
3–5 sentences: overall state, the one biggest opportunity, expected impact.

## Scorecard
| Area | Score /5 | Biggest problem | Fix |
|---|---|---|---|
...
Overall: __/70

## Top 5 fixes (in order)
1. <fix>: why, expected impact, effort, skill to run
...

## 30 / 60 / 90-day plan
- Days 1–30: ...
- Days 31–60: ...
- Days 61–90: ...

## Not checked (needs access or data)
- ...
```

Then give the user a short summary in chat and offer to start fix #1.

## Rules
- Evidence for every score: quote copy, cite pages, show numbers. Don't guess.
- Never invent reviews, rankings or metrics. Mark estimates clearly.
- Flag compliance issues even if minor.
- Keep the plan realistic for the client's budget and team size.
- Use plain English; the client may read this.
