# Knowtific Marketing Kit

A Claude Code plugin marketplace with one plugin, **knowtific-marketing-kit**: a complete marketing toolkit you add to any client project. It answers marketing questions using the client's own context, audits everything, and helps with positioning, rebrands, redesigns, content, campaigns, ads, funnels, landing pages, email/SMS, sales support, SEO and reporting, with Australian compliance built in.

## What's inside (v0.2.1)

**Always on**
| Skill | What it does |
|---|---|
| `marketing-coach` | Answers any marketing question from the knowledge library and the project's `marketing/` folder. Triggers by itself |

**Commands** (type `/knowtific-marketing-kit:<name>`)
| Area | Command | What it does |
|---|---|---|
| Setup | `init` | Reads the project, interviews you, creates the `marketing/` folder |
| Setup | `audit [url]` | Full audit across 14 areas, scorecard, top fixes, 30/60/90-day plan |
| Brand | `position` | Generic-claims check, shelf/elevator tests, positioning options, the one-sentence statement |
| Brand | `rebrand` | Refresh vs repositioning vs full rebrand, brand equity, name checks, voice, rollout that protects SEO |
| Brand | `design-brief` | Visual direction, mood board brief, colour/type/photography, page structure, design tokens for Next.js |
| Brand | `brand-world` | Characters, sets, 12-month calendar, plot, holes and actions (works as a paid workshop) |
| Brand | `customer-insights` | Mines reviews, calls, comments for insights, objections, phrases, buyer type |
| Brand | `copy` | Copy in direct response / evidence-led / story / culturally savvy styles; full landing page copy; ads and bios |
| Content | `content-ideas` | Ideas from 4 types × 2 formats × 12 angles × funnel stages, specific to the client |
| Content | `script` | Hook (text/visual/spoken), script, shot list, caption, CTA versions; carousels; YouTube; filming-day batches |
| Content | `social-plan` | Platform, approach, pillars, cadence, account audit, monthly pillar review (`pillar_report.py`) |
| Campaigns | `campaign-plan` | Insight/concept, channels, tease → unveil → launch → extend → ads → wave 2, shot list, asset list with work-back |
| Campaigns | `creator-brief` | Creator sourcing (incl. AU marketplaces), outreach, modular brief, agreement checklist, tracker, whitelisting |
| Campaigns | `partnerships` | Partners and collaborations, events with ROI goals, retail and reseller programs |
| Ads | `ads-math` | Affordable cost per lead/customer, test budgets, verdicts (`ads_math.py`) |
| Ads | `ad-concepts` | Concepts across the full ad checklist with hooks, copy, variants and briefs |
| Ads | `ads-plan` | Meta and Google structure, tracking prerequisites, 4-week tests, weekly review (`ad_set_review.py`) |
| Conversion | `funnel-build` | Offer, funnel type, lead magnet, pages, follow-up, close assets, numbers model (`funnel_math.py`) |
| Conversion | `lp-review [route]` | Scored landing page review with file/line fixes and rewrites |
| Conversion | `email-flows` | Service and e-commerce flows, campaign calendar, founder emails, SMS compliance |
| Conversion | `sales-kit` | Collateral by stage, touch cadence, scripts, call-notes objection review |
| Conversion | `outbound` | Cold email/LinkedIn for clients or Knowtific's own prospecting, with Spam Act rules |
| Search | `seo-plan` | Keyword research (DataForSEO if connected), page plan, Google Business Profile, local SEO, AI answers |
| Narrative | `crisis` | Bad review or backlash: options, reaction role-play, drafted replies |
| Narrative | `weekly-report` | Weekly wins/next/blockers/stats email, monthly report, team roll-ups |

**Agents** (used by the skills): `landing-page-reviewer`, `site-auditor`, `market-researcher`.

**Knowledge library** (`skills/marketing-coach/references/`): foundations and glossary, positioning and brand, content and social, campaigns, creators, ads, funnels and offers, email and retention, sales and outbound, SEO, partners/events/retail, PR and narrative, insights and research, Australian compliance, client questions, tools.

## Install from GitHub (the "registry")

1. Push this folder to a GitHub repo, e.g. `knowtific/knowtific-marketing-kit` (private is fine; Claude Code uses your normal git/GitHub login).
2. In Claude Code, once per machine:
   ```
   /plugin marketplace add knowtific/knowtific-marketing-kit
   /plugin install knowtific-marketing-kit@knowtific
   ```
3. In any project: run `/knowtific-marketing-kit:init` (or `:audit`), or just ask a marketing question.

### Auto-enable it in a client project
Add to the project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "knowtific": {
      "source": { "source": "github", "repo": "knowtific/knowtific-marketing-kit" }
    }
  },
  "enabledPlugins": {
    "knowtific-marketing-kit@knowtific": true
  }
}
```

### Try it locally without GitHub
```
claude --plugin-dir ./plugins/knowtific-marketing-kit
```
or `/plugin marketplace add C:\Users\Ahad\projects\knowtific-marketing-kit` from Claude Code.

## Optional connections

The kit works without any connections (it asks for exports instead), but these make it much better: DataForSEO, Google Ads, Google Analytics 4, Meta Ads, Klaviyo, Search Console, PageSpeed Insights, a browser (Playwright). Setup steps: **[docs/TOOLS.md](docs/TOOLS.md)**.

## Scripts (Python 3, no extra packages)
| Script | Use |
|---|---|
| `skills/ads-math/scripts/ads_math.py` | Ad economics and verdicts |
| `skills/ads-plan/scripts/ad_set_review.py` | Kill/keep/scale rules on an Ads Manager export |
| `skills/funnel-build/scripts/funnel_math.py` | Funnel model and what-if scenarios |
| `skills/social-plan/scripts/pillar_report.py` | Monthly pillar comparison |
On Windows use `python` or `py` if `python3` isn't found.

## Updating
1. Edit the skills or references.
2. Run `python scripts/verify_coverage.py` (checks every topic in `docs/COVERAGE-CHECKLIST.md` is still covered).
3. Run `claude plugin validate .` and `claude plugin validate ./plugins/knowtific-marketing-kit`.
4. Bump `version` in `plugins/knowtific-marketing-kit/.claude-plugin/plugin.json` (installed copies stay on the old version until it changes).
5. Commit and push. On each machine: `/plugin marketplace update knowtific`.

## Claude app (web, desktop, phone)
Plugins run in Claude Code. For the Claude app, zip `plugins/knowtific-marketing-kit/skills/marketing-coach` (it includes the whole knowledge library) and upload it under Customize > Skills. Re-upload after changes; skills don't sync.

## Layout
```
.claude-plugin/marketplace.json          ← the registry catalogue
plugins/knowtific-marketing-kit/
  .claude-plugin/plugin.json
  agents/                                ← landing-page-reviewer, site-auditor, market-researcher
  skills/
    marketing-coach/  SKILL.md + references/ (the knowledge library)
    init/             SKILL.md + templates/ (marketing/ folder files)
    audit/            SKILL.md + references/audit-rubric.md
    ...one folder per command (see table above)
docs/
  COVERAGE-CHECKLIST.md                  ← every topic and where it lives
  TOOLS.md                               ← optional connections setup
  ROADMAP.md
scripts/verify_coverage.py
CLAUDE.md                                ← context for working on this repo
```

## Notes
- Frameworks are rewritten in Knowtific's own words with Australian examples. Course transcripts live only in `_private/` (git-ignored) as personal reference.
- Some tips are one practitioner's observations (e.g. "schedulers hurt reach"); the kit presents them as things to test.
- Compliance notes are practical flags, not legal advice.
