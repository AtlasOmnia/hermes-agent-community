---
title: "Missing features ideas... after months of using Hermes"
author: u/SnooPaintings8639
date: 2026-09-14
score: 8
comments: 13
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wf8e3a/missing_features_ideas_after_months_of_using/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# Missing features ideas... after months of using Hermes

**Posted by u/SnooPaintings8639 on 2026-09-14 · 8 points (100% upvoted) · 13 comments**

Hey there. Do devs come and look at this sub? I hope so. I have some thoughts I wish to share.
The "ask your agent to write it" is not the best approach to altering Hermes runtime. I wish my setup was reproducible across my setups. i.e. once my machine die, I want it to work the same way on new machines. Hence, it would be great to have it 'git-compatible' version of all I do, so that I can backup it easily. Until then, the changes should be a feature request, as below next two.
We need a mode, in which Hermes does NOT alter it's memory or other control files (soul or whatever else there is) on its own. I hate when it changes something and it alters all my other sessions in unpredictable manner, and I really value reproducibility and stability. I just wish to have a flag that requires my acceptance of ANY persistant change the Hermes itself. These approval requrest can be in-lined or just enqueued for later review.
Background task timeouts... it does not matter which model I use, they do it wrong. They set a 10 or minutes as timeout for any longer running task, and once it's reached, they just run the same task again with longer timeout. Nah, this is not what timeout is for. Hermes should run a task WITHOUTH the hard timeout (i.e. without killing the process). It should instead call all its task with 'soft-timeout' wrapper, by default. Once the 'soft-timeout' is hit, the agent should be awoken and then decide if it is time to kill the process, or let it run.
I set it up myself, but I know that my new agents wont have it enshrined, and I strongly believe them are a sensible defaults all instances should start with.
Cheers 🍻

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wf8e3a/missing_features_ideas_after_months_of_using/)
