---
name: position
description: Finds positioning for a client business and writes its one-sentence positioning statement, with a generic-claims check, shelf and elevator tests, 2–3 positioning options from the full type list, copy-style recommendations and an AI-legibility check. Use when a client's message feels generic, before writing ads or a landing page for a new client, when the user asks how to make a business stand out, or as the first step of a rebrand.
---

# Find the positioning

## Inputs
1. Read `marketing/brand.md`, `marketing/insights.md` and `marketing/offer.md` if they exist. Read the site's main copy (home, service pages, about) or fetch the live site if given a URL.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` (sections 1–5) before starting.
3. If key facts are missing (customer, top service, competitors, proof), ask in one grouped message. Never invent proof.
4. Optional: if competitors aren't known, use the `market-researcher` agent to pull 3–5 competitors' claims and review themes.

## Process

1. **Generic check.** Quote the current headline/tagline and list every claim any competitor could also make ("quality", "reliable", "friendly", "competitive prices", "family owned" with nothing else).
2. **Shelf test.** Describe the client's "shelf" (Google results, Maps pack, Instagram feed) and how each competitor stands out. Does the client have a reason to be picked?
3. **Elevator test.** Write how the owner currently answers "Oh, like [competitor]?" and whether it's crisp.
4. **Tier.** Is the client playing good, better or best? Does pricing match?
5. **Pick candidate types.** From the full list (performance, category creation/new form, counter-position, smart, value, niche, generational, single attribute, position against, counterculture, name, and the premium types: true performance, lifestyle performance, designer, bespoke, luxury without the markup, lifestyle premium), choose the 2–3 that genuinely fit the client's real strengths. Note whether each needs a real product advantage or can be achieved through marketing. If relevant, add a taste-economy angle (the best / hero ingredient or material / transformation) and the target buyer type.
6. **Write one statement per option:**
   > For [who] who [need], [business] is the [category] that [benefit]. Unlike [alternatives], we [difference].
   Every part specific. The difference must be true today, or something the owner commits to.
7. **For each option add:** a landing page hero headline; a Google Ads headline (≤30 characters); a 3-line Instagram bio; the one word it would own; proof needed and whether they have it; the main risk (too narrow, hard to deliver, easy to copy, compliance).
8. **AI-legible test.** The AI or search query each option would win ("best X for Y in Z"), and whether the current site clearly answers it.
9. **Copy style.** Recommend which styles to test (direct response, evidence-led, story-driven, culturally savvy) and why.
10. **Recommend one**, with the reason and what the business must do or change to own it.

## Output
- A short comparison of options, then the recommendation.
- After the user picks, update `marketing/brand.md` (statement, type, one word, elevator answer, AI query, copy styles, tier). Ask before overwriting.
- Suggest next steps: `copy` to rewrite the homepage hero, `lp-review` for key pages, `rebrand` if the identity no longer fits.

## Rules
- Prefer positioning the business can prove now.
- Health professions: no outcome guarantees or testimonial-based positioning; check `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`.
- "Best/fastest/#1" claims need evidence (consumer law).
- Value (cheapest) is a last resort for established businesses; fine as a short-term entry tactic for new ones.
