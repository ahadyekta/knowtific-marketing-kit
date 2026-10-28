---
name: position
description: Finds positioning for a client business and writes its one-sentence positioning statement, with 2–3 options and a generic-claims check. Use when a client's message feels generic, before writing ads or a landing page for a new client, or when the user asks how to make a business stand out.
---

# Find the positioning

## Inputs
1. Read `marketing/brand.md` if it exists. Also read the site's main copy (home page, service pages) to see how the business currently describes itself.
2. If key facts are missing (who the customer is, top service, competitors, proof), ask in one short grouped message. Don't invent proof.

## Process

1. **Generic check.** Quote the current headline/tagline and list every claim any competitor could also make ("quality", "reliable", "friendly", "competitive prices", "family owned" with nothing else). Say plainly whether it passes the shelf test.
2. **Pick candidate types.** Read the positioning types table in `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/frameworks.md` (section 2). Choose the 2–3 that genuinely fit this business's real strengths and market. Explain in one line why each fits.
3. **Write one statement per option** using:
   > For [who] who [need], [business] is the [category] that [benefit]. Unlike [alternatives], we [difference].
   Every part must be specific. The difference must be true today or something the owner commits to.
4. **For each option, add:**
   - A headline for the landing page hero
   - A 1-line Google Ads headline (≤30 characters) and an Instagram bio line
   - The proof needed to back it up, and whether the business has it
   - The main risk (too narrow, hard to deliver, easy to copy, compliance)
5. **AI-legible test.** For each option, write the search or AI query it would win ("best X for Y in Z") and whether the current site would clearly answer it.
6. **Recommend one**, with the reason. Note what the business must do or change to own it.

## Output
- Present the options as a short comparison, then the recommendation.
- After the user picks one, update `marketing/brand.md` (Positioning statement, type, one word, voice). Ask before overwriting existing content.

## Rules
- Prefer positioning the business can prove now over aspirational claims.
- For registered health professions, avoid outcome guarantees and testimonial-based positioning (see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`).
- Value (cheapest) positioning is a last resort for established businesses; fine as a short-term entry tactic for new ones.
