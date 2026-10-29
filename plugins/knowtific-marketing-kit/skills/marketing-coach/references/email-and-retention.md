# Email, SMS and retention

## Contents
1. Why email matters
2. Campaigns vs flows
3. Cadence and research
4. Eight campaign types
5. Style: from a person, plain text, simple layouts
6. Core flows (e-commerce and services)
7. Building flows and the weekly workflow
8. Segmentation
9. Tools
10. Retention and customer experience
11. SMS in Australia
12. Referrals and word of mouth

---

## 1. Why email matters

Email and SMS are unglamorous but highly valuable. Marketing automation is a skill that will always find well-paid work, and it's straightforward, especially with AI. It keeps paying off: set up flows once and they sell every day. Your list is a lifetime asset.

## 2. Campaigns vs flows

- **Campaign**: a one-off message sent to many people at once ("Our winter range is here").
- **Flow (automation)**: messages sent automatically when someone does something. Example welcome flow: email 1 immediately; 2 days later best sellers; 2 days later proof (well-known people using it, reviews); 2 days later an offer. Even small brands see strong open and order rates on good flows.

## 3. Cadence and research

- For most brands, **1–3 emails a week**. Daily discount emails can put up numbers but cause constant list attrition (unsubscribes, fatigue).
- One a week is a fine start; one a month is better than none.
- **Research other brands on Milled**, a free directory of brands' emails: see how many they send a month, what types, and spot A/B tests (two near-identical emails with different headers or fonts) and segments.

## 4. Eight campaign types

Rotate them so people have different reasons to open:

