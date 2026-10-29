# Coverage checklist

Every useful topic from the source videos, mapped to where it lives in the plugin. `scripts/verify_coverage.py` reads the table below and checks that each "Check term" appears (case-insensitive) in the listed file, so nothing gets dropped when files are edited.

**Sources**
- **C**: How to Master Marketing in 2026 (full course)
- **MC**: The Art of the Marketing Campaign
- **AM**: The Art of Marketing (every type of marketing)
- **VC**: How to make viral content for any business
- **TE**: The taste economy
- **SS**: Starting brand social media from scratch
- **FN**: The funnels guide
- **K**: Knowtific additions (local SEO, Google Ads, Australian rules, service-business adaptations)
- **CH**: From our planning chats (AU creator platforms, follow-up engine, tools)

**File shorthand**
- `ref/x.md` = `plugins/knowtific-marketing-kit/skills/marketing-coach/references/x.md`
- `skill/x` = `plugins/knowtific-marketing-kit/skills/x/SKILL.md`
- `agent/x` = `plugins/knowtific-marketing-kit/agents/x.md`

Sponsor segments (OpenAI, HubSpot toolkit, Artlist, Dropbox, Omnisend, Swap, Framer) are excluded, except for the useful technique inside them (founder email, creative variants, AI page builders).

## Foundations

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| F01 | Five jobs of marketing: brand, product, content, demand gen, marketing ops | C | ref/foundations.md | marketing ops |
| F02 | Roles are blending; specialise in 2–3, orchestrate the rest with team and agents | C | ref/foundations.md | orchestrate |
| F03 | Distribution is king; the barriers are now taste, distribution and attention | C | ref/foundations.md | distribution |
| F04 | Marketing's real job: differentiate → map toolkit → generate demand → convert → narrative | C | ref/foundations.md | real job |
| F05 | The closer you are to the money, the more valuable you are; don't fear analytics | C, FN | ref/foundations.md | close to the money |
| F06 | Brand strategy vs creative strategy vs creative direction | C | ref/foundations.md | creative direction |
| F07 | Five AI levels: chat, project, skills, agents, brain | C | ref/foundations.md | brain |
| F07b | Project level loads personas, angles and winning scripts | C | ref/foundations.md | winning scripts |
| F08 | What to load into a brand AI project (statement, products, testimonials) and what to skip (long brand guides) | C | ref/foundations.md | brand guide |
| F09 | Multiplayer AI: named owners for projects and skills; scheduled agents (weekly ad summary) | C | ref/foundations.md | multiplayer |
| F10 | Execution is commoditised; the insight is the value; keep an insight compendium | TE | ref/foundations.md | commoditised |
| F11 | Everything is content: ads, training, events, packaging | AM | ref/content-and-social.md | packaging |
| F12 | Marketing leads must stay hands-on with platform details | AM | ref/content-and-social.md | trial reels |
| F13 | Customer support is part of marketing | AM | ref/email-and-retention.md | customer support |
| F14 | Arrive at a job or new client with a 60–90 day plan | C | ref/pr-and-narrative.md | 90-day |
| F15 | Creatives must get comfortable with money and selling | FN | ref/foundations.md | money |

