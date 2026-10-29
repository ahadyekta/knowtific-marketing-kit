---
name: brand-world
description: Maps a client's brand world (characters who can speak for the brand, sets to film at, a 12-month calendar of company, culture and industry events, and the plot: enemies, friends and specials), then finds the holes and turns them into actions. Use for new-client onboarding (it works as a paid workshop), when planning a year of content or campaigns, when the user asks "what should we post about" or "who could be in our content", or before campaign planning.
---

# Brand world map

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` section 9 and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/campaigns.md` section 9 (Australian calendar) first.

## Inputs
- `marketing/brand.md`, `marketing/brand-world.md` (update rather than replace), `marketing/channels.md`.
- Ask the owner, in one grouped message: who could be on camera (and who refuses); staff with skills or personality; customers or partners who post content; places that look good on camera; regular events, trade shows and launches; busy and quiet months; partners and suppliers; main competitors' launch timing.

## Process

1. **Characters.** List everyone who could represent the brand: owner/founder, experts on the team, social person, hired creators, customers who post (suggest checking the customer list with a tool like Outer Signal, or manually: who tags the business, who reviews it), collaborators (suppliers, partner trades, executives with podcasts). Mark each: willing? camera-comfortable? what topics?
2. **Sets.** Evergreen (showroom, clinic, workshop, warehouse, van, office corner) and temporary (job sites, trade show booth the night before, events). Note what's needed to make each look good.
3. **Calendar (12 months).** Three rows per month:
   - Company: launches, new services, anniversaries, the trade show they always attend, portfolio updates; bundle small updates into a couple of bigger "release" moments
   - Culture: seasonal and cultural moments that matter to their customers (EOFY, school holidays, footy finals, Christmas, weather seasons)
   - Industry: trade shows, regulation changes, rebates, competitor launches, and whether to launch with, before, after, or away from them
4. **Plot.** For each major moment: which characters, which set, what story. Enemies (competitor moves and our response), friends (partners and creators to plug into; what are they planning?), specials (own events, a social series, a giveaway for quiet months).
5. **Holes.** List the gaps and the action for each:
   - Nobody on camera → hire a creator / train a team member / faceless formats
   - No good sets → build one corner, hire a studio monthly, film on job sites
   - Empty months → invent a special
   - No partners → list 5 co-promotion candidates
6. **Rhythm.** Set a monthly or quarterly review of the map.

## Output
Update `marketing/brand-world.md` with the four areas, the 12-month calendar table and the holes/actions list. In chat, give the top 3 holes and suggested next steps (`content-ideas`, `campaign-plan` for the next big moment, `creator-brief` if characters are missing).

## Workshop mode
If the user is running this live with a client, offer a simple agenda: 10 min goals → 20 min characters and sets → 30 min calendar → 20 min plot → 10 min holes and actions, and a one-page summary to send after. Mention the paid-workshop model (fee credited against a retainer).
