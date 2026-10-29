# Paid advertising

## Contents
1. The numbers
2. Which platforms, in what order
3. What actually makes ads work
4. Meta setup, step by step
5. Targeting
6. The weekly loop: testing, killing, scaling
7. Ad formats and creative
8. Ad concept checklist
9. Google Ads for local services
10. Tracking
11. Using AI with ad accounts

---

## 1. The numbers

| Metric | Meaning | Use |
|---|---|---|
| **ROAS** (return on ad spend) | Revenue ÷ ad spend. 0.5 = spend $1, get 50c back. 2 = spend $1, get $2 | Arguably the most important for e-commerce; lets you build a model |
| **CPA** (cost per action) | Cost to get one sale (or lead) on average | Compare to the product's price: $30 CPA is fine on a $100 product, terrible on a $35 one |
| **CPL** (cost per lead) | Cost to get one enquiry | Service businesses |
| **CAC** (customer acquisition cost) | Cost to win a *new* customer | Growth focus |
| **LTV** (lifetime value) | What a customer spends with you over time | Lets you pay more upfront when customers return |
| **Close rate** | % of leads that become paying jobs | Converts CPL into cost per customer |

**Worked example (e-commerce).** A $100 product costs $25 to make (a common 4× markup in fashion). An ad at 2 ROAS means you spent $50 to get the $100 sale. Profit: $100 − $50 ad − $25 product = **$25**. This simple maths is how online advertising works: if the numbers work, spend more.

**First-order profitability vs LTV.** Small businesses with tight cash need the first order to be profitable. Businesses with data and capital can judge acquisition against lifetime value: if customers average $2,000 over time, the first order doesn't need to make money. A common goal is **LTV ≈ 3× CAC** (e.g. average customer worth $100 → aim for about $33 to acquire them); when those economics hold, growth can be very fast.

**Service businesses add the close rate:** CPL $40 and 1 in 4 leads become jobs → $160 per customer. Average job $2,500 → excellent. Always do this maths before ads: use `ads_math.py` (ads-math skill).

**Diagnostic metrics** (signals, not goals): CTR (click-through rate), add-to-carts, checkouts initiated, email sign-ups from pop-ups, CPC (cost per click), CPM (cost per 1,000 impressions), and thumb stop / hook rate (% watching the first seconds). Don't obsess over CPM, CPC or thumb stop. A high CPM doesn't matter if ROAS is good; use them to find *where* a problem is.

**Measurable marketing gets budget.** Because ads are measurable, they make marketing justifiable. Marketing is a combination: social drives awareness and early sales and leads; ads bring it home; other initiatives come as you grow. The more measurable you make it, the bigger the budgets and the more interesting the work you'll get to do.

## 2. Which platforms, in what order

