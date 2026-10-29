---
name: customer-insights
description: Mines customer evidence (Google and other reviews, competitor reviews, sales call notes, support emails, social comments and DMs, survey answers, search terms) for insights, objections, exact customer phrases, testimonials, buyer type and content ideas, separating what customers say about themselves from what's really driving them, and saves them to marketing/insights.md. Use when positioning or copy feels generic, before a rebrand or campaign, after a batch of sales calls, or when the user pastes reviews, call notes or comments.
---

# Customer insights

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/insights-and-research.md` first.

## 1. Collect evidence
Use what the user provides or can export:
- The client's reviews (Google, Facebook, industry sites). If not provided, ask for an export or paste. If DataForSEO is connected it can pull Google reviews (business data); otherwise use WebFetch only where allowed.
- Competitors' reviews (3–5 competitors). The `market-researcher` agent can gather themes.
- Sales call notes or transcripts (Granola, Fathom exports), support emails, quote follow-up replies.
- Social comments and DMs, ad comments.
- Search terms (Google Ads search terms report, Search Console queries).
- Lost-lead reasons, survey answers ("What nearly stopped you contacting us?").

If there's little evidence, write a short customer interview script (five questions: what was happening when you started looking; what else you considered; what almost stopped you; why us; what you'd tell a friend) and a lost-lead call script, then stop.

## 2. Analyse
1. **Cluster themes**: reasons for choosing, results/feelings, frustrations with alternatives, worries before buying, surprises.
2. **Count** how often each appears.
3. **Pull exact phrases** customers use (gold for copy and ads).
4. **Objections** with the best answer and the proof that settles each.
5. **Said vs real**: for each big theme, is it what people say about themselves, or what's really driving them? Note the evidence either way.
6. **Buyer type**: for everyday services, price-driven or quality/convenience-driven; if the business sells a premium tier, which of the four premium types (cultural omnivore, aspirational overspender, true elite, aspiring) the evidence points to. See `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/positioning-and-brand.md` section 7.
7. **Competitor gaps**: what competitors are praised and criticised for; where the white space is.
8. **Insights**: write 3–7 one-sentence insights with evidence, confidence and how to use each (positioning, offer, content angle, ad hook, campaign concept).
9. **Testimonials**: shortlist the best quotes for the website and ads, noting permissions needed and AHPRA limits for health clients.

## 3. Output
Update `marketing/insights.md` (merge, don't overwrite): insights table, objections table, exact phrases, buyer type, competitor notes. In chat give:
- The 3 strongest insights
- The top 3 objections and answers
- 5 content ideas and 3 ad hooks drawn directly from the evidence

## Rules
- Quote real customers only; never fabricate quotes or counts.
- Treat names and personal details as private; don't put full names in public-facing copy without permission.
- For registered health practitioners, testimonials about clinical outcomes can't be used in advertising (use insights privately to shape messaging instead).
- Weekly mode: if the user pastes this week's call notes, update objections and suggest 3 content pieces and 1 landing page or FAQ change.
