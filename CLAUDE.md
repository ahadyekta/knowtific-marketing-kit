# Knowtific Marketing Kit: working notes

This repo is a Claude Code plugin marketplace (`knowtific`) containing one plugin (`knowtific-marketing-kit`). It packages marketing frameworks for Knowtific's client projects so they can be added to any project from GitHub.

## Owner and context
- Ahad, Knowtific (knowtific.com.au, Melbourne): websites, local SEO, Google Ads, CRM setup, AI automations for small businesses, mainly tradies and allied health, open to other industries and Meta/Instagram ads work.
- Stack preference: Next.js/React, Cloudflare (Workers, D1) or Supabase. Avoid anything that needs a server to maintain.
- Goal: get fundamentally strong at improving businesses' marketing, and have a tool that, when added to a project, checks everything, suggests what to do, reviews landing pages, and answers marketing questions from these frameworks.

## How this started
Built from a conversation walking through a long marketing course section by section (types of marketing, positioning, brand world, positioning statement and copy styles, AI levels, organic social, paid ads, outbound, creators, funnel and landing pages, campaigns, PR, email/SMS, sales support, weekly report). The frameworks in `plugins/knowtific-marketing-kit/skills/marketing-coach/references/frameworks.md` are a rewrite in our own words, with Australian notes added. The original transcript, if present, lives in `_private/` (git-ignored) as a personal reference only; never copy it into the plugin.

## Decisions made
- Format: one plugin of several skills + one read-only agent. No hooks yet (too noisy). MCP only later, for live ad/analytics data.
- Every client project gets a `marketing/` folder (brand, economics, funnel, brand-world, content-plan). All skills read it first.
- Local services note: Google Search often comes before Meta for urgent needs; Meta creates demand.
- Compliance flags built in: Spam Act, SMS Sender ID Register (from 1 July 2026), AHPRA (no clinical testimonials), ACL, creator disclosure, trade licence numbers.
- Distribution: private GitHub repo as the marketplace. Don't sell the plugin; sell services built on it (workshop, LP audit, ads setup, reporting). Possible free lead-magnet audit later.

## Working on this repo
- Skill files: `plugins/knowtific-marketing-kit/skills/<n>/SKILL.md`, frontmatter `name` + `description` (description says what and when). Keep SKILL.md short; put detail in `references/`.
- Reference other skills' files with `${CLAUDE_PLUGIN_ROOT}/skills/...`.
- After changes: bump `version` in `plugins/knowtific-marketing-kit/.claude-plugin/plugin.json`, run `claude plugin validate .` and `claude plugin validate ./plugins/knowtific-marketing-kit`.
- Test the calculator: `python plugins/knowtific-marketing-kit/skills/ads-math/scripts/ads_math.py --job-value 2500 --margin 40 --close-rate 25`.
- Next work is listed in `docs/ROADMAP.md` (Phase 2 skills first).
- Write in plain, simple English with concrete local examples; the owner prefers simple explanations.
