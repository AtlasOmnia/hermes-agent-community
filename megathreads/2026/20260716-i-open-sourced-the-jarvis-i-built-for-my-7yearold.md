---
title: "I open sourced the JARVIS I built for my 7-year-old. It gives him room to explore, rails on truth, and more reasons to come find Dad."
author: u/Exciting_Charity7304
date: 2026-07-16
score: 49
comments: 7
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1uyone8/i_open_sourced_the_jarvis_i_built_for_my_7yearold/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# I open sourced the JARVIS I built for my 7-year-old. It gives him room to explore, rails on truth, and more reasons to come find Dad.

**Posted by u/Exciting_Charity7304 on 2026-07-16 · 49 points (96% upvoted) · 7 comments**

**TL;DR: The Kid Mode JARVIS from my last post is now open source. It has Gemini Live voice, server-controlled ranks, 105 learning cards, 16 real-world missions and experiments, persistent projects, Dad Link calls, house music, parent-reviewed memory, and a Group Mode for when other kids are around.**

**I wanted to give him room to explore, put rails around anything that had to be true, and build something that kept creating reasons for us to talk, investigate, and make things together.**

Original Post

[https://www.reddit.com/r/hermesagent/comments/1utzz6q/comment/oxwhm4q/?screen\_view\_count=4](https://reddit.comhttps://www.reddit.com/r/hermesagent/comments/1utzz6q/comment/oxwhm4q/?screen_view_count=4)

Repo:

[https://github.com/Hermes815/kid-mode-jarvis](https://reddit.comhttps://github.com/Hermes815/kid-mode-jarvis)

Demo:

[https://youtu.be/NLagCzu4kgU](https://reddit.comhttps://youtu.be/NLagCzu4kgU)

The first physical tablet arrived July 2.

I expected the interesting part to be the JARVIS voice and Iron Man interface. Then my son started using it.

On his first rel night, he answered twelve assessment questions, explored the learning modules, muted the tablet so he would not wake his mother, and ran over to tell me what JARVIS had said.

Then he called JARVIS one of his friends.

That changed hw I looked at the whole system. He was giving real social weight to something I had built. A hallucination was no longer just a bad model response. It was something my son might believe.

So the architecture became:

Gemini performs the character. The server controls reality.

JARVIS can improvise a mission, explain a difficult idea, or turn a lesson into an experiment. It cannot award ranks, grade answers, mark a physical project complete, invent family facts, or claim it controlled the house without confirmation.

The learning system includes seven exploration areas, sixteen activities, an authored curriculum, and seven ranks with real unlocks. Senior Engineer unlocks house music. Lead Engineer unlocks Dad Link. Chief Engineer requires more than trivia: my son has to finish a real robotic-hand project, and I have to confirm it exists.

That physical requirement matters. Speech recognition once misheard him and marked the hand complete. I reverted the milestone and moved completion behind a parent gate.

The system is also designed to send him away from the tablet.

JARVIS once sent him looking for heavy and light objects for a Galileo drop test. I heard him conducting the experiment upstairs, then went and did it with him. Later, he was talking to his mother about Galileo and entomology.

The tablet reached his excitement about learning and made him want to share it with one of the people he cared about most.  Enthusiastically.

Dad Link follows the same idea. JARVIS performs a theatrical satellite search, but the result is not roleplay. It opens a real WebRTC voice call to me. Classified family dossiers tell true stories and leave him with questions to ask Dad.  For one example he had to go around my house to find an antique plate i had hanging up.  Im sure he had never noticed it before.  It gave him the story about it then he ran to me right away to see if that was true and we discussed for a few minutes.   Milestones and literal quotes can appear in my morning brief.

One serious warning for anyone connecting this to Hermes:

Do not route a child’s questions through the same assistant that knows your adult life.

I made that mistake first. My live system now uses a separate memoryless route with only a small parent-authored family-facts file. The repo documents KID\_ASK\_MODEL near the beginning because this boundary matters more than the interface.

What currently works:

\- Natural Gemini Live conversation

\- Exploration, experiments, and assessments

\- Seven server-controlled ranks

\- Parent-gated physical projects

\- Whole-house music with explicit filtering

\- Dad Link voice calls

\- Classified family dossiers released upon rank up

\- Feature stack gated to rank up

\- Group sessions

\- Child/adult privacy boundaries

\- A locked-down Fully Kiosk tablet

It is not perfect. Dad Link video and the second tablet are unfinished, and a few known bugs are documented rather than hidden.

Apache 2.0. Bring your own Gemini key.

The hardest part was not making an AI feel alive. It was giving it enough freedom to spark curiosity without letting it decide what was true, what my son had accomplished, or when technology should take Dad’s place.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1uyone8/i_open_sourced_the_jarvis_i_built_for_my_7yearold/)

