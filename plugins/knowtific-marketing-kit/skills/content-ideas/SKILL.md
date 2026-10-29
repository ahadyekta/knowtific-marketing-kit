---
name: content-ideas
description: Generates specific, high-quality social content ideas for a client by combining the four content types (storytelling, ratings and rankings, breakdowns, scenarios), two formats (carousel, video), the twelve angles for "boring" businesses (format shakeup, speed, viral vehicle, skill showcase, exciting scenarios, strong takes, current events, dumb questions, versus, lore and depth, one interesting element, tour guide) and the content funnel, using the client's real characters, sets, insights and calendar. Use when the user asks for post ideas, a content calendar, "what should we post", ideas for a boring industry, or a month of content.
argument-hint: "[number of ideas, platform, or topic focus]"
---

# Content ideas

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/content-and-social.md` (sections 4–7) first.

## Inputs
- `marketing/brand.md`, `insights.md` (objections, phrases, questions), `brand-world.md` (characters, sets, calendar), `content-plan.md` (pillars and what works), `content-bank.md` (avoid repeats; reuse winning hooks).
- What's happening now: upcoming calendar moments; for current-events angles, use WebSearch for recent news or trends in the niche and region (note the date).
- If no marketing folder: ask what the business sells, who buys, who can be on camera, and any constraints (faceless, health rules).

## Process
1. **Decide the perspective**: expert or student, and who's on camera (or faceless: carousels, hands-only POV, voiceover).
2. **Generate ideas across the grid.** Default: 20 ideas unless asked otherwise. Spread them across:
   - 4 types × 2 formats
   - At least 8 of the 12 angles
   - Funnel stages: about 40% top (attention), 40% middle (trust/education), 20% bottom (the ask), adjusted if the account has no traction yet (then skip hard CTAs)
   - Pillars in `content-plan.md` (if they exist)
3. **Make each idea specific to this client**: real services, suburbs, customers' words, the actual set and character. "Rating 5 hot water systems as a plumber of 20 years, filmed in the van" beats "product review".
4. **Shareability check**: why would someone send this to a friend? Drop ideas with no answer.
5. **Compliance check** (health claims, testimonials, competitor claims, current events sensitivity).

## Output
A table:

| # | Idea (title) | Type | Format | Angle | Funnel | Hook (text / visual / spoken) | Character + set | Why it'll be shared |
|---|---|---|---|---|---|---|---|---|

Then:
- **Top 5 to make first**, and why
- **A 4-week starter calendar** if asked (respecting the cadence in `content-plan.md`; default 4–6 posts/week from 2–3 type×format combos)
- Offer to script the top ideas with `/knowtific-marketing-kit:script`

Append the ideas to `marketing/content-bank.md` (Idea backlog) unless the user says not to.

## Quality bar
- No generic ideas ("share a tip", "behind the scenes") without the specific tip or scene.
- At least 3 ideas that a competitor in the same niche probably isn't doing.
- Use real customer questions as hooks where possible.
- For local businesses, include at least 2 "critique/compare" ideas (e.g. rating local examples, what I would have done).