## Positioning, messaging, brand, taste

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| P01 | Positioning = what you're known for; never generic; be remembered | C | ref/positioning-and-brand.md | remembered |
| P02 | AI-legible positioning | C | ref/positioning-and-brand.md | AI-legible |
| P03 | Shelf test | C | ref/positioning-and-brand.md | shelf test |
| P04 | Positioning is relative to competitors and a moving target | AM | ref/positioning-and-brand.md | moving target |
| P05 | Elevator comparison exercise | AM | ref/positioning-and-brand.md | elevator |
| P06 | Good / better / best tiers | AM | ref/positioning-and-brand.md | better / best |
| P07 | Performance positioning (prove with data, metaphors, tests) | C | ref/positioning-and-brand.md | Performance |
| P08 | Category creation / new form factor | C | ref/positioning-and-brand.md | Category creation |
| P09 | Counter-positioning | C | ref/positioning-and-brand.md | Counter-position |
| P10 | Position against ("we're not the bad version") | AM | ref/positioning-and-brand.md | Position against |
| P11 | Counterculture positioning | AM | ref/positioning-and-brand.md | Counterculture |
| P12 | Smart positioning | C | ref/positioning-and-brand.md | Smart |
| P13 | Value positioning (hard vs marketplaces; good for services and newcomers) | C | ref/positioning-and-brand.md | Value |
| P14 | Niche positioning (purchase as support; smaller TAM) | C | ref/positioning-and-brand.md | TAM |
| P15 | Generational positioning | C | ref/positioning-and-brand.md | Generational |
| P16 | Single attribute (own one word) | C | ref/positioning-and-brand.md | one word |
| P17 | Premium: true performance and lifestyle performance | C | ref/positioning-and-brand.md | lifestyle performance |
| P18 | Premium: designer | C | ref/positioning-and-brand.md | Designer |
| P19 | Premium: bespoke | C | ref/positioning-and-brand.md | Bespoke |
| P20 | Premium: luxury quality without the markup | C | ref/positioning-and-brand.md | without the markup |
| P21 | Lifestyle premium (aspiration, intangibles) | AM | ref/positioning-and-brand.md | aspire |
| P22 | Oddball / name positioning | C | ref/positioning-and-brand.md | Name positioning |
| P23 | Positioning is the north star; finding it is your job | C | ref/positioning-and-brand.md | north star |
| P24 | Positioning statement formula (after Geoffrey Moore) | C | ref/positioning-and-brand.md | Geoffrey Moore |
| P25 | Mission, vision and taglines matter less than one statement and one style | C | ref/positioning-and-brand.md | mission statement |
| P26 | Copy style: direct response (Dan Kennedy) | C | ref/positioning-and-brand.md | Dan Kennedy |
| P27 | Copy style: evidence-led (Claude Hopkins) | C | ref/positioning-and-brand.md | Claude Hopkins |
| P28 | Copy style: human / story-driven | C | ref/positioning-and-brand.md | story-driven |
| P29 | Copy style: culturally savvy | C | ref/positioning-and-brand.md | Culturally savvy |
| P30 | Test your way into styles; read the original authors | C | ref/positioning-and-brand.md | books |
| P31 | Add real human stories on top of AI drafts | C | ref/positioning-and-brand.md | AI draft |
| P32 | Taste economy: supply chain democratised; the nice version costs little more | TE | ref/positioning-and-brand.md | democratised |
| P33 | Caring is easy: content educates; algorithms feed taste | TE | ref/positioning-and-brand.md | caring is easy |
| P34 | Little luxuries; identity through taste | TE | ref/positioning-and-brand.md | little luxur |
| P35 | The educated consumer (ingredients, materials) | TE | ref/positioning-and-brand.md | educated consumer |
| P36 | Sell "the best" (mirrors how people search) | TE | ref/positioning-and-brand.md | the best |
| P37 | Hero ingredient or material | TE | ref/positioning-and-brand.md | hero ingredient |
| P38 | Sell the transformation | TE | ref/positioning-and-brand.md | transformation |
| P39 | Enthusiasm is the by-product of education | TE | ref/positioning-and-brand.md | enthusiasm |
| P40 | Premium buyer: cultural omnivore | TE | ref/positioning-and-brand.md | cultural omnivore |
| P41 | Premium buyer: aspirational overspender (petite bourgeoisie) | TE | ref/positioning-and-brand.md | petite bourgeoisie |
| P42 | Premium buyer: true elite (in person, long-form storytelling) | TE | ref/positioning-and-brand.md | true elite |
| P43 | Premium buyer: aspiring logo-buyer; balancing them | TE | ref/positioning-and-brand.md | logo |
| P44 | Pick 1–2 buyer types and plan product + marketing for them | TE | ref/positioning-and-brand.md | archetype |
| P45 | True luxury is a generational play built on craft | TE | ref/positioning-and-brand.md | generational play |
| P46 | Insights: what people say about themselves vs what's true; take stances | TE | ref/insights-and-research.md | say about themselves |
| P47 | Brand lore: mood boards, behind the scenes, lookbooks | MC | ref/positioning-and-brand.md | mood board |
| P48 | Brand world map as a paid workshop credited against a retainer | C | ref/positioning-and-brand.md | credited |
| P49 | Characters (founder, experts, team, customers via Outer Signal, collaborators, podcasters) | C | ref/positioning-and-brand.md | Outer Signal |
| P50 | Sets: evergreen vs temporary; night-before trade show filming; Osmo for factory teams; local videographers via Upwork | C | ref/positioning-and-brand.md | Upwork |
| P51 | Events: company (bundle features into a release), culture, industry (launch before/with/after competitors) | C | ref/positioning-and-brand.md | before them |
| P52 | Plot: enemies, friends, specials (social shows, own events) | C | ref/positioning-and-brand.md | specials |
| P53 | Find the holes; revisit monthly or quarterly; calendar feeds email | C | ref/positioning-and-brand.md | holes |
| P54 | Rebrand process that protects existing brand equity | K | skill/rebrand | brand equity |

