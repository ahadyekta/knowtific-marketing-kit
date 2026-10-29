---
name: outbound
description: Plans and writes cold outreach (email, LinkedIn, phone, and personalised video or audit-led outreach) for a client or for Knowtific's own client acquisition: ideal customer profile, list building sources and filters, sending setup (separate domains, inboxes, warm-up), personalisation research, 3–5 touch sequences, reply handling, tracking, and Spam Act compliance. Use when the user wants to find clients, do cold email or LinkedIn outreach, write a prospecting sequence, or build a lead list.
argument-hint: "[who to target]"
---

# Outbound

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/sales.md` section 10 and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md` (Spam Act).

## Inputs
- Who's selling and what (the client's offer, or Knowtific's: websites, local SEO, Google Ads, CRM setup, AI automations, follow-up engine).
- Target market, capacity (how many new clients a month), budget for tools.

## Process
1. **ICP.** Industry, size, location, role of the decision-maker, trigger signals (e.g. poor website, few reviews, running ads to a homepage, slow mobile site, hiring, new location).
2. **List building.** Sources: Google Maps (category + suburb), LinkedIn Sales Navigator, industry directories, local business associations, cold email databases (ListKit, Apollo). Filters and how many to start with (e.g. 200). If DataForSEO is connected, Google Maps/business listing data can help build lists.
3. **Sending setup.** Separate sending domain(s) and inboxes (never the main domain), SPF/DKIM/DMARC, warm-up period, daily volume limits, unsubscribe handling, a suppression list.
4. **Personalisation research.** One specific, true observation per prospect (their website, Google Business Profile, a review, a recent post), gathered manually or with the `market-researcher` agent for a small batch.
5. **Offer the value first.** A free mini-audit, a 2-minute screen-recording review, a mock-up of a better hero section, or a specific idea. For Knowtific: "I recorded a 2-minute review of your website on mobile. Want me to send it?"
6. **Sequence.** 3–5 touches over 2–3 weeks across email and LinkedIn (and phone for warm replies): subject lines, first lines with personalisation slots, body (under ~100 words), one clear ask, follow-ups that add something new; stop on reply.
7. **Reply handling.** Templates for interested, not now, wrong person, and unsubscribe.
8. **Tracking.** A simple pipeline: prospects contacted, replies, positive replies, calls booked, won. Targets and what to change if reply rates are low (list, offer, first line).

## Output
Save to `marketing/sales/outbound-<target>.md`. In chat: the ICP, the first-touch email, and the setup checklist.

## Rules (Spam Act, telemarketing and good practice)
- Phone outreach: check numbers against the Do Not Call Register (unless you have consent), call only within the permitted hours (weekdays 9am–8pm, Saturday 9am–5pm, not Sundays or national public holidays), say who you are and the business, and end the call when asked. See `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`.
- Identify the sender (name, business, contact details), include a working unsubscribe, honour it promptly.
- Contact businesses at addresses published for that purpose where the message is relevant to their role; avoid personal emails.
- Don't buy dodgy lists; keep volumes modest; never use deceptive subject lines.
- Get legal advice for large-scale programs.
