---
name: design-brief
description: Creates a visual direction brief for a redesign or new brand identity (mood board brief, logo direction, colour palette, typography, photography and video style, layout and components, page structure, accessibility) grounded in the client's positioning, tier and buyer type, and outputs design tokens ready for a Next.js/Tailwind codebase. Use when redesigning a client website, starting a new site, briefing a designer, or after a rebrand decision.
---

# Design brief

Design follows positioning. A premium designer brand and a value-priced emergency plumber need very different looks. Start from the strategy.

## 1. Inputs
- `marketing/brand.md` (positioning, tier, buyer type, voice), `marketing/insights.md`, `marketing/design/` if present.
- The current site/codebase: existing colours, fonts, components (look for Tailwind config, CSS variables, theme files).
- Ask the owner (if not known): brands they admire in any industry and why; what they dislike; what must stay (brand equity); how customers should feel.
- Optional: use the `market-researcher` agent to capture competitors' visual style so the new design stands apart on the "shelf".

## 2. Strategy summary (top of the brief)
- Positioning statement and the one word
- Tier (good/better/best) and buyer type
- Three feelings the design must create (e.g. "trustworthy, calm, premium")
- How it must differ from competitors (the visual shelf test)
- Brand equity to keep

## 3. Visual direction
Give **2 distinct directions** (unless the user wants one), each with:
- **Name and one-line idea** ("Workshop craft: honest materials, warm timber, close-ups of hands at work")
- **Mood board brief**: 8–12 reference descriptions (types of imagery, textures, layouts, brands to look at), written so a designer or image search can find them. Don't copy any specific brand's identity.
- **Logo direction**: wordmark vs symbol, style, what it should suggest, what to avoid, minimum sizes (van, favicon, embroidery)
- **Colour**: primary, secondary, accent, neutrals, with hex values, usage proportions, and WCAG contrast checks for text/button combinations
- **Typography**: heading and body fonts (Google Fonts or licensed), sizes and weights, why they fit
- **Photography and video**: real people and real work (no stock for trades and clinics), lighting, framing, close-up "craft" shots for premium positioning, before/after rules, the **set** (where the brand films)
- **Graphic elements**: shapes, icons, patterns, how they're used
- **Tone of UI**: corners, shadows, spacing, density, motion

Recommend one direction and say why.

## 4. Website structure
- Page list and purpose (home, each core service, about/team, reviews, FAQ, contact/quote, lead magnet and thank-you pages, location pages only where genuine)
- Home page section order and service page structure (from `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md`, section 5: "Home page (local service business)" and "Type 2: service page")
- Key components: hero, proof bar (rating, licences, years), before/after gallery, review cards, how-it-works steps, FAQ accordion, sticky mobile call/quote bar, quote form, team cards, case study cards
- Mobile first: tap targets, click-to-call, sticky CTA, short forms

## 5. Design tokens (for the build)
Save `marketing/design/tokens.json` and a Tailwind snippet. Example shape:
```json
{
  "color": {"primary": "#...", "primary-foreground": "#...", "accent": "#...", "background": "#...", "foreground": "#...", "muted": "#...", "border": "#..."},
  "font": {"heading": "...", "body": "..."},
  "radius": {"sm": "...", "md": "...", "lg": "..."},
  "shadow": {"card": "..."},
  "spacing": {"section": "..."}
}
```
If the project uses Tailwind/shadcn, map tokens to CSS variables in `globals.css` and the theme config, and offer to apply them. Use the `frontend-design` skill (if available) when building the actual pages.

## 6. Designer handoff (if an external designer makes the logo)
A one-page brief: background, positioning, audience, feelings, direction chosen, must-haves, avoid list, deliverables (logo files in SVG/PNG, colour and mono versions, favicon, social avatars, vehicle and signage versions, a mini style guide), timeline and review rounds.

## Output
Save `marketing/design/design-brief.md` (+ `tokens.json`). Summarise the recommended direction in chat and offer to apply the tokens or build the first page.

## Rules
- Never reproduce another brand's logo, distinctive identity or trademarked elements.
- Check colour contrast for accessibility (aim for WCAG AA: 4.5:1 for body text).
- Real photography beats stock for local service businesses; plan a shoot if needed (see brand-world sets).