## Content and social

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| S01 | Free attention is the advantage ("alpha") and still underused | C | ref/content-and-social.md | alpha |
| S02 | Organic success factors: narrative, taste, focus, credibility | C | ref/content-and-social.md | credibility |
| S03 | Pick one main network; don't be average everywhere | C | ref/content-and-social.md | focus |
| S04 | TikTok needs an "army": multiple accounts, creators, slideshows; Social Growth Engineers | C, MC | ref/content-and-social.md | Social Growth Engineers |
| S05 | Regional or language accounts; hands-only POV videos | C | ref/content-and-social.md | hands |
| S06 | Instagram strategies: expert, storytelling, art-directed | C | ref/content-and-social.md | art-directed |
| S07 | Expert on a separate account promoting the brand | C | ref/content-and-social.md | separate account |
| S08 | YouTube for services; 1–2k views can be enough; thumbnails and titles; searchable tutorials | C, AM | ref/content-and-social.md | thumbnail |
| S09 | LinkedIn is a team sport; employee programs | C | ref/content-and-social.md | team sport |
| S10 | X and Snapchat secondary; YouTube Shorts with low expectations | SS | ref/content-and-social.md | Shorts |
| S11 | Goals and metrics: hook rate, views, saves, shares; reach, leads, sales | C | ref/content-and-social.md | hook rate |
| S12 | Content funnel top/middle/bottom; viral top content raises the floor | C | ref/content-and-social.md | raises the floor |
| S13 | The world beats the brand account; multiply personalities | C | ref/content-and-social.md | personalit |
| S14 | You compete with the whole feed; ICP feed exercise | C | ref/content-and-social.md | ICP |
| S15 | Shareability test | C | ref/content-and-social.md | share |
| S16 | Pattern examples: founder comparisons, factory quests, web designer critiquing brand sites | C | ref/content-and-social.md | web design studio |
| S17 | Minimum team: social manager + on-camera person | C | ref/content-and-social.md | on camera |
| S18 | Pillar system: 3–5 formats, 3–4 each per month, monthly review, swap after two bad months, report | C | ref/content-and-social.md | two months |
| S19 | Traction in 3–5 months, good by 6 | C | ref/content-and-social.md | 3–5 months |
| S20 | Cross-post everything natively | C, SS | ref/content-and-social.md | cross-post |
| S21 | Level 2: separate strategy per network; collaborator pillar | C | ref/content-and-social.md | collaborator pillar |
| S22 | Idea tools and video databases: hook analysis, narrative frameworks, outliers; look outside the niche | C | ref/content-and-social.md | outlier |
| S23 | Social shows / episodic series | C | ref/content-and-social.md | episod |
| S24 | Best fit: services and expert-driven products; a person or lens delivering expertise | SS | ref/content-and-social.md | lens |
| S25 | Awareness sources: ads, referral, cold outreach, organic (uncapped) | SS | ref/content-and-social.md | uncapped |
| S26 | Short-form is evergreen: Instagram in Google; seasonal resurfacing; no slop | SS | ref/content-and-social.md | slop |
| S27 | Content in every funnel stage (page, pre-call, call, post-call, email) | SS | ref/content-and-social.md | pre-call |
| S28 | Four content types: storytelling, ratings and rankings, breakdowns, scenarios | SS | ref/content-and-social.md | ratings and rankings |
| S29 | Two formats: carousel or video (talking head, vlog, green screen) | SS | ref/content-and-social.md | green screen |
| S30 | Storytelling with the hero's journey | SS | ref/content-and-social.md | hero's journey |
| S31 | Student vs expert perspective | SS | ref/content-and-social.md | student |
| S32 | Look the part | SS | ref/content-and-social.md | look the part |
| S33 | Breakdowns: give away the playbook; current-event breakdowns | SS | ref/content-and-social.md | playbook |
| S34 | Scenarios: exact situations | SS | ref/content-and-social.md | over 40 |
| S35 | Thoughtful content beats easy content; small views still valuable | SS | ref/content-and-social.md | 600 views |
| S36 | Focus TikTok + Instagram; LinkedIn/X if you'll engage | SS | ref/content-and-social.md | TikTok and Instagram |
| S37 | Creator accounts, not business accounts (TikTok Shop exception) | SS | ref/content-and-social.md | creator account |
| S38 | Start the account in the target country | SS | ref/content-and-social.md | country |
| S39 | Schedulers reportedly hurt reach; post natively (test it) | SS | ref/content-and-social.md | scheduler |
| S40 | Cadence: 2–3 type×format combos, 2 each weekly (4–6 posts), one month before judging | SS | ref/content-and-social.md | 4–6 posts |
| S41 | Layer in content answering common comment questions | SS | ref/content-and-social.md | common questions |
| S42 | No CTA until traction; then lead magnets via bio or comment-to-DM (ManyChat) | SS | ref/content-and-social.md | ManyChat |
| S43 | Reply to every comment and DM; proactive DMs; social is a sales tool | SS | ref/content-and-social.md | every comment |
| S44 | Ignore guru hacks | SS | ref/content-and-social.md | hack |
| S45 | Batch filming every two weeks from prepared scripts | SS | ref/content-and-social.md | batch |
| S46 | Level up the set | SS | ref/content-and-social.md | set |
| V01 | No boring businesses, only boring content | VC | ref/content-and-social.md | boring content |
| V02 | Format shakeup | VC | ref/content-and-social.md | Format shakeup |
| V03 | Speed / speedrun | VC | ref/content-and-social.md | speedrun |
| V04 | Viral vehicle | VC | ref/content-and-social.md | viral vehicle |
| V05 | "This is amazing" skill showcase | VC | ref/content-and-social.md | This is amazing |
| V06 | Expertise inside exciting scenarios | VC | ref/content-and-social.md | exciting scenario |
| V07 | Strong takes | VC | ref/content-and-social.md | hot take |
| V08 | Current events and pop culture (attention hijacking) | VC | ref/content-and-social.md | attention hijack |
| V09 | Questions people feel dumb asking | VC | ref/content-and-social.md | dumb |
| V10 | Versus format | VC | ref/content-and-social.md | versus |
| V11 | Lore and depth (be the biggest nerd; "the Coachella of X" hooks) | VC | ref/content-and-social.md | nerd |
| V12 | Normal content plus one interesting element | VC | ref/content-and-social.md | ladder |
| V13 | Tour guide to a hidden world; sell access to the world | VC | ref/content-and-social.md | tour guide |
| V14 | Hooks in three parts; mechanisms (blitz, storytime); simple outlines | C | ref/content-and-social.md | punch line |
| V15 | Critique others' work in your field ("what I would have done") | VC | ref/content-and-social.md | what I would have done |

