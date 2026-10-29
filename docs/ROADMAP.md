# Roadmap

## v0.1 (done)
- [x] marketing-coach, init, position, ads-math, lp-review, landing-page-reviewer agent

## v0.2 (done)
- [x] Knowledge library split into 16 topic files; all 381 topics from 7 source videos covered (`docs/COVERAGE-CHECKLIST.md`, `scripts/verify_coverage.py`)
- [x] Brand: audit, position (upgraded), rebrand, design-brief, brand-world, customer-insights, copy (incl. landing page copy)
- [x] Content: content-ideas, script, social-plan (+ pillar_report.py)
- [x] Campaigns: campaign-plan, creator-brief, partnerships
- [x] Ads: ads-math, ad-concepts, ads-plan (+ ad_set_review.py)
- [x] Conversion: funnel-build (+ funnel_math.py), lp-review (upgraded), email-flows, sales-kit, outbound
- [x] Search: seo-plan (DataForSEO-aware)
- [x] Narrative: crisis, weekly-report
- [x] Agents: site-auditor, market-researcher
- [x] Optional connections guide (docs/TOOLS.md)

## v0.2.1 (done): independent review fixes
- [x] Scripts: kill rule matches the source (3 sales at 5× target = keep testing), decimal-percentage guard, Google Ads and UTF-16 exports, "A$" amounts, ROAS minimum spend, pillar report fixes, funnel spend/cpc scenarios
- [x] Compliance updated: Sender ID relabelling and entity associates, BPC replaces VBA, health providers and the Privacy Act, single total price, Google review policy (no incentives or gating), Do Not Call Register
- [x] Referral programs, home page structure, consistent buyer types and AU budgets, full reference paths everywhere

## Next
- [ ] Try the kit on 2–3 real client projects (start with Square Flooring) and fix whatever feels clunky
- [ ] Add example `marketing/` folders (a tradie and a clinic) for reference
- [ ] Skill evals (`claude plugin eval`) for the most-used skills: audit, lp-review, content-ideas, ads-plan
- [ ] Scheduled weekly report agent using GA4 + ads connections
- [ ] Design system skill: turn `marketing/design/tokens.json` into Tailwind/shadcn theme automatically
- [ ] userConfig for agency name, country and default currency, so the kit can be shared publicly

## Public (later)
- [ ] Free lead magnet: "free website and marketing audit for tradies" on Cloudflare, powered by the audit rubric
- [ ] Optional open-source version for developers

## Related product idea
Follow-up engine for tradies on Cloudflare (Workers, D1, Workflows, Email Service, AU SMS provider): instant lead reply, missed-call text-back, quote follow-ups that stop on reply, simple phone-friendly pipeline, weekly report. Positioned against GoHighLevel: simple, reliable, set up for you, AU compliance handled, works alongside ServiceM8/Tradify.
