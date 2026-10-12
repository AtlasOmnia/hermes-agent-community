---
title: "Hermes Agent ran code on my laptop through a tool I thought was just for browsing"
author: u/Wild_ApeCap
date: 2026-10-12
score: 8
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x35fh1/hermes_agent_ran_code_on_my_laptop_through_a_tool/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# Hermes Agent ran code on my laptop through a tool I thought was just for browsing

**Posted by u/Wild_ApeCap on 2026-10-12 · 8 points (100% upvoted) · 3 comments**

I was using Hermes Agent to work on a keyboard-lighting app. Its usual terminal ran inside Docker, so I thought commands touching my laptop’s hardware would have to be run by me.
Hermes also had a tool called
browser_exec
. It invoked it with
local=True
, which gave it a local host session. Inside that session, it used Python’s
subprocess.run()
to launch a test as my logged-in user:
python
subprocess.run(
["python", "/home/[user]/Documents/[shared-folder]/hardware_effect_test.py"],
cwd="/home/[user]/[project-checkout]",
env={..., "PYTHONPATH": "/home/[user]/[project-checkout]/src"},
)
The script connected to a local Unix
SOCK_SEQPACKET
broker socket my user could access. The broker handled the privileged keyboard-lighting operations, so Hermes didn’t need
sudo
or my password to change the physical keyboard lighting.
I hadn’t realized a browser-named tool could run Python on my host, and Hermes didn’t clearly tell me before using it to control hardware.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x35fh1/hermes_agent_ran_code_on_my_laptop_through_a_tool/)
