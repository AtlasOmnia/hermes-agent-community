---
title: "Honcho: One Month Review"
author: u/Farkovnio
date: 2026-09-29
score: 9
comments: 15
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wspwz5/honcho_one_month_review/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# Honcho: One Month Review

**Posted by u/Farkovnio on 2026-09-29 · 9 points (100% upvoted) · 15 comments**

A recent thread prompted me to do a bit of an analysis on how Honcho has impacted my Hermes instance, I am self hosting both so my Honcho expenditure doesn't even register, it has cost me €0.22 over the past 30 days. I had Hermes review it's own sessions over the past month and both it and I reviewed the actual contents of Honcho's database.
It seems to have had a net positive impact on quality for me, Hermes own memory can be stale or limited in comparison to what it's injecting on top of it. I have to provide much less exposition to Hermes than I did without it, although some of this can just be attributed to skills, there are other parts that are clearly Honcho. For example today I fired a one line prompt to Hermes about where I was in a current project, Hermes memory had no context for what the hell I was on about, it hadn't updated to reflect current state and didn't know the file I was working on existed, Honcho did, and I got a quality response in one.
It does hold a fair bit of nonsense though, a small but notable % of Honcho's database are transient pieces of information like "Farkovnio hasn't pushed yet" (presumably git) and "Farkovnio is waiting on a response" (presumably some prior project blocker I was waiting on an email or part for), these are odd but very difficult to surface organically, I suspect their only real impact is taking up storage space, and it's not that much.
An amusing finding is it's ingested it's own deriver prompt as facts about me, the deriver prompt includes the following section:
These examples are fabricated illustrations of the output format. Never emit a conclusion for which content comes from these examples. Every conclusion must be supported by the <messages> block only.
EXAMPLES (using `alice` as the target peer id):
- EXPLICIT: <message idx="0" peer="alice" target="true">I just turned 25</message> → "alice is 25 years old"
- EXPLICIT: <message idx="1" peer="alice" target="true">I took my dog for a walk in NYC</message> → "alice has a dog", "alice walked her dog in NYC"
- EXPLICIT: <message idx="2" peer="alice" target="true">I've lived in NYC for six years</message> → "alice lives in NYC", "alice has lived in NYC for six years"
There were 28 examples in honchos memory where it logged some variation of me being a 25 year old dog owning woman from NYC. I am none of these things, and while it only represents a fraction of a percent of the data honcho held, it does explain that one time Hermes hallucinated a dog for me.
Overall, net positive. The vast majority of what Honcho holds is worthwhile and what it's injecting into conversations is meaningful, but it does hold a small amount of odd or false statements and I would imagine at some point it will cause Hermes to run with a strange assumption. I think it's worth keeping for me, at it's current cost the conversational benefits are very clear. I expect running a cron job to find and remove erroneous conclusions or even just upgrading the model I'm using a smidge would get rid of the weaker conclusions but I'm not hugely bothered unless they start surfacing. In the meantime I've just modified it's inbuilt prompt and deleted all reference to my NYC alter ego from the database.
I'd be interested to know if anyone else has reviewed the impact of their memory provider beyond general vibes, I know some people are having great results with mnemosyne or hindsight for example, what does that look like? Are you also getting strong responses to single line expositionless prompts and did you too get a free imaginary dog?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wspwz5/honcho_one_month_review/)
