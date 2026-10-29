---
name: social-plan
description: Builds or fixes a client's organic social strategy (choose the primary platform and Instagram approach, account setup checks, content types and pillars, cadence, cross-posting, CTA timing, comment and DM engagement, batching and sets, team roles, collaborator pillar) and runs the monthly pillar review from exported post data with pillar_report.py to decide what to keep, change or replace. Use when starting social for a client, when an account isn't working, for "how often should we post", or each month to review results.
argument-hint: "[plan | review | audit]"
---

# Social plan

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/content-and-social.md` in full first.

## Mode 1: Plan (default)

**Inputs:** `marketing/brand.md`, `brand-world.md` (characters, sets), `channels.md` (accounts), `content-plan.md`. Ask: who can be on camera, how much time per week, any platform they already have traction on, goals (awareness, leads, sales).

**Decide and write into `marketing/content-plan.md`:**
1. **Primary platform** (usually Instagram; LinkedIn for B2B; YouTube as a second for service businesses with someone good on camera). Cross-post list.
2. **Approach**: expert on camera (default), storytelling, or art-directed; or faceless (carousels, POV) if needed. Expert vs student perspective.
3. **Pillars**: 3–5 formats (type × format combinations), each with 3 example ideas specific to the client.
4. **Cadence**: new/reset accounts 4–6 posts/week (2–3 combos × 2/week) for a month before judging; established accounts 3–4 per pillar per month (12–16).
5. **Funnel mix**: top/middle/bottom split; no hard CTAs until posts reach roughly 5,000 views (2,000 in small niches), then lead magnet via bio or comment-to-DM.
6. **Engagement process**: who replies to comments and DMs, within what time; proactive DM rules for qualified commenters; handoff to sales.
7. **Production**: batch filming every two weeks, run sheet, set improvements, equipment.
8. **Team**: social manager + on-camera person (+ creators or a collaborator pillar later).
9. **Metrics**: per post (hook rate, views, saves, shares); monthly (reach, leads, attributable sales).
10. **Timeline**: what to expect at 1, 3 and 6 months.

Offer to generate the first month's ideas with `content-ideas`.

## Mode 2: Account audit
Check each account against: account type (creator vs business on TikTok), country/location set-up, bio (what we do / why follow / CTA + link), profile image and highlights, last 30 posts (types, faces, hooks, consistency), view trend, replies to comments and DMs, cross-posting, scheduling tool use (recommend posting natively and testing). Output a short fix list.

## Mode 3: Monthly pillar review
1. Get the data: export or paste the month's posts (date, platform, pillar, views, likes, comments, shares, saves, hook rate or average watch %, follows gained, leads). If insights aren't exported, ask the user to tag each post with its pillar.
2. Save as CSV and run:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/social-plan/scripts/pillar_report.py" posts.csv [--previous last_month.csv]
```
(On Windows use `python` or `py`.) The script compares pillars on averages and per-1,000-view rates, flags winners and losers, and (with `--previous`) month-over-month change and pillars underperforming two months in a row.
3. Decide per pillar: keep / adjust (what to change) / replace (with what new test pillar).
4. Write the monthly results table in `content-plan.md` and draft the monthly social report (see `weekly-report` skill): what we posted, top performers, what's improving, what we're changing.

## CSV columns for pillar_report.py
`date,platform,pillar,views,likes,comments,shares,saves,hook_rate,follows,leads` (hook_rate as a % number; unknown values can be blank).
