---
name: lp-review
description: Reviews a landing page or service page in this codebase (Next.js/React or static HTML) for conversion: message, structure, proof, CTA, forms, thank-you page, tracking, speed, mobile and Australian compliance, and returns a scored report with prioritised fixes. Use when the user builds or edits a landing page, asks "check this page", or before launching ads to a page.
argument-hint: "[route or file path, optional]"
---

# Landing page review

## 1. Find the page
- If the user gave a route or file (`$ARGUMENTS`), use it.
- Otherwise find likely landing pages: in Next.js look under `app/**/page.tsx|jsx` or `pages/**`; otherwise `*.html`. Prefer routes named like `lp`, `landing`, `quote`, `book`, or service names. If several match, list them and ask which one.
- Read the page file and every component it renders (follow imports), so you review the actual copy and markup, not just the shell.

## 2. Load context
- `marketing/brand.md` (positioning, proof, objections, compliance) and `marketing/funnel.md` (where traffic comes from) if they exist.
- If the user said which ad or keyword sends traffic here, keep that text handy for the message-match check.

## 3. Review
Delegate the detailed audit to the `landing-page-reviewer` agent when available, passing the file paths and any context. Otherwise work through `references/checklist.md` yourself. Use the checklist either way as the scoring rubric.

If a dev server is running or the user gives a URL, you may also check the rendered page (mobile width, load, form behaviour). Otherwise review from code and say so.

## 4. Report
Use this format:

```
## Landing page review: <route>
Score: <total>/100  (Message __/25 · Structure __/20 · Proof __/15 · Conversion __/20 · Technical __/15 · Compliance __/5)

### Fix first (highest impact)
1. <issue> → <specific fix> (file:line)
2. ...

### Then
- ...

### Already good
- ...

### Rewrites
- Headline options (3): ...
- CTA button text options (3): ...
```

Rules for the report:
- Every issue gets a concrete fix and a file/line reference where possible.
- Rank by expected impact on conversion, not by checklist order.
- Rewrites must use the client's positioning and real proof from `brand.md`. Never invent reviews, numbers or claims.
- Flag compliance problems clearly, even if the score is otherwise high.

## 5. Offer next steps
Offer to apply the top fixes directly in the code. Make changes only after the user agrees.
