---
name: creator-brief
description: Plans and runs creator and influencer work for a client: which use (ads/UGC, seeding, affiliates, face of the account), the pyramid, where to find creators (customers first, Australian marketplaces, manual local search), vetting, outreach messages, the modular brief, the agreement checklist (raw files, ad code, usage rights), seeding tracker, whitelisting steps and disclosure rules. Use when the user wants creators, influencers, UGC, a brief for a creator, designer or videographer, an outreach message, or a creator program.
argument-hint: "[goal or campaign]"
---

# Creator brief and program

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/creators.md` in full.

## Inputs
- `marketing/brand.md`, `insights.md`, `offer.md`; campaign file in `marketing/campaigns/` if this is for a campaign.
- Budget, goal, location (local creators needed on site?), product cost (for seeding), whether ads will run.

## Process
1. **Choose the use(s):** ads/UGC (creative diversity), seeding/experience, affiliate/referral, face of the account or a separate account, or collaborator pillar. Explain why for this client.
2. **Shape the pyramid** for the budget (e.g. 3–5 local micro creators + 1 mid-tier; or 10 UGC creators for ads).
3. **Sourcing plan:** start with customers (list tools or manual: who tags/reviews), then marketplaces (Collabstr filtered by city, Influee, JoinBrands, The Right Fit, Fiverr/Upwork), platform search terms and hashtags to use, local groups. Vetting checklist: real comments, posting frequency, past brand work, on-camera quality, audience location (for influencers).
4. **Outreach messages:** a short DM and an email version, personalised, clear on what's offered, no pressure. Seeding version ("no obligation to post").
5. **The brief** using `templates/brief.md` (modular: drop starred items for experienced creators).
6. **Agreement checklist** using `templates/agreement-checklist.md`.
7. **Tracker:** a table (or CSV) for the seeding/creator CRM: name, handle, platform, followers, location, contact, sent/date, posted (Y/N), link, views, cost, ad code, usage expiry, next step.
8. **Whitelisting steps:** how the creator generates the partnership ad code and how to add it in Ads Manager (or Spark Ads on TikTok).
9. **Disclosure and compliance** notes for this client (AANA/ACCC disclosure, AHPRA for health practitioners, TGA for therapeutic goods).

## Output
Save the brief to `marketing/briefs/<creator-or-campaign>.md` and the tracker to `marketing/briefs/creator-tracker.md` (or `.csv`). In chat, summarise the plan, the outreach message, and the first 10 search terms to find creators.

## Also works for designers and videographers
Use the same modular brief with: deliverables, formats and sizes, brand tokens (`marketing/design/`), references, shot list, deadline and review rounds.
