---
name: seo-plan
description: Builds an SEO and local search plan for a client: keyword research (using DataForSEO, an SEO suite or Search Console if connected, otherwise manual research), opportunity scoring by volume, difficulty and intent, a page plan (one page per core service and genuine location, with titles, headings, content outline, FAQ, embedded video), Google Business Profile optimisation, reviews, citations and NAP, schema, technical checks, internal links and link building, AI-answer visibility, brand-name clash checks, and pre-launch SEO timing. Use when the user asks about SEO, ranking on Google, Google Business Profile, local search, AI search visibility, or before launching a new site or product.
argument-hint: "[service, location or URL]"
---

# SEO plan

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/seo.md` in full and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/tools.md`.

## 1. Inputs
- `marketing/brand.md` (services, area, positioning), `channels.md`, any `marketing/seo/` files.
- The site (codebase or URL): pages, titles, headings, internal links, schema, sitemap, speed.
- Connections (check which exist): **DataForSEO** (keyword volumes and difficulty, live results, competitor domains, backlinks, Google Business data, AI-mention tools), SEO suites (Ahrefs, Semrush, SE Ranking), **Search Console** (real queries and pages), GA4, PageSpeed Insights.
- If none are connected: say which connection would help (DataForSEO is pay-as-you-go), then continue with Search Console exports, Google Keyword Planner numbers from the user, and WebSearch to inspect current results pages for target terms.

## 2. Keyword research
1. Seed list: each service × (suburbs/region, "near me", intent words: cost, price, best, emergency, same day, reviews, vs).
2. Get volume and difficulty (batch lookups; tell the user roughly how many API calls for large lists).
3. Classify intent: urgent/transactional, commercial investigation, informational.
4. Score opportunities: volume × intent fit ÷ difficulty; flag quick wins (low difficulty, decent volume, high intent) and terms where the client is already ranking positions 4–15.
5. Brand check: does the brand name clash with another business that dominates search?

## 3. Page plan
For each target cluster: URL, page type (service, location, guide, FAQ), title tag (≤60 characters), H1, meta description (≤155), content outline (what it is, who it's for, process, price range, proof, FAQs, CTA), embedded video idea, internal links to/from, schema type. Location pages only where the business genuinely serves the area and has specific content (local jobs, photos, reviews). No thin duplicates.

## 4. Local SEO
- Google Business Profile checklist: primary/secondary categories, services with descriptions, service areas, hours, photos plan (real, monthly), posts, Q&A, products, booking link, UTM on the website link.
- Reviews: the job-complete review request flow (see email-flows) sent to every customer, reply templates. No incentives of any kind and no gating (Google policy); see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`.
- Citations and NAP consistency: priority directories for Australia and the industry.
- Schema: LocalBusiness (specific subtype), Service, FAQ, Review where valid.

## 5. Technical checks
Indexing (Search Console coverage), sitemap and robots, Core Web Vitals on mobile (PageSpeed), title/heading duplicates, broken links and redirects, image optimisation, canonical tags, HTTPS, mobile usability. In a Next.js codebase, check `metadata`/`generateMetadata`, `sitemap.ts`, `robots.ts`, image handling and structured data components, and offer fixes.

## 6. Authority and links
Legitimate link sources: suppliers and partners, local associations, sponsorships, local news stories, industry directories, case studies with clients, guest content, the client's social profiles. No paid link schemes.

## 7. AI answers
Test "best [service] in [area]" style queries in AI tools (and DataForSEO's AI tools if connected); note who's mentioned and why; recommend clarity, FAQs, third-party mentions and review strength.

## 8. Timeline
SEO takes months. Give a 90-day plan (technical fixes and GBP first, then core service pages, then location pages and links) and, for launches, start SEO before the launch.

## Output
Save `marketing/seo/seo-plan-YYYY-MM-DD.md` (keyword table, page plan, GBP checklist, technical fixes, 90-day plan). In chat: the top 5 quick wins.
