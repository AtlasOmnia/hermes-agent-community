---
title: "Hermes gets 90% through an Amazon return then hits a wall. The reason picker blocks every automated click."
author: u/W1141175
date: 2026-10-05
score: 24
comments: 33
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wxhfdq/hermes_gets_90_through_an_amazon_return_then_hits/
flair: "Help — Technical issues, errors, config, debugging"
---

# Hermes gets 90% through an Amazon return then hits a wall. The reason picker blocks every automated click.

**Posted by u/W1141175 on 2026-10-05 · 24 points (90% upvoted) · 33 comments**

Trying to have Hermes return two items from an Amazon order. It opens the return, selects the item, gets to the reason page, and stops dead.
The reason buttons are plain HTML buttons. Visible, topmost, not disabled. Hermes clicks them at exact pixel coordinates in Camoufox and nothing happens. Tried trusted mouse clicks, direct DOM clicks, keyboard focus plus Enter and Space. None register. My guess is Amazon rebuilt this step on the Rufus widget and it filters out anything that is not a real finger.
Workaround so far is dumb: I pick the reason by hand in the app and Hermes cannot finish the job.
Has anyone gotten past this? If there is a flag or a path I am missing, I would love to hear it.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wxhfdq/hermes_gets_90_through_an_amazon_return_then_hits/)
