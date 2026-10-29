# Knowtific Marketing Kit: working notes

This repo is a Claude Code plugin marketplace (`knowtific`) containing one plugin (`knowtific-marketing-kit`). It packages a full marketing toolkit for Knowtific's client projects so it can be added to any project from GitHub.

## Owner and context
- Ahad, Knowtific (knowtific.com.au, Melbourne): websites, local SEO, Google Ads, CRM setup, AI automations for small businesses, mainly tradies and allied health, open to other industries and Meta/Instagram ads work.
- Stack preference: Next.js/React, Cloudflare (Workers, D1) or Supabase. Avoid anything that needs a server to maintain.
- Goal: get fundamentally strong at improving businesses' marketing, and have a tool that, when added to a project, checks everything, suggests what to do, reviews landing pages, helps with rebrands, redesigns, content and ads, and answers marketing questions from these frameworks.

## Sources
Built from seven videos by the same marketing practitioner (a full marketing course; the art of the marketing campaign; every type of marketing; viral content for any business; the taste economy; starting brand social from scratch; the funnels guide), walked through and rewritten in our own words with Australian and local-service additions. Transcripts live only in `_private/` (git-ignored) as personal reference; never copy transcript text into the plugin.

`docs/COVERAGE-CHECKLIST.md` lists every topic (381) and where it lives. `python scripts/verify_coverage.py` must pass after any edit.

## Structure
- Knowledge library: `plugins/knowtific-marketing-kit/skills/marketing-coach/references/*.md` (one file per area). Skills point to these with `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/<file>.md`.
- 26 skills (`skills/<name>/SKILL.md`), 3 read-only agents (`agents/`), 4 Python scripts (no dependencies).
- Every client project gets a `marketing/` folder (created by `init`); all skills read it first and save outputs into it.

## Decisions made
- One plugin, many skills + read-only agents. No hooks (too noisy). MCP connections are optional; skills detect them and fall back to asking for exports (see `references/tools.md`, `docs/TOOLS.md`).
- Ad connections: read and suggest; change budgets/pause only when the user explicitly asks; never auto-publish ads.
- Local services: Google Search and GBP often come before Meta for urgent needs; Meta creates demand.
- Compliance built in: Spam Act (incl. DMs), SMS Sender ID Register (from 1 July 2026), AHPRA, TGA, ACL (provable claims, reviews, prices, guarantees), creator disclosure, trade licence numbers, privacy.
- Practitioner opinions (e.g. schedulers hurt reach, calls needed above ~$2,000) are presented as things to test.
- Distribution: private GitHub repo as the marketplace. Sell services built on it (workshop, audits, ads, reporting); possible free lead-magnet audit later.

## Working on this repo
- Skill frontmatter: `name` (matches folder) + `description` (what + when, ≤1024 characters). Keep SKILL.md focused; detail goes in references.
- After changes: run `python scripts/verify_coverage.py`, `claude plugin validate .`, `claude plugin validate ./plugins/knowtific-marketing-kit`, then bump `version` in `plugins/knowtific-marketing-kit/.claude-plugin/plugin.json`.
- Test scripts:
  - `python plugins/knowtific-marketing-kit/skills/ads-math/scripts/ads_math.py --job-value 2500 --margin 40 --close-rate 25`
  - `python plugins/knowtific-marketing-kit/skills/funnel-build/scripts/funnel_math.py --visitors 1000 --lp-cvr 4 --close-rate 25 --job-value 2500 --margin 40 --scenario lp-cvr=8`
  - `pillar_report.py` and `ad_set_review.py` take CSVs (see their docstrings).
- Rebuild the Claude app skill zip from `skills/marketing-coach` after changing the library.
- Scripts take whole-number percentages and reject decimals like 0.25. "Close rate" means leads → customers everywhere except `funnel_math.py`, where it is booked → customer.
- Compliance facts were last reviewed in October 2026 (`references/australia-compliance.md`); recheck before big launches.
- Next work: `docs/ROADMAP.md`.
- Write in plain, simple English with concrete local examples; the owner prefers simple explanations.
