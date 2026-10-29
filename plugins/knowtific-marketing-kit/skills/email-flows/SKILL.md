---
name: email-flows
description: Plans and writes a client's email and SMS marketing: the core automated flows (welcome/enquiry, quote follow-up, booking reminders, job complete and review request, rebook, win-back, missed-call text-back; or for e-commerce welcome, abandoned cart, browse abandonment, post-purchase, cross-sell, second purchase), a campaign calendar rotating the eight campaign types, plain-text founder emails, segments, the weekly Monday workflow, and compliance (Spam Act, Sender ID). Use when the user asks about email marketing, SMS, automations, follow-up sequences, newsletters, retention, or "what should we email".
argument-hint: "[flows | calendar | write <email>]"
---

# Email and SMS flows

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/email-and-retention.md` in full, and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md` (Spam Act, Sender ID).

## Inputs
- `marketing/brand.md` (voice), `offer.md`, `insights.md` (objections for FAQ emails), `funnel.md`, `channels.md` (email/SMS/CRM tools), `content-bank.md` (content to reuse), `brand-world.md` (calendar).
- Business type (service or e-commerce), list size, tools (Klaviyo, Kit, Beehiiv, Mailchimp, ServiceM8/Tradify automations, Knowtific follow-up engine).
- If the Klaviyo MCP is connected, read current flows and performance first.

## Mode 1: Flows (default)
1. List the flows the business needs (service or e-commerce set) and which already exist.
2. For each flow: trigger, filters/exit conditions (stop on reply, booking or purchase), timing, channel (SMS if we have a number and consent, else email), and the full copy for each message (subject line + preview text for email; ≤160 characters for SMS where possible).
3. Include a founder plain-text email in the welcome/enquiry flow and the post-purchase/job-complete flow.
4. Note segment branches where they matter (e.g. service type, suburb, customer vs lead).
5. Implementation notes for the client's tool (or for Knowtific's follow-up engine: Workers/D1/Workflows trigger and stop conditions).

## Mode 2: Campaign calendar
1. Cadence (default 1/week; 1–3/week for e-commerce).
2. A 4–8 week calendar rotating the eight types (shop the content, new release, from the community, business update, better together, curation/history, FAQ, deals), tied to the brand world calendar and recent content.
3. For each send: type, topic, subject line options (2), plain text vs designed, owner, date.
4. The weekly Monday workflow checklist for whoever runs it.

## Mode 3: Write an email
Write the email in the brand voice: 2–3 subject lines, preview text, body (plain text from a person by default for service businesses; or a simple 2–3 card layout for designed emails), one CTA, P.S. if useful.

## Output
Save to `marketing/email/flows.md` and/or `marketing/email/calendar.md` (create the folder if needed). Summarise the priority flows in chat.

## Rules
- Consent, sender identification and unsubscribe/STOP in every marketing message.
- Branded SMS sender names must be registered (Sender ID register); or send from a mobile number.
- Don't only send deals; mix types.
- Health clients: no testimonials about clinical outcomes; reminders and education are fine.
- Never invent reviews or results.
