---
name: weekly-report
description: Writes the weekly client or boss update (wins with numbers, next week's priorities, blockers and what's needed from whom, key stats) and the monthly report (social pillars, ads, funnel, SEO and Google Business Profile, email, plan for next month), pulling numbers from connected ad, analytics and email tools or from pasted exports, plus team roll-ups for agencies. Use at the end of each week or month, when the user asks for a client report, an update email, or a summary of marketing results.
argument-hint: "[weekly | monthly | rollup]"
---

# Weekly and monthly reports

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/pr-and-narrative.md` sections 3–4.

## Gather
1. Numbers for the period (and the previous one for comparison). Use connections if available (GA4, Google Ads, Meta Ads, Klaviyo, Search Console; see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/tools.md`); otherwise ask for exports or the figures.
   - Leads (by source), cost per lead, ad spend, bookings/jobs won, revenue if known
   - Response time to leads, close rate
   - Website sessions and landing page conversion
   - Social: reach, top posts, follows, leads from social
   - Email/SMS: sends, opens/clicks, flow revenue or bookings
   - GBP: calls, website clicks, direction requests, new reviews
2. What was done this period (from `marketing/ads/log.md`, `content-plan.md`, campaign files, and the user).
3. What's planned next and what's blocked.

## Weekly format (email-ready)
```
Subject: [Business] marketing update, week of [date]

Wins
- [win with number and comparison]
- ...

Next week
1. [priority]
2. ...

Blockers / what we need
- [what, from whom, by when]

Stats
| Metric | This week | Last week |
|---|---|---|
| Leads | | |
| Cost per lead | | |
| Ad spend | | |
| Avg response time | | |
| Jobs booked | | |
| Site visits | | |
```
Keep it to one screen. Lead with the most important win. Cheerlead genuine wins; flag problems early with a plan.

## Monthly format
Sections: summary (3 sentences); results vs targets; ads (best and worst, tests next month); social pillars (from the pillar review: keep/change/replace); funnel (page conversion, close rate, speed to touch); SEO and GBP; email and SMS; next month's plan; decisions needed from the client.

## Roll-up mode (agency or team)
Combine each team lead's or each client's wins/next/blockers/stats into one summary: the biggest wins, the biggest blockers (with who needs to act), and the stats that matter.

## Output
Save to `marketing/reports/weekly-YYYY-MM-DD.md` or `monthly-YYYY-MM.md`, and show the email-ready text in chat.

## Rules
- Never invent or round numbers misleadingly; mark estimates.
- Same metrics every week so trends are visible.
- Plain English; the client should understand it in 60 seconds.
