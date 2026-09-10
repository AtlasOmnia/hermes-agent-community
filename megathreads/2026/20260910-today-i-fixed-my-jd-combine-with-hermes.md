---
title: "Today I fixed my JD combine with Hermes"
author: u/flairtestuser123
date: 2026-09-10
score: 14
comments: 6
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wbz4ph/today_i_fixed_my_jd_combine_with_hermes/
flair: "Use Case — Real tasks, business & personal"
---

# Today I fixed my JD combine with Hermes

**Posted by u/flairtestuser123 on 2026-09-10 · 14 points (93% upvoted) · 6 comments**

So we were having an issue with the electronics on this combine for last several days.  Paid a Deere mechanic to come out, which we have done like twice in the last decade, and he couldn't figure it out.
I worked with Hermes running Astra, we build a test suite for CanBUS that used a PCan USB adapter to read CanBUS messages and a Rigol 4-channel oscilloscope that I barely know how to run but has a network adapter on it.
The test suite would run while I communicated with the Hermes instance on my laptop, it seemed to be able to figure out the CanBUS messages and would also compare the electronic traces it pulled from the scope against what it was seeing for messages.  We would discuss the diagnostic procedure and pull controllers and compare results against traces that I'd pulled from another working combine I have.
We found two problematic controllers, one that was pulling the CanH line low randomly (the Rigol caught that) and one that would hold the bus hostage and messages would drop off a cliff (the Pcan found that).
Now I'm bus-pirating the combine to build my own yield monitor since I'm fairly confident I can have Hermes build me something that will pull the yield data off of CanBUS while it takes in GPS messages from my RTK module and base station, something I've wanted for years but didn't want to pay $20k to put in.
JD:0
Hermes:1

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wbz4ph/today_i_fixed_my_jd_combine_with_hermes/)