| Platform | Notes |
|---|---|
| **Meta** (Facebook + Instagram) | The first choice for about 90% of brands; "a money-printing machine" for many. The interface can be learned in an hour |
| **Google Ads** | Search ads, shopping, display. Excellent when there's a lot of search demand. Harder interface; many hire specialists. Data connectors (e.g. Windsor.ai, or the official Google Ads MCP) let AI read results |
| **TikTok ads** | Works like Meta; reuse Meta creative. Often reaches roughly 30–50% of Meta's scale in suitable categories, especially for mid-size brands and TikTok Shop sellers |
| **YouTube ads** | Underpriced opportunity; the best second platform. Needs horizontal versions of creative |
| **LinkedIn ads** | Expensive but works for B2B or high-ticket services. Far after Meta |
| **Incremental** (AppLovin in mobile games, Shopify's Shop app, Snapchat) | For e-commerce brands already spending six or seven figures a month. Each adds a few % (3–7%) |
| **TV / connected TV** (e.g. Tatari) | Advanced; not for starting out |
| **Newsletter sponsorships** | Underrated for unusual niches and high-ticket offers. Use the Beehiiv ad network, or ask AI for popular newsletters in the niche; many have rate cards. Agree the audience, placement, CTA and lead goal |

**Typical order (e-commerce):** Meta → reuse on TikTok → YouTube (horizontal) and Google around the same time → incremental platforms when spend is large.

**Local services (Knowtific clients):** urgent, high-intent needs (burst pipe, hot water, emergency electrician, "physio near me") are *searched*, so **search intent comes first: Google Search and Google Business Profile**. Meta creates demand for things people aren't searching for yet (renovations, solar and batteries, "fix your back pain", premium services). Most local clients need both.

## 3. What actually makes ads work

Media buying is simply **directing money to what's working and constantly testing new things** so you always have winners. It's a continuous weekly process, never set-and-forget. The biggest needle movers, in order:
1. **Who the customer is and the right message for them** (positioning).
2. **Which product or service you pitch** (lead with what already sells).
3. **Price point.** Every brand has a sweet spot. One fashion brand found $180–$350 items worked on Meta; cheaper items sold but the maths didn't. If a product is too cheap to advertise profitably, **bundle** it.
4. **The offer**: the angle and the deal ("free inspection", "fixed quote in 24h", "first visit $49", "10% off this month").
5. **The creative**: designs, videos, hooks.

## 4. Meta setup, step by step

1. **Create campaign.** Choose Auction. Objective: **Sales** for most; **Leads** for service businesses that capture leads.
2. **Name it** clearly.
3. **Budget type.**
   - **Campaign budget (CBO / Advantage+ campaign budget):** Meta spreads money across ad sets. Consider only with lots of data, good customer lists and experience.
   - **Ad set budget (ABO):** you control spend per ad set. **Recommended for most starting out.** Turn off budget sharing.
4. **Ad set = one concept.** Every new idea gets its own ad set (e.g. "founder ads", "art-directed product carousels") with 3–10 variations inside. If it works, increase its budget without affecting other ad sets.
5. **Ad set settings:**
   - Conversion location: website (or instant form/lead form for leads)
   - Audience: all customers to start; later test new-customers-only and understand both economics
   - Performance goal: maximise number of conversions
   - Bid strategy: **highest volume** to start. ROAS goals and bid caps come later, once you know your numbers and are scaling
   - Attribution: standard
   - Daily budget: the source's benchmark is about **$50/day per ad set** (as low as $10 is slow; $100 learns faster), quoted in US dollars for e-commerce. In Australia, plan on **about A$50–75/day per ad set, or whatever reaches 3–5× the target cost per lead in about 5 days** (run `ads-math`). Small local businesses with tiny budgets should test fewer ad sets rather than starve each one
   - Placements: Advantage+ (all) is fine to start; or restrict to Instagram, Stories or Facebook
6. **Create the ad.** Upload image or video, or paste a **partnership ad code** to run a creator's post from their account (see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/creators.md`). Add the website URL (ideally a dedicated landing page), primary text, headline, CTA button.
7. **Customise columns** in Ads Manager to show what matters: spend, results, cost per result, ROAS, CTR, CPM, frequency, hook rate.

## 5. Targeting

| Option | How | When |
|---|---|---|
| **Custom audiences** | Upload customer or lead lists; connect Instagram/Facebook engagers; website visitors via the pixel | Always build these. They teach Meta who your customers are |
| **Lookalikes** | From a custom audience: 1% (closest match), 3%, 10% (widest) | Start around 3%, then expand to 10% |
| **Interest targeting** | Age, location, interests from a list ("ages 30–60, Melbourne, interested in home renovation") | Only when you have no data |
| **Broad** | No restrictions; Meta finds people | Once Meta has lots of conversion data from the account |

Order: lookalikes → broad once there's data. Interests only with no data at all. For local services, always set the location radius to the service area.

## 6. The weekly loop

**The creative strategy cycle, forever:** plan new creative → buy the media (launch) → report on results → plan the next creative from the results. It can be one person or several.

**Volume:**
- Small accounts: 2–3 new ad sets a week × about 3 ads = 9–10 new ads a week
- Large brands: 50–100 new ads a month, some 200–400

**Rules:**
- Group ads into ad sets logically: by customer profile or creative type ("targeting mums", "green-screen ads").
- **3–10 ads per ad set**, each genuinely different (different creator, take, or style), not tiny tweaks.
- **Naming**: include the customer profile and creative type, e.g. `Homeowners45+ | Owner-to-camera | Wk43`. Good naming lets you and AI read what works.

**Kill / scale rule.** Set a target cost per result. Spend **3–5× that target** on an ad set before judging. Example: target $50 per sale, 5 days, $250 spent:
- 5+ sales (on target) → **increase budget** (scaling; common practice is about 20–30% every few days)
- About 3 → keep testing a little longer
- 0 sales but many add-to-carts, checkouts or sign-ups → the ad works; fix the landing page, offer or message
- Terrible on everything → turn it off

For services, judge on cost per customer, not just cost per lead (see ads-math). Use `ad_set_review.py` (ads-plan skill) to apply the rule to an export.

**Scaling** = increasing spend on what works, while adding new ideas each week based on what's succeeding.

## 7. Ad formats and creative

| Format | Notes |
|---|---|
| **Static** | Single image. Fast to make and test |
| **Video** | Short vertical video (Reels/TikTok style) |
| **Carousel** | Several swipeable images or videos |
| **Catalog** | Auto-generated from an e-commerce catalog; mainly retargeting. Tools like Marpipe dress up catalog images |
| **Whitelisted / partnership** | Runs from a creator's account (see `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/creators.md`). Many strong accounts run 30–50% of the ads in their account this way |

**Creative diversity.** Use many different people (ages, genders, backgrounds, styles: vlogs vs talking to camera). Different customers respond to different faces.

**Creative variants at scale.** Make versions of a winning ad for different audiences: male vs female voiceover, regional accents or languages (e.g. an Australian voiceover for local ads), different hooks, lengths and aspect ratios. AI voice and editing tools make this fast.

## 8. Ad concept checklist

Make sure every launch or month has a spread of these:
1. **Problem–solution**: name the pain, show the fix
2. **Founder story**: why we started, why we do it this way
3. **Selfish desire**: what's in it for me (status, time, money, looks, comfort)
4. **Reply-to-comment**: answer a real comment on video
5. **Magazine editorial**: styled like an article or review
6. **User testimonial / UGC** (not for AHPRA-regulated clinical claims)
7. **Static image**: bold headline + product or result
8. **Category comparison**: us vs the usual option
9. **Offer-led**: the deal is the hero
10. **Demonstration / before-after**: show the result (with care for health claims)
11. **Listicle**: "5 reasons homeowners in [suburb] choose us"
12. **Objection-buster**: tackles the #1 reason people don't buy

## 9. Google Ads for local services

The video course barely covers Google; these are Knowtific's core practices.
- **Campaign types:** Search for high-intent services; Performance Max only once conversion tracking is reliable; check whether Local Services Ads are available for the client's category in Australia.
- **Keywords:** service + location ("emergency plumber Ringwood"), service + intent ("hot water repair same day"). Use phrase and exact match to start; broad match only with strong conversion data and smart bidding.
- **Negative keywords** from day one: jobs, courses, DIY, free, cheap (if premium), competitor names (if not bidding on them), irrelevant suburbs. Review the search terms report weekly.
- **Location targeting:** the real service area, "presence" (people in the area) not "interest".
- **Ad assets:** call assets with business hours, location asset (linked Google Business Profile), sitelinks to service pages, callouts (licensed, fixed price, same-day), structured snippets.
- **Landing pages:** one per service theme, matching the ad's words (message match).
- **Bidding:** start with manual CPC or Maximise Clicks with a cap to gather data, then Maximise Conversions / target CPA once there are roughly 30+ conversions a month.
- **Brand campaigns:** bid on the business's own name if competitors or directories show above it.

## 10. Tracking

Nothing works without it. Before spending:
- **Meta pixel + Conversions API** (server-side events) for lead and purchase events
- **Google Ads conversion tracking** (form submits, calls from ads, calls from the site, imported offline conversions if a CRM records won jobs)
- **GA4** with key events, and UTM parameters on every ad and social link
- **Call tracking** for phone-heavy businesses
- Test every event before launch.

## 11. Using AI with ad accounts

- Connect the ad account to AI (official MCP connections; see tools.md). Each Monday ask: what worked last week, which ad sets to turn off, which to scale, and give 10 new hook ideas based on what's working and the customer profile.
- Ask for a **mock-up** of an ad idea (a rough static) to send a designer as a reference, or have the AI write briefs for creators.
- **Read and make light changes only** (budgets, pausing). **Don't auto-publish** lots of ads through automation: platforms may shut down accounts that look automated. Publish ads yourself in Ads Manager.
- Advanced teams use a creative "brain" (e.g. Motion's tools) connecting ad results, creative strategy and briefs.
