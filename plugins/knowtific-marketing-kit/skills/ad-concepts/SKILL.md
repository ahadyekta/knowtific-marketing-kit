---
name: ad-concepts
description: Generates paid ad concepts for a client across the full concept checklist (problem–solution, founder story, selfish desire, reply-to-comment, magazine editorial, testimonial/UGC, static, category comparison, offer-led, demonstration, listicle, objection-buster), each with hooks (text, visual, spoken), primary text, headline, format, the audience/ad set it belongs in, variants for creative diversity, and a ready brief for a creator or designer. Use when the user needs new ads, ad ideas, hooks, angles, a creative test plan, or ad copy for Meta, TikTok, YouTube or Google.
argument-hint: "[offer, audience or number of concepts]"
---

# Ad concepts

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/ads.md` sections 3, 7 and 8, and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/creators.md` section 5 (the brief).

## Inputs
- `marketing/brand.md`, `insights.md` (objections, phrases, insights: the best hooks come from here), `offer.md`, `economics.md`, `ads/log.md` (what's already been tested and won).
- Platform(s), offer, audience(s), budget, who can be on camera or which creators are available.
- If results data exists, start from the winners: new hooks and angles on winning concepts, plus one or two new concepts.

## Process
1. **Pick the angle set.** Map 6–10 concepts across the checklist, matched to the audience and funnel stage (cold vs warm vs retargeting).
2. **For each concept write:**
   - Concept name and the insight behind it
   - Ad set it belongs in (audience | creative type), so each ad set tests one idea
   - Format (video, static, carousel, partnership/whitelisted, catalog) and aspect ratios
   - 3 hooks, each with on-screen text, visual and spoken line
   - Primary text (2 versions: one direct response, one evidence-led), headline, CTA button
   - Landing page it sends to (must match the message)
   - Variants for creative diversity (different person, age, setting, voiceover gender/accent)
3. **Google Search (if relevant):** 15 headlines (≤30 characters), 4 descriptions (≤90), sitelink texts, callouts, keyword themes and negatives.
4. **Briefs.** For the top 3 concepts, write a ready brief (creator or designer) using the creator-brief template, or a script via `script`.
5. **Test order.** Which 2–3 concepts to launch first and why, with the budget per ad set and the decision rule.
6. **Compliance check.** Provable claims; special ad categories; AHPRA (no clinical testimonials, no outcome guarantees) and TGA rules; genuine urgency and offers.

## Output
Save to `marketing/ads/concepts-YYYY-MM-DD.md`. In chat: a table of concepts (name, ad set, format, best hook) and the recommended first tests.

## Quality bar
- Each concept is genuinely different (not the same ad with a new colour).
- Hooks use real customer language and real numbers.
- Every concept passes "would I stop scrolling for this?"
- Static concepts include the exact headline text and layout description so a designer (or AI image tool) can mock it up.