| Type | What it is | Service-business example |
|---|---|---|
| **1. Shop the content** | Reuse content you already made (a video, a carousel's slides) with a bit more written detail. The easiest win | "Our most-shared video this month: 3 signs your switchboard is unsafe" |
| **2. New release** | A new product, service or feature, and why it matters | "We now install home batteries" |
| **3. From the community** | What customers and creators are posting and saying | "This month's favourite before/after from a customer" |
| **4. Business update** | What's happening inside, ideally from a named person | "Hi, Mike here. We've hired two new electricians, so bookings are faster" |
| **5. Better together** | Things that go together, inside or outside your range | "Planning a bathroom? How to choose tiles, lighting and vanity together" |
| **6. Category, history or curation** | Interesting things from your field, for enthusiasts | "5 new building rules Melbourne homeowners should know this year" |
| **7. FAQ** | Answer common questions and objections from sales calls and social | "Do I need to move out during a renovation?" |
| **8. Deals** | Offers and limited-time promotions | "Free safety inspection with any switchboard upgrade this month" |

Deal emails sell the most, but if you only send deals, people stop buying without one. With a mix, people open for many reasons.

**Don't always sell.** Share your best content, ideas and journeys. Value makes people open the next one.

## 5. Style

- **Send from a person.** Emails from the founder, CEO or a named team member build connection over time. For small and service businesses especially, plain-text emails from the founder feel natural and invite replies, which start sales conversations ("What project are you working on? What did you think of the guide?"). One agency selling premium websites switched to founder plain-text emails and got prospects talking to the CEO quickly.
- **Founder emails** are a recurring tool: introduce a sale, tell the story behind a product or an ignored product, celebrate a milestone, or explain a mistake or problem honestly. Put one in the welcome flow and the post-purchase flow so customers get used to hearing from the founder.
- **Give the brand a personality**: a consistent voice and recurring formats.
- **Simple layouts work.** Two or three cards are enough for an email (a headline card, a testimonial card, a reason-to-buy card). Don't overthink it.
- **Lifestyle vignettes.** Ask creators you're already paying for a "photo dump" of their day using the product, and build an email around it.
- **Designed vs plain text:** decide per email. Klaviyo's Composer agent can make basic graphics; AI can make clean UI-style graphics with proper spacing.

## 6. Core flows

**E-commerce**
1. **Welcome**: over 1–2 weeks after sign-up (brand story, best sellers, proof, offer)
2. **Abandoned cart**: reminders, then a stronger reason or offer
3. **Browse abandonment**: viewed a product (pixel + known email) but didn't add to cart
4. **Post-purchase**: thanks, how to use it, review request, cross-sell
5. **Repeat triggers**: second purchase, 100th purchase, one-year anniversary, replenishment
6. **Cross-sell**: bought X, show the thing that goes with it

**Service businesses (Knowtific defaults)**
1. **Enquiry**: instant SMS + email ("Thanks, [name] will call within 10 minutes"), then "what happens next", proof, FAQ
2. **Quote follow-up**: e.g. day 1, day 3, day 7, then monthly; stop when they reply, book, or are marked won/lost
3. **Booking reminders**: day before and morning of (reduces no-shows)
4. **Job complete**: thank you + review request (+ referral ask about a week later)
5. **Rebook / service reminder**: 6–12 months (annual service, check-up, gutter clean)
6. **Win-back**: past customers who haven't booked in a long time
7. **Missed-call text-back**: instant SMS when a call is missed

**Knowtific's follow-up engine** (built on Cloudflare: Workers, D1, Workflows, Email Service, plus an Australian SMS provider) is designed to run exactly these service flows, with stop-on-reply and compliance built in.

## 7. Building flows and the weekly workflow

**Building a flow** (Klaviyo, Kit, Beehiiv and others work similarly): choose a template (welcome series, browse abandonment, loyalty) → set the **trigger** (e.g. viewed product) → add **filters** (e.g. not if they purchased in the last 2 days) → set the **wait time** → add **conditions** (SMS if we have their number, otherwise email) → write the message. Start from the platform's templates and improve later; just setting up the basic flows is high-value work done once.

**Weekly email workflow (Monday):**
1. What happened last week or is coming this week? What content did we post? What did the community post? What happened in the business? What questions or objections came up in sales calls? (Ideally from the end-of-week recap.)
2. Turn that into this week's emails. Don't start from scratch.
3. Decide: plain text from a person, or designed (brief a designer or make graphics with AI)?
4. Write subject lines, schedule, and assign owners and time on the calendar.

It's a flywheel: last week's good video becomes this week's email and a sales asset.

## 8. Segmentation

A **segment** is a smaller group of your list that gets different messages.
- Use behaviour (clicked, viewed, purchased, opened several times) or customer data.
- Tools like Outer Signal analyse a list and reveal big groups. One beauty brand discovered three distinct customer groups (young Gen Z, middle-aged women, and about 7% whose first language was Spanish) and changed messages and language for each.
- You don't need 50 segments; find the few big differences that will lift opens and conversions.
- Service example: a physio clinic segmenting runners, office workers with back pain, and older patients.

**AI help:** connect Klaviyo through the **Klaviyo MCP** and ask in your weekly meeting: "How could our flows perform better? What recent content should we add to automations? Should we create a segment from this persona data?"

## 9. Tools

| Business type | Tools |
|---|---|
| E-commerce | Klaviyo (most common), Omnisend (good value on Shopify), Mailchimp |
| Non-e-commerce, creators, services | Kit (formerly ConvertKit), Beehiiv: simpler, text-friendly, built-in opt-in pages |
| Service follow-up | CRM/job management automations (ServiceM8, Tradify), or Knowtific's follow-up engine |

**Email ideas for service businesses** (same cadence thinking as e-commerce): progress on a current project, a new piece of equipment, meet a team member, a new certification or licence, a big new client, results from recent work, seasonal tips.

## 10. Retention and customer experience

**Retention** means keeping customers and getting them to buy again and spend more. It's one of the most ignored areas: everyone focuses on the first sale.
- Most brands have a **starter product** (a $40–$70 entry item). The retention program educates buyers about the rest of the range and moves them to higher-ticket items over time.
- Like a car brand: their job is to get you to buy that brand again, not switch, and eventually upgrade.
- Services: first job → maintenance plan → bigger project → referrals.

**Customer support is marketing.** How you treat people when something goes wrong drives word of mouth and whether they return. Support should tell marketing which questions keep coming up (fix them with content and messaging upfront) and which customers are advocates (testimonials). Marketing should use support conversations for content ideas and to find people to feature.

**Look up your customers.** One fashion brand started looking up who its customers were and found patterns: many wore the clothes to festivals, and far more customers were influencers than expected. That led to festival collections and a seeding program. Retention work can be manual and still very valuable.

## 11. SMS in Australia

- Since 1 July 2026, branded alphanumeric sender names must be registered on the ACMA **Sender ID** Register (through your SMS provider). Unregistered names are replaced with "Unverified" and grouped into one "Unverified" thread with likely scams. Sending from a normal or virtual mobile number isn't affected and lets customers reply.
- When Knowtific (or any agency) sends for a client, the client owns and registers the sender ID and authorises each SMS provider; the agency is an "entity associate". Sort this out before launching any SMS follow-up.
- Every marketing SMS needs consent, sender identification and an opt-out ("Reply STOP"). See `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/australia-compliance.md`.

## 12. Referrals and word of mouth

Referrals are one of the four places new customers come from, and for tradies and clinics they are often the biggest and cheapest. Most businesses leave them to chance. (This section is Knowtific's practice, not from the source course.)

**Ask at the right moment.** Right after a great moment: the job is finished and the customer is happy, or the patient reports progress. Ask for the review first, then the referral about a week later ("If a neighbour or friend needs a hand, here's a link they can use. You'll both get $50 off").

**Make it easy to pass on.** Give them something forwardable: a short text they can send, a link, a business card or fridge magnet left on the job. People refer more when they don't have to explain you.

**Reward both sides (optional).** A two-sided reward (credit for the referrer and the new customer) works better than a one-sided one. Keep it simple and state the terms. Rules:
- Referral rewards are fine under consumer law if the terms are clear and honest. They are **not** the same as review incentives, which Google bans completely.
- Registered health practitioners: an ad offering a gift, discount or inducement must state its terms and conditions, and must not encourage unnecessary use of services. Many clinics prefer a simple personal thank-you card instead.

**Thank every referrer personally.** A handwritten card, a call from the owner or a small gift (no strings) gets more referrals than any program.

**Build referral partners.** For trades, the best referrals often come from other businesses: builders, real estate agents and property managers, strata managers, insurers' assessors, complementary trades (a plumber and a tiler). For clinics: GPs, personal trainers, other practitioners. Keep a short partner list, stay in touch, and refer work back. See `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/partners-events-retail.md`.

**Use the job site.** Let neighbours know you're working nearby: a polite letterbox card ("We're renovating at no. 12 this week, sorry for the noise. Need anything done while we're here?"), tidy van signage, a yard sign where allowed.

**Track it.** Add "How did you hear about us?" to every form and call script, give referral links or codes, and report referrals as their own channel in the weekly report. If referrals are a big source, protect the things that drive them (speed, tidiness, communication) before spending more on ads.
