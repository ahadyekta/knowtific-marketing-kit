---
name: rebrand
description: Runs a complete rebrand for a client, from deciding whether a rebrand is needed (refresh vs repositioning vs full rebrand), through audit, customer insights, positioning, naming checks, voice and messaging, visual identity direction, to a rollout and launch campaign that protects existing brand equity and SEO. Use when a client wants a new look, new name, new positioning, a "fresh start", or when the brand no longer fits who they serve.
---

# Rebrand

A rebrand is a business decision first and a design job second. Work through the stages in order; save everything to `marketing/` so later skills use the new brand.

Read before starting: `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/insights-and-research.md`.

## Stage 0: Do they need a rebrand? (decide the scope)

Ask why now (new services, new audience, growth into premium, merger, bad reputation, dated look, name clash or trademark problem, owner change). Then recommend one:

| Scope | When | Changes |
|---|---|---|
| **Refresh** | Positioning is right, the look is dated or inconsistent | Visual polish, tidy logo, consistent colours/fonts, new photos, website redesign |
| **Repositioning** | The look is OK but the business now serves a different customer or tier, or is generic | Positioning, messaging, offers, website copy and structure; some visual changes |
| **Full rebrand** | Name or identity is a problem (clash, bad reputation, merger, outgrown) | Name, identity, positioning, everything |

Don't over-rebrand: a refresh plus sharper positioning is often enough.

## Stage 1: Audit what exists and what to keep (brand equity)

- Current positioning, messaging, visual identity, website, GBP, social, vehicles, signage, uniforms, quotes/invoices, email signatures.
- **Brand equity to protect:** recognisable colours or symbols, a name customers know, review history, phone number, domain authority and rankings, vehicle wraps people recognise.
- What customers say about the brand today (reviews, comments, calls).
- Run or reuse an `audit` if one exists.

## Stage 2: Insights and buyer

- Run `customer-insights` (reviews, calls, comments, competitors) if `marketing/insights.md` is thin.
- Decide the target buyer and buyer type, and the tier (good/better/best). Everyday services: price-driven or quality/convenience-driven. Premium tiers: cultural omnivore, aspirational overspender, true elite or aspiring (see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` section 7).
- Capture 3–5 strongest insights the new brand should be built on.

## Stage 3: Positioning and offer

- Run the `position` process: generic check, shelf and elevator tests, 2–3 options, the positioning statement, the one word, AI-legibility.
- Update `marketing/offer.md`: the offer statement ("we're a [X] that does [Y] for [Z]"), core offers, guarantee, entry offer.

## Stage 4: Name (only if changing)

- 5–10 name options with the idea behind each.
- Checks for each: say-it-on-the-phone test, spelling, meaning in other languages relevant to the area, domain availability (.com.au), social handles, **ASIC business name and IP Australia trademark search** (tell the user to check or get advice), and **search clash** (does a similar name already dominate Google in the category? You'd end up paying for your own brand name).
- Recommend 1–2 with reasons.

## Stage 5: Voice and messaging

- Tone in three words, with do/don't examples.
- Copy styles to use (direct response, evidence-led, story-driven, culturally savvy).
- Messaging hierarchy: positioning statement → 3 key messages → proof points for each → objection answers.
- New homepage hero, 3-line social bio, GBP description, email signature, elevator line. Use the `copy` skill for variants.
- Brand lore: origin story, "why we do it this way", the craft details worth showing.

## Stage 6: Visual identity direction

- Run `design-brief` for the full visual direction (mood board brief, logo direction, colour, type, photography, components, tokens).
- If a designer will make the logo, produce a designer brief; if Knowtific builds the site, produce design tokens for the Next.js codebase.

## Stage 7: Rollout plan

**Asset inventory and order of replacement:**
1. Website (new design + copy), favicon, social profile images and bios, GBP (name/description/photos; **name changes on GBP must match real-world signage and documents**, or risk suspension)
2. Email signatures, quote and invoice templates, proposals, uniforms
3. Vehicles, signage, printed material (often the slowest and most expensive; schedule it)
4. Directory listings and citations (keep NAP consistent; update everywhere at once)

**Protect SEO and search:**
- Keep the same domain if possible. If the domain must change: map every old URL to its new URL with 301 redirects, keep page content where it ranks, update Search Console (change of address), GBP website link and backlinks you control.
- Keep the phone number.
- For a name change, mention "formerly [old name]" on the website and GBP for 6–12 months.

**Tell customers first:**
- An email or SMS to past customers from the owner, explaining why (in their terms: what's better for them).
- Run the launch as a campaign with `campaign-plan`: tease ("something's changing"), unveil the new look and the story, launch, extend (behind the scenes, the meaning of the new identity), and refresh.

## Output

Save `marketing/design/rebrand-plan.md` with: scope decision, equity to keep, insights, positioning (and update `brand.md`), name decision (if any), voice and messaging, design brief link, rollout checklist with owners and dates, and the launch campaign link. Give the user a short summary and the next step.

## Rules
- Never recommend changing what customers love without a reason.
- Trademark, business name and domain checks: tell the user what to check; don't claim a name is legally clear.
- Health clients: messaging must stay within AHPRA rules.
