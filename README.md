# Knowtific Marketing Kit

A Claude Code plugin marketplace with one plugin, **knowtific-marketing-kit**: marketing know-how you can add to any client project. It answers marketing questions using the client's own context, sets up a `marketing/` folder, finds positioning, works out ad budgets, and reviews landing pages in the codebase.

## What's inside (v0.1)

| Command / agent | What it does |
|---|---|
| `marketing-coach` (auto) | Answers marketing questions using the frameworks and the project's `marketing/` folder. Triggers on its own when you ask a marketing question |
| `/knowtific-marketing-kit:init` | Interviews you and creates `marketing/` (brand, economics, funnel, brand world, content plan) |
| `/knowtific-marketing-kit:position` | Generic-claims check, 2–3 positioning options, one-sentence statement |
| `/knowtific-marketing-kit:ads-math` | Affordable cost per lead, test budget, feasibility, scale/kill verdict (Python script) |
| `/knowtific-marketing-kit:lp-review [route]` | Scored landing page review with file/line fixes |
| `landing-page-reviewer` (agent) | Read-only auditor used by `lp-review` |

## Install from GitHub (the "registry")

1. Push this folder to a GitHub repo, e.g. `knowtific/knowtific-marketing-kit` (private is fine; Claude Code uses your normal git/GitHub login to fetch it).
2. In Claude Code, once per machine:
   ```
   /plugin marketplace add knowtific/knowtific-marketing-kit
   /plugin install knowtific-marketing-kit@knowtific
   ```
3. Use it in any project: `/knowtific-marketing-kit:init`, or just ask a marketing question.

### Auto-enable it in a client project
Add this to the project's `.claude/settings.json` so anyone opening the project in Claude Code is offered the plugin:

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

## Updating
1. Edit the skills, then bump `version` in `plugins/knowtific-marketing-kit/.claude-plugin/plugin.json` (users stay on the old version until it changes).
2. Run `claude plugin validate .` and `claude plugin validate ./plugins/knowtific-marketing-kit`.
3. Commit and push. On each machine: `/plugin marketplace update knowtific`.

## Claude app (web, desktop, phone)
Plugins run in Claude Code. For the Claude app, zip `plugins/knowtific-marketing-kit/skills/marketing-coach` and upload it under Customize > Skills. Skills don't sync between Claude Code and the app, so re-upload after changes.

## Layout
```
.claude-plugin/marketplace.json        ← the registry catalogue
plugins/knowtific-marketing-kit/
  .claude-plugin/plugin.json
  agents/landing-page-reviewer.md
  skills/
    marketing-coach/  (SKILL.md + references/)
    init/             (SKILL.md + templates/)
    position/
    ads-math/         (SKILL.md + scripts/ads_math.py)
    lp-review/        (SKILL.md + references/checklist.md)
docs/ROADMAP.md
CLAUDE.md                              ← context for working on this repo in Claude Code
```

## Notes
- Frameworks are written in Knowtific's own words. Don't paste third-party course content into the repo (`_private/` is git-ignored for personal notes).
- Compliance notes are practical flags, not legal advice.
