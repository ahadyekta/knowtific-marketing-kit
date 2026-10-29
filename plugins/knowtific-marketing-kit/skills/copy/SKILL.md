---
name: copy
description: Writes or rewrites marketing copy in different styles (direct response, evidence-led, story-driven, culturally savvy) from the client's positioning, proof and customer phrases, including full landing page copy by section, headlines, ads, emails, social captions, bios (3-line formula), GBP descriptions and offers, with a compliance check. Use when the user asks to write, rewrite, tighten or "make this better" for any copy, wants landing page copy, or wants versions to test.
argument-hint: "[what to write, or paste the copy]"
---

# Copy

## Inputs
- `marketing/brand.md` (positioning statement, voice, copy styles, proof), `marketing/insights.md` (exact customer phrases, objections), `marketing/offer.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` section 5 (copy styles). For landing pages also read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md` section 5.
- If writing from scratch with no `marketing/` folder, ask for: who it's for, what they want, the offer, proof, and the CTA.

## Modes

### A. Rewrite or write a piece (default)
Give versions in the styles that fit the brand (default: direct response, evidence-led, story-driven; add culturally savvy only if the brand and audience suit it). For each version: the copy, plus one line on when to use it. Then recommend which to test first.

### B. Landing page copy
Write the full page section by section, in the structure that fits (service page, product page, listicle, luxury; see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md`):
- Hero: 3 headline options, subheadline, 3 benefit bullets, CTA text, trust line
- Each section's copy, in order
- FAQ answering the real objections from insights.md
- Final CTA with response-time promise
- Thank-you page copy and "prepare for your call" page copy
Provide the main version in one style, plus alternative heros in the other two styles for testing. If the project is a codebase, offer to put the copy into the page component.

### C. Short-form set
For a campaign or offer: 10 headlines, 5 primary texts, 5 Google Ads headlines (≤30 characters) and 4 descriptions (≤90 characters), 3 email subject lines, 3 captions, a 3-line bio (what we do / why follow / CTA), a GBP description (≤750 characters).

## Rules
1. **Specific beats clever.** Use real numbers, places, timeframes and customer words.
2. **Benefits from the customer's view**, then features as proof.
3. **One idea per piece**, one CTA.
4. **Never invent** proof, statistics, reviews, awards or guarantees. Use placeholders like `[review count]` when data is missing.
5. **Add the human layer.** Ask for a real story or detail if the copy feels generic.
6. **Compliance check** before finishing, using `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`: provable claims, price display, health rules (no clinical testimonials or outcome guarantees for AHPRA professions; TGA for therapeutic goods), genuine urgency, guarantee wording.
7. Australian spelling and plain English.