## Campaigns

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| M01 | What a campaign is (launch, feature, company news, seasonal) | MC | ref/campaigns.md | seasonal |
| M02 | Start from an insight or a concept | MC | ref/campaigns.md | concept |
| M03 | Core channels | MC | ref/campaigns.md | Core |
| M04 | Extensions (retailers and partners) | MC | ref/campaigns.md | Extensions |
| M05 | Existing customers first (early access, VIP one-to-one emails) | MC | ref/campaigns.md | early access |
| M06 | Merchandising (displays, pallets, gondolas, signage) | MC | ref/campaigns.md | pallet |
| M07 | Organic first, then ads, then creators (loop) | MC | ref/campaigns.md | organic first |
| M08 | Phase: tease (low stakes) | MC | ref/campaigns.md | Tease |
| M09 | Phase: unveil (walkthroughs become product page assets) | MC, C | ref/campaigns.md | Unveil |
| M10 | Phase: launch (hero asset, multiple shots, carousels from stills, meme carousel) | MC | ref/campaigns.md | meme carousel |
| M11 | Phase: extend (tutorials, unboxing, FAQ; works for B2B) | MC | ref/campaigns.md | unboxing |
| M12 | Phase: performance (ads checklist) | MC | ref/campaigns.md | selfish desire |
| M13 | Phase: sustain and refresh (wave 2, top comments) | MC, C | ref/campaigns.md | wave 2 |
| M14 | 15–22 pieces per launch | MC | ref/campaigns.md | 15–22 |
| M15 | Plan every asset before the shoot | MC | ref/campaigns.md | shot list |
| M16 | Production matters less than concept | MC | ref/campaigns.md | low-fi |
| M17 | Creator flywheel: multiply winning ideas across creators | MC | ref/campaigns.md | flywheel |
| M18 | Events in campaigns (trade show, own event, VIP Zoom, office meetup) | MC | ref/campaigns.md | VIP |
| M19 | Brand world network (partner content folder, collabs, regional paid; ~10% great) | MC | ref/campaigns.md | 10% |
| M20 | World levers: pro team, retailers, seeding, free trials, email, giveaways, in person, volume, crossover | MC | ref/campaigns.md | giveaway |
| M21 | Scale past a fixed budget when the economics work | MC | ref/campaigns.md | fixed budget |
| M22 | Compounding moment (1+1+1+1 > 4) | MC | ref/campaigns.md | compound |
| M23 | Always-on chain of campaigns | MC | ref/campaigns.md | back to back |
| M24 | Concepts creators can easily join | MC | ref/campaigns.md | easy to join |
| M25 | Campaign types: theme, anchor launch, feature bundle, yearly theme | C | ref/campaigns.md | anchor |
| M26 | Internal vs external grid per stage; asset list with owners, dates, work-back | C | ref/campaigns.md | work-back |
| M27 | Enabled media: owned + paid + enabled | TE | ref/campaigns.md | enabled |
| M28 | Australian marketing calendar | K | ref/campaigns.md | EOFY |

