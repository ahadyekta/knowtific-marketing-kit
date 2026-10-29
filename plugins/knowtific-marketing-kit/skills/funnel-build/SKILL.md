---
name: funnel-build
description: Designs a client's full funnel from attention to customer: the offer statement, choice of funnel type (lead magnet, tripwire, webinar, video sales letter, DM funnel, direct quote), lead magnet idea, page plan (landing/squeeze, thank-you, "prepare for your call" pages), CRM and speed-to-touch setup, follow-up touches, close assets, setter/closer roles, and the numbers model with funnel_math.py showing what each improvement is worth. Use when the user asks how to get more leads or sales from the same traffic, wants a funnel, lead magnet, offer, VSL or webinar, or when leads aren't converting.
argument-hint: "[offer or goal]"
---

# Funnel build

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md` in full, and `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/sales.md` sections 3–5.

## Inputs
- `marketing/brand.md`, `offer.md`, `economics.md`, `funnel.md` (current state), `insights.md` (objections).
- Current numbers if known: monthly visitors or ad spend + CPC, page conversion, qualified %, booked %, close rate, job value, margin, response time.
- The codebase (if Knowtific builds the site) to see existing pages and forms.

## Process
1. **Map the current funnel** stage by stage (attention → CTA → page → lead → CRM → follow-up → customer → repeat/referral) and mark the leaks.
2. **Offer.** Write the offer statement ("We're a [X] that does [Y] for [Z]"), then sharpen: what's included, extras/bonuses, guarantee (consumer-law safe), genuine urgency, price signals. Decide whether a sales call is needed (often for anything above roughly $2,000).
3. **Choose the funnel type** and say why:
   - Direct quote/booking (urgent services)
   - Lead magnet funnel (considered purchases, long sales cycles)
   - Tripwire (entry product that can fund ad spend, then upsell)
   - Webinar / workshop (one-to-many education then offer)
   - Video sales letter (complex offers, strong presenter)
   - DM funnel (strong social presence)
4. **Lead magnet** (if used): 3 options matched to the buyer's question (checklist, price guide, quiz, report, mini video course, free audit), with title, format and outline. Pick one.
5. **Page plan** (each with purpose, sections and CTA):
   - Landing / squeeze page (structure from `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/funnels-and-offers.md`)
   - Thank-you page (video from the person who'll call, next steps, proof, optional upsell to book now)
   - Booking confirmation / "prepare for your call" page (who you'll meet, agenda, what to have ready)
   - For VSL: the script beats (problem → unique method → why us → objections → CTA); for webinar: registration page + reminder sequence + outline
6. **Follow-up system:**
   - Speed to touch target (under 5 minutes) and how: instant SMS/email, notification to the caller, AI responder (Knowtific follow-up engine)
   - Touch sequence (number, timing, channel, reason for each), stopping on reply/booking
   - Close assets (before and after the call)
   - Roles: owner, setter, closer; CRM fields to track (source, stage, next action)
   - Email automation after sign-up: instant confirmation and intro, day 2 best content, then nurture (use `email-flows` for the full sequence)
7. **Numbers.** Model baseline and improvements:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/funnel-build/scripts/funnel_math.py" --spend 1500 --cpc 3 --lp-cvr 4 --qualified 70 --booked 80 --close-rate 35 --job-value 2500 --margin 40 --scenario lp-cvr=8 --scenario close-rate=45
```
(Windows: `python` or `py`.) Percentages are whole numbers (4 = 4%). **Close rate in this script is booked/quoted → customer only.** If you only have the leads → jobs close rate from `marketing/economics.md`, leave `--qualified` and `--booked` at 100 so it isn't counted twice. Show which fix is worth most and prioritise it.
8. **Tests.** Page variants (long vs short, light vs dark, with/without video, three copy angles), offer variants, lead magnet variants.

## Output
Save `marketing/funnel.md` (update) and a detailed plan at `marketing/audits/funnel-plan-YYYY-MM-DD.md` with a diagram (text arrows), page specs, follow-up table, numbers, and the build order. Offer to build the pages in the codebase (using brand tokens from `marketing/design/` and `copy` for the words), then run `lp-review`.

## Rules
- Fix the biggest leak first (often response speed or the page, not traffic).
- Never invent proof for pages; use placeholders.
- Compliance: guarantees, pricing, health rules, consent for messages.
