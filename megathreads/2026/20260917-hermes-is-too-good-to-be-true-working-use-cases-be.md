---
title: "Hermes is too good to be true. (working use cases below)"
author: u/xbxz
date: 2026-09-17
score: 30
comments: 6
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wijyx0/hermes_is_too_good_to_be_true_working_use_cases/
flair: "Use Case — Real tasks, business & personal"
---

# Hermes is too good to be true. (working use cases below)

**Posted by u/xbxz on 2026-09-17 · 30 points (89% upvoted) · 6 comments**

So, I run a small software development company having 20ish devs spanning over 4-5 enterprise grade client systems. It includes node, next, flutter, wordpress and all. Everyday, team reviews a handful of large PRs (5k+/1k-) and its was time consuming. For quick prototypes too for new prospective clients, everything requires a hell lot of manual work.
For PRs and daily status and daily ios/apk builds for clients, it's almost a manual work so far, from sending team a notification regarding pr reviewed to sending client status and all.
Enters Hermes. Tried with a couple of local models on 16gb vram. Agent goes into loop backs of tool calls. Of course. Then started using deepseek v4 flash. Somewhat better performance but not exactly what i was looking for. Tried v41 flash and its good.
Slap full hermes on one vps. Gave root access. Provided access to my teams irc, repo access and cf access, nginx and almost set hermes free too take actions once I say yes after his active prompting to me. After a couple of days of tweaking, it automatically does most of my manual tasks which listed above. The skills creator skill is life saver.
Now, my process is create a skill first for whatever I wanted to do, add test cases for it and then do the actual task. One nit is that it does not have a test skills which checks which skills will be picked up by what prompt so it's mostly trial and error only.
It seamlessly connects with my handmade mcps to wrappers and almost everything.
One con I feel is the session management over its gateways. I'm yet to find the option where i can continue my cli sessions to slack without corrupting its sqlitedb. Raised a couple of issues with fixes of hermes git already. Another con is that it's token hungry. Like it consumes a hell lot of tokens. Planning to use local models for easy tasks but need to find the solution. Suggestions always welcomed.
Overall 8/10 agent.
Slap me with your use cases. I'd be happy to know your hermes use cases.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wijyx0/hermes_is_too_good_to_be_true_working_use_cases/)