## Funnels, offers, landing pages

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| N01 | Funnel drop-off; analyse every stage | AM, FN | ref/funnels-and-offers.md | drop off |
| N02 | Traffic is precious | AM | ref/funnels-and-offers.md | precious |
| N03 | Attention sources incl. referral, search/AI, foot traffic | C | ref/funnels-and-offers.md | foot traffic |
| N04 | CTA and the three-line bio | C | ref/funnels-and-offers.md | bio |
| N05 | Landing page, not homepage; conversion maths | C | ref/funnels-and-offers.md | homepage |
| N06 | Default pages first; audience variants as spend grows | C | ref/funnels-and-offers.md | variant |
| N07 | Product page (PDP) structure | C | ref/funnels-and-offers.md | PDP |
| N08 | Service page structure | K | ref/funnels-and-offers.md | service page |
| N08b | Home page structure for local services | K | ref/funnels-and-offers.md | Home page (local service business) |
| N09 | Listicle page | C, FN | ref/funnels-and-offers.md | listicle |
| N10 | Luxury page (why it's worth it; macro shots) | C | ref/funnels-and-offers.md | macro |
| N11 | Page modules: comparison chart, feature videos, quiz, fit on different bodies | C, AM | ref/funnels-and-offers.md | comparison chart |
| N12 | Swipe file; screenshot → AI builder; brand design skill | C, FN | ref/funnels-and-offers.md | swipe file |
| N13 | Soft CTAs enable hard CTAs | AM, SS | ref/funnels-and-offers.md | soft |
| N14 | Answer buying objections on the page | AM | ref/funnels-and-offers.md | objection |
| N15 | Hard-CTA page essentials (objective, benefits, testimonials, FAQ) | SS | ref/funnels-and-offers.md | objective |
| N16 | Offer formula: "I'm a [X] that does [Y] for [Z]" | FN | ref/funnels-and-offers.md | that does |
| N17 | Leads, CRM, leads vs customers | FN, C | ref/funnels-and-offers.md | CRM |
| N18 | Lead magnets (checklist, quote, report for long sales cycles) | FN, SS | ref/funnels-and-offers.md | lead magnet |
| N19 | Squeeze page | FN | ref/funnels-and-offers.md | squeeze page |
| N20 | Thank-you page | C, FN | ref/funnels-and-offers.md | thank-you page |
| N21 | "Prepare for your call" page | FN | ref/funnels-and-offers.md | prepare for your call |
| N22 | Upsell | FN | ref/funnels-and-offers.md | upsell |
| N23 | Extras / bonuses | FN | ref/funnels-and-offers.md | bonus |
| N24 | Guarantee | FN | ref/funnels-and-offers.md | guarantee |
| N25 | Sales call above roughly $2,000 | FN | ref/funnels-and-offers.md | $2,000 |
| N26 | Setter and closer | FN | ref/funnels-and-offers.md | setter |
| N27 | Automation | FN | ref/funnels-and-offers.md | automation |
| N28 | Top and bottom of funnel; qualified and hot leads | FN | ref/funnels-and-offers.md | qualified lead |
| N29 | DM funnel | FN | ref/funnels-and-offers.md | DM funnel |
| N30 | Lead magnet funnel | FN | ref/funnels-and-offers.md | lead magnet funnel |
| N31 | Tripwire funnel (can fund ad spend) | FN | ref/funnels-and-offers.md | tripwire |
| N32 | Webinar funnel | FN | ref/funnels-and-offers.md | webinar |
| N33 | Video sales letter funnel and its beats | FN | ref/funnels-and-offers.md | video sales letter |
| N34 | Test page variants (length, light/dark, video, three copy angles) | FN | ref/funnels-and-offers.md | dark mode |
| N35 | After-signup emails: instant, then day 2 best content, then nurture | FN | ref/funnels-and-offers.md | day 2 |
| N36 | The email list is a lifetime asset | FN | ref/funnels-and-offers.md | asset |
| N37 | Speed to touch | C | ref/funnels-and-offers.md | speed to touch |
| N38 | Close assets | C | ref/funnels-and-offers.md | close assets |
| N39 | North-star numbers: page conversion and close rate; volume; qualified rate | C | ref/funnels-and-offers.md | close rate |
| N40 | Map the funnel with the sales team | C | ref/funnels-and-offers.md | sales team |
| N41 | AI page builders; we build in Next.js | FN | ref/funnels-and-offers.md | Framer |

## Paid ads

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| A01 | ROAS with worked example | C | ref/ads.md | ROAS |
| A02 | CPA | C | ref/ads.md | CPA |
| A03 | CAC, LTV, first-order profitability, 3:1 | C | ref/ads.md | first-order |
| A04 | Diagnostic metrics (CTR, add to cart, checkout, CPC, CPM, thumb stop) | C | ref/ads.md | thumb stop |
| A05 | Measurable marketing earns budget | C | ref/ads.md | justifiable |
| A06 | Meta first for most | C | ref/ads.md | Meta |
| A07 | Google Ads; harder interface; data connectors (Windsor) | C | ref/ads.md | Windsor |
| A08 | TikTok ads at roughly 30–50% of Meta scale | C | ref/ads.md | 30–50% |
| A09 | LinkedIn ads | C | ref/ads.md | LinkedIn ads |
| A10 | Incremental platforms (AppLovin, Shop app, Snapchat) | C | ref/ads.md | AppLovin |
| A11 | YouTube ads underpriced; horizontal creative | C | ref/ads.md | horizontal |
| A12 | TV (Tatari) | C | ref/ads.md | Tatari |
| A13 | Newsletter sponsorships | C | ref/ads.md | newsletter sponsorship |
| A14 | Platform order; local services: search intent first | C, K | ref/ads.md | search intent |
| A15 | Needle movers: customer + message, product, price sweet spot, bundles, offer, creative | C | ref/ads.md | sweet spot |
| A16 | Meta campaign setup; CBO vs ABO; budget sharing off | C | ref/ads.md | CBO |
| A17 | Ad set settings incl. bid caps later, $50/day, placements | C | ref/ads.md | bid cap |
| A18 | Custom columns | C | ref/ads.md | columns |
| A19 | Audiences: custom, lookalike 1/3/10%, interest, broad | C | ref/ads.md | lookalike |
| A20 | Weekly creative strategy loop | C | ref/ads.md | creative strategy |
| A21 | Ad volume benchmarks | C | ref/ads.md | 400 |
| A22 | 3–10 genuinely different ads per ad set | C | ref/ads.md | 3–10 |
| A23 | Naming convention | C | ref/ads.md | naming |
| A24 | Kill/scale rule: spend 3–5× target before judging | C | ref/ads.md | 3–5× |
| A25 | Scaling | C | ref/ads.md | scaling |
| A26 | AI connections: read and light edits; don't auto-publish | C | ref/ads.md | auto-publish |
| A27 | AI for hooks, angles and mock-ups | C | ref/ads.md | mock-up |
| A28 | Ad asset types incl. catalog (Marpipe) and whitelisted | C | ref/ads.md | catalog |
| A29 | Creative diversity | C | ref/ads.md | creative diversity |
| A30 | Ad concept checklist | MC, C | ref/ads.md | magazine editorial |
| A31 | Creative variants: voiceover gender, accent, region, language | AM | ref/ads.md | voiceover |
| A32 | Google Ads basics for local services | K | ref/ads.md | negative keywords |
| A33 | Pixel and Conversions API | K, C | ref/ads.md | Conversions API |

## Creators and influencers

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| R01 | Creator vs influencer | C | ref/creators.md | influencer |
| R02 | Creator content performs in ads; creative diversity | C | ref/creators.md | creative diversity |
| R03 | Seeding | C | ref/creators.md | seeding |
| R04 | Affiliates (TikTok Shop, ShopMy, LTK) | C | ref/creators.md | ShopMy |
| R05 | Creators as the face of the account, a separate account, or many creators | C | ref/creators.md | face of |
| R06 | Sourcing tools (Outer Signal, Tribe, Sideshift, Later, Meta, Social Snowball, agencies) | C | ref/creators.md | Sideshift |
| R07 | Australian marketplaces and manual local search | CH | ref/creators.md | Collabstr |
| R08 | The pyramid: micro, mid, anchors | C | ref/creators.md | pyramid |
| R09 | AI agent for sourcing and outreach | C | ref/creators.md | agent |
| R10 | It's a numbers game | C | ref/creators.md | numbers game |
| R11 | Modular brief; top 10% don't need one | C | ref/creators.md | modular brief |
| R12 | Whitelisting and darklisting | C | ref/creators.md | darklist |
| R13 | Agreement: raw files, ad code, usage rights, edits, price | CH | ref/creators.md | usage rights |
| R14 | Seeding system: find, contact, send, track, graduate to paid; keep it in-house | AM | ref/creators.md | graduate |
| R15 | Long-term partnerships over one-offs | AM | ref/creators.md | long-term |
| R16 | PR kit design; free trials for software | MC | ref/creators.md | PR kit |
| R17 | Pro teams and ambassadors | MC | ref/creators.md | pro team |
| R18 | Micro creators can outperform | MC | ref/creators.md | micro |
| R19 | Give creators a theme attached to the launch | MC | ref/creators.md | theme |
| R20 | Disclosure rules | K | ref/creators.md | disclos |
| R21 | Advanced creative "brains" (Motion) | C | ref/creators.md | Motion |

## Email, SMS, retention

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| E01 | Campaigns vs flows | C | ref/email-and-retention.md | flow |
| E02 | Research others' emails on Milled; spot A/B tests | C | ref/email-and-retention.md | Milled |
| E03 | 1–3 emails a week; daily discounting causes list attrition | C | ref/email-and-retention.md | attrition |
| E04 | Don't always sell; give it a personality | AM | ref/email-and-retention.md | personality |
| E05 | Eight campaign email types | C | ref/email-and-retention.md | better together |
| E06 | Lifestyle vignette from a creator photo dump | C | ref/email-and-retention.md | photo dump |
| E07 | Simple card layouts | C | ref/email-and-retention.md | cards |
| E08 | Plain text from a real person | C | ref/email-and-retention.md | plain text |
| E09 | Founder email uses (sale, story, milestone, mistake) | SS | ref/email-and-retention.md | mistake |
| E10 | Core flows incl. browse abandonment, second purchase, anniversary, cross-sell | C, AM | ref/email-and-retention.md | browse abandonment |
| E11 | How a flow is built (trigger, filter, wait, condition) | C | ref/email-and-retention.md | trigger |
| E12 | Start from templates | C | ref/email-and-retention.md | templates |
| E13 | Weekly Monday email workflow | C | ref/email-and-retention.md | Monday |
| E14 | Plain vs designed; Klaviyo Composer; UI-style graphics | C | ref/email-and-retention.md | Composer |
| E15 | Segmentation (language, age, behaviour) | C | ref/email-and-retention.md | segment |
| E16 | Klaviyo MCP for flow analysis | C | ref/email-and-retention.md | Klaviyo MCP |
| E17 | Tools by business type | C | ref/email-and-retention.md | Kit |
| E18 | Email ideas for service businesses | C | ref/email-and-retention.md | certification |
| E19 | Service flows | K | ref/email-and-retention.md | quote follow-up |
| E20 | Retention: starter product → bigger purchases | AM | ref/email-and-retention.md | starter product |
| E21 | Support feeds marketing; looking up customers reveals patterns | AM | ref/email-and-retention.md | look up |
| E22 | SMS and sender IDs | K | ref/email-and-retention.md | Sender ID |
| E23 | Knowtific follow-up engine (Cloudflare) | CH | ref/email-and-retention.md | Cloudflare |
| E24 | Referral programs and word of mouth (ask timing, two-sided rewards, partners, tracking) | K | ref/email-and-retention.md | Referrals and word of mouth |
| E25 | Agencies sending SMS for clients are entity associates | K | ref/email-and-retention.md | entity associate |

## Sales support and outbound

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| L01 | Leads and CRM fields | C | ref/sales.md | CRM |
| L02 | Collateral by stage, incl. a forwardable package and upsell at ~90 days | C | ref/sales.md | forward |
| L03 | Collateral types (FAQ, case study, best content, infographics, comparisons) | C | ref/sales.md | infographic |
| L04 | Asset request process for sales | C | ref/sales.md | request |
| L05 | Reuse: one asset, many places | C | ref/sales.md | flywheel |
| L06 | Speed of response | C | ref/sales.md | 60 seconds |
| L07 | Number of touches (the 11th touch) and a reason for each | C | ref/sales.md | 11th |
| L08 | Triage social leads to sales | C | ref/sales.md | triage |
| L09 | Work with the hungriest salesperson | C | ref/sales.md | hungriest |
| L10 | Record calls (Granola, Fathom); mine objections weekly | C | ref/sales.md | Granola |
| L11 | Sales leaders back marketing that moves revenue | C | ref/sales.md | sales leaders |
| L12 | DM selling | SS, FN | ref/sales.md | DM |
| L13 | Outbound tools and setup (Sales Navigator, ListKit, Apollo, domains, warm-up) | C | ref/sales.md | Sales Navigator |
| L14 | Outbound for Knowtific's own client acquisition | CH | ref/sales.md | Knowtific |
| L15 | Phone outreach: Do Not Call Register and calling hours | K | skill/outbound | Do Not Call |
| L16 | One-to-many selling (webinars, community calls) | FN | ref/sales.md | one-to-many |

## SEO and search

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| O01 | SEO and AI search | AM | ref/seo.md | Perplexity |
| O02 | SEO tools | AM | ref/seo.md | Ahrefs |
| O03 | Only the top 3 matter | AM | ref/seo.md | top 3 |
| O04 | Brand name clashes | AM | ref/seo.md | brand name |
| O05 | Low-difficulty single-term opportunities | AM | ref/seo.md | difficulty |
| O06 | Dedicated page with write-up and embedded video | AM | ref/seo.md | embed |
| O07 | Engagement signals and links | AM | ref/seo.md | links |
| O08 | It takes months; long-term free traffic | AM | ref/seo.md | months |
| O09 | Do SEO before a launch | AM | ref/seo.md | before launch |
| O10 | Search habits: best, worst, reviews, vs | TE | ref/seo.md | worst |
| O11 | Instagram posts in Google; YouTube searchable titles | SS, AM | ref/seo.md | Instagram posts |
| O12 | Local SEO: Google Business Profile, reviews, suburb pages, citations, schema | K | ref/seo.md | Google Business Profile |
| O13 | Visibility in AI answers | K | ref/seo.md | AI answers |

## Partnerships, events, retail

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| X01 | Selling events | AM | ref/partners-events-retail.md | selling event |
| X02 | B2B trade shows: book meetings, set a sales goal | AM | ref/partners-events-retail.md | trade show |
| X03 | Customer appreciation events | AM | ref/partners-events-retail.md | appreciat |
| X04 | Piggybacking events; hosting your own | MC | ref/partners-events-retail.md | piggyback |
| X05 | Local customer meetup | MC | ref/partners-events-retail.md | pizza |
| X06 | Collaborations and their logistics | AM | ref/partners-events-retail.md | collaboration |
| X07 | Collaboration calendar; ongoing programs | AM | ref/partners-events-retail.md | Moncler |
| X08 | Licensing | AM | ref/partners-events-retail.md | licensing |
| X09 | Why a retailer should stock you (data, regional traffic, support, shelf gap) | AM | ref/partners-events-retail.md | regional |
| X10 | Merchandising (shelf-ready boxes, aisle interrupters, displays) | AM | ref/partners-events-retail.md | aisle interrupter |
| X11 | Retail staff training | AM | ref/partners-events-retail.md | field team |
| X12 | Retailer collab posts and newsletter features | MC | ref/partners-events-retail.md | retailer |
| X13 | Partner and reseller content network | MC | ref/partners-events-retail.md | reseller |
| X14 | Events designed for content (enabled) | TE | ref/partners-events-retail.md | Coachella |

## PR and internal narrative

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| Q01 | Press coverage is worth less than it used to be | C | ref/pr-and-narrative.md | journalist |
| Q02 | Crisis communication and role-play | C | ref/pr-and-narrative.md | crisis |
| Q03 | Weekly email: wins, next, blockers, stats | C | ref/pr-and-narrative.md | blockers |
| Q04 | Roll-up from team leads to executives | C | ref/pr-and-narrative.md | roll-up |
| Q05 | Cheerlead wins; advocate for the team | C | ref/pr-and-narrative.md | cheerlead |
| Q06 | Monthly social report | C | ref/pr-and-narrative.md | monthly |

## Insights and research

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| I01 | Sources of insight: reviews, support, calls, comments, DMs, customer look-ups | AM, C | ref/insights-and-research.md | reviews |
| I02 | Said vs real; conviction | TE | ref/insights-and-research.md | conviction |
| I03 | Insight compendium | TE | ref/insights-and-research.md | compendium |
| I04 | Ask AI what the audience pays attention to | C | ref/insights-and-research.md | pay attention to |
| I05 | Competitor research | K | ref/insights-and-research.md | competitor |

## Australian compliance

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| K01 | Spam Act | K | ref/australia-compliance.md | Spam Act |
| K02 | SMS Sender ID Register | K | ref/australia-compliance.md | Sender ID |
| K03 | AHPRA advertising | K | ref/australia-compliance.md | AHPRA |
| K04 | Provable claims | K | ref/australia-compliance.md | provable |
| K05 | Fake or incentivised reviews | K | ref/australia-compliance.md | reviews |
| K06 | Paid content disclosure | K | ref/australia-compliance.md | disclos |
| K07 | Licence numbers | K | ref/australia-compliance.md | licence |
| K08 | Privacy | K | ref/australia-compliance.md | Privacy |
| K09 | TGA rules for health products | K | ref/australia-compliance.md | TGA |
| K10 | DMs can be commercial electronic messages | K | ref/australia-compliance.md | instant message |
| K11 | Guarantees can't remove consumer guarantees | K | ref/australia-compliance.md | consumer guarantees |
| K12 | Google review policy: no incentives, no review gating | K | ref/australia-compliance.md | gating |
| K13 | Health providers covered by Privacy Act regardless of turnover | K | ref/australia-compliance.md | whatever their turnover |
| K14 | Single total price rule | K | ref/australia-compliance.md | single total price |
| K15 | Telemarketing: DNCR and calling hours | K | ref/australia-compliance.md | Do Not Call Register |
| K16 | Victorian trade regulator is the BPC (replaced VBA) | K | ref/australia-compliance.md | Building and Plumbing Commission |

## Tools and connections

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| T01 | DataForSEO | CH | ref/tools.md | DataForSEO |
| T02 | Google Ads MCP (read-only) | CH | ref/tools.md | google-ads-mcp |
| T03 | Google Analytics MCP | CH | ref/tools.md | analytics-mcp |
| T04 | Meta Ads MCP (can spend money) | CH | ref/tools.md | mcp.facebook.com |
| T05 | Klaviyo MCP | CH | ref/tools.md | Klaviyo |
| T06 | SEO suites (Ahrefs, Semrush, SE Ranking) | CH | ref/tools.md | SE Ranking |
| T07 | Search Console | CH | ref/tools.md | Search Console |
| T08 | PageSpeed Insights | CH | ref/tools.md | PageSpeed |
| T09 | Browser for screenshots and rendered pages | CH | ref/tools.md | Playwright |
| T10 | Call notes | CH | ref/tools.md | Granola |
| T11 | Graceful fallback when a tool isn't connected | CH | ref/tools.md | fallback |

## Skills and agents

| ID | Topic | Src | File | Check term |
|---|---|---|---|---|
| SK01 | Marketing coach routes to the right reference | – | skill/marketing-coach | references |
| SK02 | Project setup | – | skill/init | marketing/ |
| SK03 | Full marketing audit | – | skill/audit | scorecard |
| SK04 | Positioning | – | skill/position | positioning statement |
| SK05 | Rebrand | – | skill/rebrand | rebrand |
| SK06 | Brand world | – | skill/brand-world | holes |
| SK07 | Customer insights | – | skill/customer-insights | insights.md |
| SK08 | Design brief | – | skill/design-brief | mood board |
| SK09 | Copy | – | skill/copy | direct response |
| SK10 | Content ideas | – | skill/content-ideas | angle |
| SK11 | Script | – | skill/script | hook |
| SK12 | Social plan and review | – | skill/social-plan | pillar |
| SK13 | Campaign plan | – | skill/campaign-plan | unveil |
| SK14 | Creator brief | – | skill/creator-brief | brief |
| SK15 | Ads maths | – | skill/ads-math | ads_math.py |
| SK16 | Ad concepts | – | skill/ad-concepts | hook |
| SK17 | Ads plan and weekly review | – | skill/ads-plan | ad_set_review.py |
| SK18 | Funnel build | – | skill/funnel-build | funnel_math.py |
| SK19 | Landing page review | – | skill/lp-review | checklist |
| SK20 | Email flows | – | skill/email-flows | flow |
| SK21 | Sales kit | – | skill/sales-kit | objection |
| SK22 | Outbound | – | skill/outbound | Spam Act |
| SK23 | SEO plan | – | skill/seo-plan | DataForSEO |
| SK24 | Partnerships and events | – | skill/partnerships | event |
| SK25 | Crisis response | – | skill/crisis | crisis |
| SK26 | Weekly report | – | skill/weekly-report | blockers |
| SK27 | Landing page reviewer agent | – | agent/landing-page-reviewer | checklist |
| SK28 | Site auditor agent | – | agent/site-auditor | positioning |
| SK29 | Market researcher agent | – | agent/market-researcher | competitor |
| SK30 | Social review script | – | skill/social-plan | pillar_report.py |
