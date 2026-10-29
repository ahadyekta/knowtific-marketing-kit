---
name: init
description: Sets up the marketing/ folder in the current client project (brand, insights, offer, economics, funnel, channels, brand world, content plan, content bank, plus folders for campaigns, briefs, ads, reports, audits, SEO and design) by reading the project and interviewing the user. Use when starting marketing work for a new client, when the user says "set up marketing for this project", or when another knowtific-marketing-kit skill finds no marketing/ folder.
---

# Set up the client's marketing folder

The `marketing/` folder is the client's "brand project": the single source of truth every other skill reads. Keep it short, factual and current.

## Folder layout

```
marketing/
  brand.md          positioning statement, customer, services, proof, voice, compliance
  insights.md       customer insights compendium, objections, buyer type
  offer.md          offers, lead magnets, guarantees, pricing signals
  economics.md      job value, margin, close rate, targets, current results
  funnel.md         traffic sources, pages, lead capture, follow-up, tracking, leaks
  channels.md       accounts, tools, access, connections (what's set up and who owns it)
  brand-world.md    characters, sets, calendar, plot, holes
  content-plan.md   platform, approach, pillars, cadence, monthly results
  content-bank.md   idea backlog and what worked
  campaigns/        one file per campaign plan (and partnership plans)
  briefs/           creator, design and ad briefs; creator tracker
  ads/              ads plan, concepts, test log (log.md) and weekly reviews
  email/            flows and campaign calendar
  sales/            sales kit, follow-up cadence, outbound plans
  reports/          weekly and monthly reports
  audits/           audits and reviews
  seo/              keyword plans and page plans
  design/           design briefs and brand tokens
```

## Steps

1. **Check what exists.** If `marketing/` exists, read it and only fill gaps. Never overwrite filled-in content without asking.
2. **Gather what you can without asking.** Read the project: site copy, page titles, service lists, contact details, footer (ABN, licence numbers), testimonials on the site, `package.json`, README, any analytics or pixel code (note what tracking exists). If the user gives the live website URL, you may fetch it. Note what you found and where.
3. **Interview briefly.** Ask only for what you couldn't find, in one grouped message, using the priority questions below. Anything unknown becomes a `TODO:` line with the question.
4. **Create the files** by copying each template from `templates/` and filling it in. Create the empty subfolders with a `.gitkeep`.
5. **Summarise** in 3–6 lines: what's filled, the biggest gaps, and the next command (usually `/knowtific-marketing-kit:audit` for an existing business, `/knowtific-marketing-kit:position` if positioning is weak, `/knowtific-marketing-kit:ads-math` if ads are planned).

## Priority questions

1. What does the business do, where, and for whom?
2. Top 1–3 services or products to promote, average job/order value, rough gross margin
3. Close rate (enquiries → paying jobs) or quote acceptance rate
4. Top 3 competitors and what makes this business different
5. Proof: review count and rating, photos, case studies, licences, years, jobs done
6. Current lead sources, ad spend and cost per lead if any
7. Industry type (trade, registered health, other service, e-commerce, B2B) for compliance flags
8. Who could be on camera, and where could you film?

For a deeper interview use `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/client-questions.md`.

## Rules

- Plain English, bullet points, no essays.
- Record numbers as given; mark estimates `(estimate)`.
- Registered health profession → add the AHPRA note under Compliance in `brand.md`.
- Never invent reviews, numbers or credentials.
- Suggest committing `marketing/` to git so the context travels with the project.
