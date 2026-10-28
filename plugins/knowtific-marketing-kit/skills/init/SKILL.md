---
name: init
description: Sets up a marketing/ folder in the current client project (brand, economics, funnel, brand world, content plan) by interviewing the user and filling templates. Use when starting marketing work for a new client, when the user says "set up marketing for this project", or when another knowtific-marketing-kit skill finds no marketing/ folder.
---

# Set up the client's marketing folder

The `marketing/` folder is the single source of truth every other knowtific-marketing-kit skill reads. Keep it short and factual.

## Steps

1. **Check what exists.** If `marketing/` already exists, read it and only fill gaps. Never overwrite filled-in content without asking.
2. **Gather what you can without asking.** Read the project for clues: site copy, `package.json` name, README, existing pages, service lists, contact details, reviews embedded in the site. Note what you found.
3. **Interview briefly.** Ask the user only for what you couldn't find, in one grouped message, using the priority questions below. If the user doesn't know something, write `TODO:` with the question so it's visible later.
4. **Create the files** from `templates/` (copy each template, then fill it in):
   - `marketing/brand.md`
   - `marketing/economics.md`
   - `marketing/funnel.md`
   - `marketing/brand-world.md`
   - `marketing/content-plan.md`
5. **Summarise** in 3–5 lines: what's filled, the most important gaps, and the next command to run (usually `/knowtific-marketing-kit:position` if positioning is weak, or `/knowtific-marketing-kit:ads-math` if ads are planned).

## Priority questions (ask these first)

1. What does the business do, where, and for whom?
2. Top 1–3 services to promote, average job value, and rough gross margin
3. Close rate (enquiries → paying jobs), or quote acceptance rate
4. Top 3 competitors and what makes this business different
5. Proof available: review count/rating, photos, case studies, licences
6. Current lead sources, current ad spend and CPL if any
7. Industry type (trade, registered health, other) for compliance flags

For a deeper interview, use the question bank at `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/client-questions.md`.

## Rules

- Write in plain English. Bullet points, not essays.
- Record numbers as the user gave them; mark estimates as `(estimate)`.
- If the client is a registered health profession, add the AHPRA note in `brand.md` under Compliance.
- Suggest adding `marketing/` to git so the context travels with the project.
