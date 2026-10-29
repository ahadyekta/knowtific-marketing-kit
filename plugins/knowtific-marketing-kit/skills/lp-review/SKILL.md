---
name: lp-review
description: Reviews a landing page, service page, product page, lead magnet page or booking flow in this codebase (Next.js/React or HTML), or at a live URL, for conversion: page type and structure, message match, proof, CTAs, soft CTAs, forms, thank-you and "prepare for your call" pages, tracking, speed, mobile and Australian compliance, and returns a scored report with prioritised file/line fixes and rewrites. Use when the user builds or edits a page, asks "check this page", or before sending ads to a page.
argument-hint: "[route, file path or URL, optional]"
---

# Landing page review

## 1. Find the page
- If the user gave a route, file or URL (`$ARGUMENTS`), use it.
- Otherwise find likely landing pages: in Next.js look under `app/**/page.tsx|jsx` or `pages/**`; otherwise `*.html`. Prefer routes named like `lp`, `landing`, `quote`, `book`, `thank-you`, or service names. If several match, list them and ask which.
- Read the page and every component it renders (follow imports). Also find the thank-you/success route or state and any booking confirmation page.

## 2. Load context
- `marketing/brand.md` (positioning, proof, compliance), `insights.md` (objections), `offer.md`, `funnel.md` (traffic source).
- If the user said which ad, keyword or post sends traffic here, keep it for the message-match check.

## 3. Review
Delegate the detailed audit to the `landing-page-reviewer` agent, passing file paths (or URL) and context. **Always include these two rubric paths in the agent's prompt exactly as written here** (agents may not resolve plugin paths themselves): `${CLAUDE_PLUGIN_ROOT}/skills/lp-review/references/checklist.md` and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md`. Otherwise work through `${CLAUDE_PLUGIN_ROOT}/skills/lp-review/references/checklist.md` yourself. The checklist is the scoring rubric either way.

If a dev server is running, a URL is given, or a browser tool (Playwright MCP, Claude in Chrome) is available, also check the rendered page at mobile width (375px) and desktop: load, layout, sticky CTA, form behaviour and success state. If the PageSpeed Insights API is available, get mobile scores. Otherwise review from code and say what couldn't be checked.

## 4. Report
```
## Landing page review: <route>
Page type: <service / PDP / listicle / luxury / lead magnet / booking>
Score: <total>/100  (Message __/25 · Structure __/20 · Proof __/15 · Conversion __/20 · Technical __/15 · Compliance __/5)

### Red flags
- (if any)

### Fix first (highest impact)
1. <issue> → <specific fix> (file:line)

### Then
- ...

### Already good
- ...

### Rewrites
- Headline options (3): direct response / evidence-led / story
- CTA button text (3)
- Missing section copy (if any)

### Tests to run next
- ...

### Not checked
- ...
```
Rules: concrete fix and file/line for every issue; rank by expected impact on leads; rewrites use real positioning and proof (placeholders if missing); compliance flagged clearly.

Save a copy to `marketing/audits/lp-<route>-YYYY-MM-DD.md`.

## 5. Next steps
Offer to apply the top fixes in the code (only after the user agrees), to write the full page with `copy`, or to model the impact with `funnel_math.py`.
