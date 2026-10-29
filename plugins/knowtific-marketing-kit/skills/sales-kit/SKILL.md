---
name: sales-kit
description: Builds the sales support system for a lead-based business: collateral by stage (first email, thank-you page, call deck, forwardable after-call pack, case studies, FAQ/objection answers, comparisons, upsell pack at ~90 days), the follow-up touch cadence with a reason for every touch, speed-to-touch targets, DM and phone scripts, lead triage from social, setter/closer roles, and the weekly objection review from call notes. Use when leads aren't closing, quotes go unanswered, the user wants follow-up scripts, sales collateral, objection handling, or to turn call notes into content.
argument-hint: "[kit | cadence | scripts | call-notes]"
---

# Sales kit

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/sales.md` in full, and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md` section 6.

## Inputs
- `marketing/brand.md`, `offer.md`, `insights.md` (objections), `funnel.md` (current follow-up), `economics.md` (close rate), `content-bank.md` (best content to reuse).
- How leads arrive and who responds; current response time; average touches; CRM or job management tool.

## Mode 1: Kit (default)
Produce, by stage:
1. **First response** (within minutes): SMS and email templates; phone opener.
2. **Thank-you page** content (or check the existing one).
3. **Pre-call / pre-quote email**: what to expect, who's coming, 2–3 proof links, prep checklist.
4. **On the call / at the quote**: a short deck or one-pager outline (problem, approach, examples, process, pricing ranges, guarantee, next steps).
5. **After-call pack** designed to be forwarded to a partner or boss: summary of their situation, the recommendation, price, comparison with alternatives, case study, reviews, FAQ, next step.
6. **Case study one-pager** template and 1–2 drafted from real jobs (placeholders where data is missing).
7. **FAQ / objection answers**: the top objections from insights.md with the best answer and the proof for each; format as PDF copy, email blocks and a script for a short owner video.
8. **Upsell pack** for existing clients (~90 days): results summary and next offers.

## Mode 2: Cadence
A follow-up table: touch number, day, channel, message, reason (new content, case study, seasonal moment, availability, answer to a common worry), and when to stop. Default: 6–8 touches over 4–6 weeks, then monthly nurture. Note that some high-ticket sales close around the 11th touch.

## Mode 3: Scripts
Phone (first call, quote follow-up, "just checking in" replaced with a reason), DM (to commenters and engaged followers; to inbound DMs), voicemail, SMS. Natural, short, Australian English.

## Mode 4: Call notes (weekly)
From pasted or exported call notes/transcripts: objections and how often, what made people say yes, questions marketing should answer, suggested FAQ or landing page changes, 3 content ideas, and coaching notes for the salesperson. Update `marketing/insights.md`.

## Triage and roles
- How social comments, DMs and new followers in the service area are passed to sales (channel, owner, response time).
- Roles: owner/closer/setter and who does what; CRM fields to use.
- Suggest working closely with the most motivated salesperson.

## Output
Save to `marketing/sales/sales-kit.md` (create folder). In chat, list the 3 changes most likely to raise the close rate this month.

## Rules
- Real proof only; placeholders where missing.
- Commercial messages need consent and an opt-out; DMs count too.
- Health clients: AHPRA limits on testimonials apply to sales materials used as advertising.
