---
name: script
description: Turns a content idea into a ready-to-film video script or carousel (three-part hook with on-screen text, visual and spoken line; simple outline; full script or slide copy; shot list and B-roll; set and props; caption with searchable keywords; organic and ad CTA versions; alternative hooks; cross-posting notes). Use when the user wants a script, a talking-head video, a Reel or TikTok, a carousel, a YouTube video outline, or a batch of scripts for a filming day.
argument-hint: "[idea or topic]"
---

# Script

Read `${CLAUDE_PLUGIN_ROOT}/skills/marketing-coach/references/content-and-social.md` sections 5–7 and 11.

## Inputs
- The idea (from `$ARGUMENTS`, `marketing/content-bank.md`, or the user).
- `marketing/brand.md` (voice, proof), `insights.md` (customer phrases), `brand-world.md` (character and set).
- Platform and length (default: vertical 30–60 seconds for Reels/TikTok; carousels 6–10 slides; YouTube 6–12 minutes).

## Output for a video
```
Title (internal):
Type / angle / funnel stage:
Character + set + props (look the part):

HOOK (first 2–3 seconds)
- On-screen text:
- Visual:
- Spoken line:
Alternative hooks (2): ...

OUTLINE
1. Hook
2. ...
3. CTA

SCRIPT
[spoken lines, short sentences, with [B-ROLL: ...] and [TEXT: ...] cues]

SHOT LIST
- A-roll: ...
- B-roll: ...

CAPTION (with the words people search for)
CTA versions
- Organic: (none yet if the account lacks traction; else comment-to-DM or link in bio)
- Ad version: (clear CTA + landing page)
Cross-post notes: (TikTok/IG/Shorts/LinkedIn/Facebook differences)
Compliance check:
```

## Output for a carousel
Slide-by-slide copy (slide 1 = the hook, last slide = the CTA or save/share prompt), design notes (layout, imagery per slide), caption and alt text.

## Output for YouTube
Title options (searchable), thumbnail concept (text ≤4 words + visual), intro hook, chapter outline, key points with examples, CTA, description with links and chapters.

## Batch mode (filming day)
If asked for several scripts: group by set and outfit, order to minimise changes, add a one-page run sheet (time, script, location, props), and an equipment checklist.

## Rules
- Write for speaking: short lines, contractions, no jargon.
- Give value fast; no long intros.
- The hook must earn the next 3 seconds; the payoff must match the hook.
- Never invent statistics or testimonials. Health clients: education, not outcome promises.
