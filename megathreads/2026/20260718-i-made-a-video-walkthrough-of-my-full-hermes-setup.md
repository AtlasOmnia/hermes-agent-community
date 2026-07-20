---
title: "I made a video walkthrough of my full Hermes setup (28 cron jobs, 30+ skills) update to my last viral post: I've been asked many times what my Hermes actually does explain! And as you know by now I will spare no details."
author: u/HolmeBengt
date: 2026-07-18
score: 127
comments: 27
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v03vab/i_made_a_video_walkthrough_of_my_full_hermes/
flair: "USE CASE - Real-world tasks, business uses, personal workflows"
---

# I made a video walkthrough of my full Hermes setup (28 cron jobs, 30+ skills) update to my last viral post: I've been asked many times what my Hermes actually does explain! And as you know by now I will spare no details.

**Posted by u/HolmeBengt on 2026-07-18 · 127 points (92% upvoted) · 27 comments**

A few weeks ago, I wrote about what my Hermes agent does all day and it got way more attention than I expected **(234K+ views, thank you!).**

*original post name: I've been asked many times what my Hermes actually does explain! And as you know by now I will spare no details.*

A lot of you asked for more details, so I turned it into a full walkthrough video.

If you prefer reading, I also wrote a detailed blog post: [https://blog.holmebengt.com/post.html?id=hermes-full-setup](https://reddit.comhttps://blog.holmebengt.com/post.html?id=hermes-full-setup)





# Here are all the updates to the last post:



**Mnemosyne Fixed My Biggest Problem**

In the original post I said: "Long-term memory is still the biggest unsolved problem. Dreaming helps, but session-to-session recall remains inconsistent. I built an Obsidian integration but Hermes rarely reaches for it naturally."

Now: I installed Mnemosyne as my memory provider and it completely changed how Hermes remembers things. I can talk about something on Monday, switch to something else for three days, and on Thursday Hermes remembers exactly what we discussed. No more "who are you, what are we building" moments.

This was actually suggested by several people in the comments of the original post — u/Worried_Corner_8541, u/epigrammaticism, and u/SirDomz all recommended it. I said I'd try it, and it genuinely works. If you're running Hermes and struggling with memory, stop what you're doing and set up Mnemosyne. I wrote a detailed guide on my blog too.

**MySalary — From Personal Tool to Product**

In the original post I said: "All my finances live in MySalary, a finance dashboard I built myself and host on my VPS."

Now: I actually released the commercial version. MySalary is now available on my shop — a self-hosted finance dashboard with Hermes API integration, Telegram bot, net worth tracking, and weekly/monthly AI reports. The link is in the video description if you want to check it out. It's brand new and I'm actively developing it based on feedback.

**Food Tracker Got Its Own Gateway**

In the original post I said: "I tell him what I ate that day as precisely as possible, so with weight, and it tracks it."

Now: I built a dedicated food logging gateway. Instead of typing meals into Telegram, I have a proper Hermes Gateway where I log everything text, photo, or barcode scan. It parses macros (calories, protein, fats, even magnesium) through a database and cross-references against my lean bulk targets. The widget on my iPhone lock screen still shows me exactly how many calories and protein I have left for the day.

**The Most Important Questions I Answered (With Full Replies)**

The original post got 200+ comments and I tried to answer every single one. Here are the conversations that generated the most value:

**On "What model do you use?" and token costs**

Several people asked about model choice and costs. I use DeepSeek V4 Flash for everything except vision tasks. My monthly spend is around $17, which I shared as a screenshot in the thread. One person couldn't believe it was that low, and when I compared it to OpenClaw pricing, it made more sense.The key insight: you don't need expensive models for most cron jobs. Flash models handle classification, summarization, and data extraction perfectly fine. Save the expensive inference for complex reasoning tasks.

**On Guardrails and Security**

Someone asked if I have any guardrails or if I'm "raw dogging it." The answer is: many guardrails.

Hermes runs on a dedicated Mac Mini M4. It runs as a standard user, not an admin. I never give it direct access to anything where a mistake would be devastating — no delete permissions on critical data, no direct access to financial accounts, no send capability on email.

The Mail Gatekeeper is designed this way by principle: there is no send endpoint anywhere in the system. Hermes can read and draft, but nothing can physically leave the machine. Every email gets classified by a local Ollama model before it reaches Hermes at all.

**On Getting Apple Health Data Out**

Several people asked how I get Apple Health data into Hermes. The pipeline:

1. **Health Bridge** app on iPhone reads Apple Health data
2. Writes directly to a **Neon PostgreSQL** database
3. Hermes queries the database via API

No Shortcuts, no iCloud middleman, no janky export workflows. Just an app, a Postgres table, and a SELECT query.

**On Ollama Setup**

I run Ollama 24/7 on the Mac Mini for local inference specifically for email classification in the Gatekeeper. The Mac Mini sits at \~15W idle so power cost is negligible. It's set up as a launchd service so it starts automatically on boot. I use TG Pro to manage fan curves since sustained Ollama usage generates heat.

The architecture split: local models for classification and filtering (fast, free, private), cloud API (DeepSeek V4 Flash) for actual agentic work. Never let a cloud model touch raw email content.

**On the Mnemosyne Discovery**

This was the most valuable thread in the entire post. Multiple people recommended memory solutions:

\- u/Worried_Corner_8541 linked to Hermes docs mentioning Mnemosyne, Honcho, and OpenViking

\- u/epigrammaticism recommended Basic Memory and shared their full use case

\- u/SirDomz confirmed they had good results with Mnemosyne

\- u/epigrammaticism said "I've heard only good things about Mnemosyne!"

My reply: "I will try Mnemosyne right now, and I will give you an update if it works."

One month later: it works. Best Hermes decision I've made since setting up the gateway.

thank you all 👍🏻

**On Costs and Value**

Someone asked if this is all just "fluff and pseudo-productivity." My honest answer: it should be fun, and if you get 20% more done or it stops being a pain in the ass, that's fine with me.

Another person said it gives an "illusion of being more productive." My answer: I create time-saving software that I use every day. The finance reports save me hours of manual spreadsheet work. The study audit keeps me accountable. The health coach helped me gain 4kg of lean mass in two months. That's not an illusion.

**On Using Multiple Profiles vs One**

I'm still running everything under one profile with multiple skills. Several people recommended splitting into profiles but I haven't made the switch yet. One user described how they set up separate Telegram bots per profile and said it was easy — Hermes created the profiles automatically. I'll get to this once I stabilize the current setup.

**On the Feedback Loop Learning Curve**

Someone asked if the Writing Improvement tool actually gets better over time. My honest answer: the execution still needs work, but yes — I see a gradual shift in tone and style. It catches patterns I wouldn't notice myself. But sometimes it misses completely. It's still in active iteration.





**TL;DR / What I'd Tell a New Hermes User**

Based on everything I've learned in the last month:

1. **Start with Mnemosyne** — memory is the foundation. Without it, nothing else works well.
2. **Build one skill, nail it, then build the next** — don't try to replicate my 30-skill setup on day one.
3. **Test immediately** — it never works the first time. Fix fast, simplify, move on.
4. **Self-built tools fit better** — downloaded skills never worked as well for me as the ones I built with Hermes from my actual needs.
5. **Share your prompts** — the community gives back way more than you give.
6. **Guardrails from day one** — dedicated machine, limited permissions, no send endpoints.

That's the one-month update. 28 cron jobs, 30+ skills, now with working memory and a commercial product. Still iterating.





Ask me anything happy to share the exact prompts, approaches, and lessons learned 💪

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v03vab/i_made_a_video_walkthrough_of_my_full_hermes/)

