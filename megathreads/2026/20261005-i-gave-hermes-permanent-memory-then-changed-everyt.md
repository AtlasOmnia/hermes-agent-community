---
title: "I gave Hermes Permanent Memory … then changed everything else."
author: u/creativ4art
date: 2026-10-05
score: 42
comments: 48
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wxxc16/i_gave_hermes_permanent_memory_then_changed/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# I gave Hermes Permanent Memory … then changed everything else.

**Posted by u/creativ4art on 2026-10-05 · 42 points (92% upvoted) · 48 comments**

It’s been 6+ months roughly with Hermes… and boy it has been a ride!
This is my journey. It’s a long one so grab a drink 🥃
Things I loved -
Relatively Fast (than open claw)
Great access to tools
Access to root / OS level stuff
I was like anything is possible! Woohoo agents who can learn and adapt! YouTubers vouching for it!! … pfft.. easier promised than delivered.
I was unemployed, had limited runway and some time.. so figured let’s just make a bot-trader and set out to make my Fever dream happen with Hermes!
The issues I ran into -
Inconsistent memory
Constant prompting to do stuff
Constant probing to fetch stuff
Looses context mid turn
Looses trail mid turn
Agent storing memory but failing to retrieve it.
Agent storing memory but looking it up with different strings.
Agents not being able to “connect the dots”
Giving vague instructions took it for a spin.
Finds stray tail ends and goes on a chase only to realize it’s on the wrong path.
Annoying compression loops that got in the way.
Unwanted bloat that costed more
Random nuking of days’ worth of work - Guardrails was not doing its thing
… and lots more that I can list.
Let’s just say, coz of all of the above, my fever dream was distant! The harness was inconsistent and flawed by design.
I was done. Tried different models, different platforms. My wallet was bleeding.. $200-300 in api costs.
I was frustrated and not to mention depressed!
The honeymoon phase was over.
I don’t want to prompt it to fetch $hit.
I don’t want to remind it every time to load Skills…
I don’t want to keep reminding it to check sessions!!
I didn’t want to fix one thing one day and then the next morning come back and see it’s broken again coz of some update.
I don’t want to spend time writing a 200-word prompt every time.
I want them to know stuff about me.
I want it to know - I found this in my recent trip -> what trip am I referring to and not make one up.
Check your logs for errors -> which log am I referring to…
catch up in you session -> it pulls up some parent session that was 5 days ago and summarizes!
Do a git pull on your core -> what does core mean and which core am I referring to!
I don’t want every /reset to spawn a blank agent.
I don’t my msg to be the first thing to bring up an agent
If do not say catch up or ground yourself it will just say Hi and sit there. Or if I say am a mango today, it would just agree.
It’s just bad UX ( My background in SaaS and UX kicked in)
I tried memory plugins like Obsidian and Holographic. But the trend was the same. Agents would store (sometimes) facts but each run it wouldn’t know the fact existed. So essentially each run it was almost running cold.
And as mentioned before, even when prompted to look at the memory or session for facts, if you didn’t give the exact term, it would not find it. And then go looking all over for the first tail end it could find.
Had enough. I started the journey to fork the core and rebuild.
3 months later… I now have  -
Core agents with Postgres memory
No more .md files. PG is the source of truth.
All vectorized. Queries are blazing fast.
Agents are able to ground themselves in 2-4 turns instead of 10-20 turns.
Even skills recide in memory now.
Don’t have to prompt agents to load skills.
Don’t have to prompt agents to catch up. They do it instinctively.
Don’t have to tell them where to look.
I reduced bloat and optimized sessions.. at 131k context size each turn end still remains at 40-60% full.
Even though each set of turns end up with like 1-2M tokens, cache is hit 90%+ of the time so costs are super low.
Plus gave it like 10 adaptive and learnin loops so it auto-learns and adapts.
Session continuity is preserved so if you leave and come back after a visit to the throne, she still knows what the last move was.
Compression even if it fires does not destroy continuity.
It stores bread crumbs from our interactions so it serves as hints to context.
No random stalls.
New session refreshes what it should and still keeps the agent warm.
On gateway restart agent welcomes me in their own voice. And not wait for my msg to start a conversation.
Platform independent- all over telegram app - no additional installs required.
And lots more …
It’s now de-coupled from the stock Hermes so the updates don’t break stuff. I am happy with the way things are and agents are consistent on long-standing projects and tasks.
So if anyone has a VPS / VM, and thought about integrating PG for native, it’s possible but it’s a long haul. If you have a local GPU, I’d suggest using it for embedding and STT instead of running local models. But that’s just my preference. My net cost has gone down from $100/week to $20-40/month.
My setup - Dell server with proxmox, split into various instances. Has P5000 and 2060 GPU for basic embeds and voice-to-text decode. LLMs run on DS cloud through Ollama and it’s blazing fast.
All this has given me some good knowledge on how the harness works.
So feel free to AMA. I can try to answer.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wxxc16/i_gave_hermes_permanent_memory_then_changed/)
