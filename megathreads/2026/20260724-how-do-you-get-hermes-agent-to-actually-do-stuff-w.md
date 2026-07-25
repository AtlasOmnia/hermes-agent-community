---
title: "How do you get Hermes Agent to actually do stuff well?"
author: u/PM_ME_YOUR_REPORT
date: 2026-07-24
score: 18
comments: 23
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v5tixs/how_do_you_get_hermes_agent_to_actually_do_stuff/
flair: "Help — Technical issues, errors, config, debugging"
---

# How do you get Hermes Agent to actually do stuff well?

**Posted by u/PM_ME_YOUR_REPORT on 2026-07-24 · 18 points (85% upvoted) · 23 comments**

I'm a convert from Openclaw to Hermes Agent, came looking for some stability. I'm using a basic conversion setup and running Grok-4.3 as the underlying model on their Pro level plan. I'm finding I'm struggling to get my agent to actually do anything useful.

For instance yesterday I gave it a detailed markdown spec of an image set I wanted it to search the web for and collect for LORA training purposes. It kept on asking me for confirmation every step of the way. When I finally said "go ahead and do whatever is needed to do this task and work through all the problems autonomously" it went ahead and started working. However it just collected a list of images and the image directory was empty. When I told it actually need you to download the images, it went a downloaded the same image 250 times, not the ones it had catalogued.

Then today I asked it to do another task I have a skill already working for, but it confused what I wanted with the LORA collection task and told me it didn't understand what I wanted and did I send the message by mistake.

I've used grok cli for coding and found it extremely capable so it doesn't feel like the model is the problem, just the agent setup. Do you need to put a lot more effort into building agents manually to get it to really act reliably? I have given it a soul that says it should act proactively and work autonomously in a goal driven way, and develop it's own skills. But when it does act proactively it's just a complete screw up.

Where am I going wrong? Does anyone have recommended resources on actually getting stuff done with this rather than just hyping how good it is supposed to be over Openclaw?

  
I'm running Hermes Agent (Nous Research) locally on macOS using the default profile. It’s configured with grok-4.3 (xAI) as the primary model and has full tool access including terminal, browser automation, file operations, subagent delegation, cron jobs, and persistent memory via Mnemosyne.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v5tixs/how_do_you_get_hermes_agent_to_actually_do_stuff/)

