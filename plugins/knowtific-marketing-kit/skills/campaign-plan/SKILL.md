---
name: campaign-plan
description: Plans a full marketing campaign or launch (new service, product, feature, seasonal or theme campaign, rebrand launch): the insight or concept, core/extensions/customers/merchandising channels, the six content phases (tease, unveil, launch, extend, performance ads checklist, sustain and wave-2 refresh) with 15–22 organic assets, a shot list for one shoot day, creator and partner roles, events, crossover reuse, an internal × external grid, and an asset list with owners and work-back dates. Use when the user says launch, campaign, Black Friday, EOFY, seasonal push, new service announcement, or "how do we make a big moment".
argument-hint: "[what's launching and when]"
---

# Campaign plan

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/campaigns.md` in full, and skim `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/creators.md` and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/partners-events-retail.md`.

## Inputs
- What's launching, the launch date, the goal (leads, sales, bookings, awareness), budget range.
- `marketing/brand.md`, `insights.md`, `offer.md`, `brand-world.md` (characters, sets, friends, calendar), `economics.md`.
- Ask in one message for anything missing: launch date, budget, who's on camera, partners/retailers, existing customer list size, whether ads will run.

## Process
1. **Position the campaign.** One sentence: the idea and why customers will care.
2. **Insight and/or concept.** Write 2–3 options (insight-led, concept-led, both), each with a campaign name, the core message, the visual world, and why it suits this audience. Recommend one. Check it's **easy for creators and partners to join**.
3. **Channels.** List what's available in each area: core, extensions (retailers, partners), existing customers (early access, VIP emails, customer pricing, invitation to post), merchandising (shopfront, vehicles, displays, signage, packaging).
4. **Six phases with assets.** Plan 15–22 organic pieces (fewer for small businesses, keeping all phases):
   - Tease (1–2, low stakes)
   - Unveil (1–3; walkthroughs that will live on the product/service page)
   - Launch (hero asset + recuts, carousels from stills, a meme or share-friendly carousel)
   - Extend (tutorials, unboxing or "what's included", FAQ answers, behind the scenes)
   - Performance (the ads checklist: problem–solution, founder story, selfish desire, reply-to-comment, magazine editorial, testimonial/UGC (not clinical for health), static, category comparison), with ad variants per winning organic post
   - Sustain and refresh: wave 2 (date, second concept or insight, creator wave 2), responding to top comments
5. **Shoot plan.** One shoot day → a shot list producing the assets above (location, set, character, shot type, which asset it feeds). Use `script` for scripts.
6. **The world.** Creators (anchor? micro?), seeding or experience invites, partners and resellers (content folder, collab posts, regional spend), events (VIP preview, launch at a trade show, local meetup), email/SMS to the list, giveaways, PR/podcasts if relevant, enabled moments (what will people film and share?).
7. **Grid.** Fill the internal × external grid per stage.
8. **Asset list with work-back.** Every asset: phase, channel, owner, draft date, review date, publish date. Work back from launch day.
9. **Budget and measurement.** Ad budget and test plan (link to `ads-math`), KPIs per phase (views and shares for tease/launch; leads, bookings, sales, cost per result for performance), and the review dates.
10. **Next campaign.** Suggest what follows this one, so campaigns run back to back.

## Output
Save `marketing/campaigns/<campaign-name>.md` using `templates/campaign-plan.md`. In chat, summarise the concept, the phase plan in one table, and the first three actions with owners.

## Rules
- Scale to the business: a sole trader still gets all phases, with smaller numbers.
- Real offers only; urgency must be genuine.
- Health and therapeutic goods rules for any testimonial or claim.
- Plan the content before the shoot; never "we'll film and figure it out".
