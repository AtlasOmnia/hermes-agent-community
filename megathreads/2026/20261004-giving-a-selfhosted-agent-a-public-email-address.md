---
title: "Giving a self-hosted agent a public email address"
author: u/cryme_ariver
date: 2026-10-04
score: 9
comments: 11
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wwk2l9/giving_a_selfhosted_agent_a_public_email_address/
flair: "INTEGRATIONS — App connections, webhooks, API workflows"
---

# Giving a self-hosted agent a public email address

**Posted by u/cryme_ariver on 2026-10-04 · 9 points (84% upvoted) · 11 comments**

Before you continue: Please don’t go all elitist on my ass. I am a mere tech enthusiast that can use the help of an agent in daily tasks. Your participation to this thread is absolutely optional ^^
I run a self-hosted agent (Hermes Agent in Docker) with its own mailbox and its own account on my personal domain. It reads mail over IMAP and replies in-thread. The address is meant to be its front door: it emails suppliers and services, and I'd like anyone who writes back to get an answer no safe-sender list.
Today only two addresses get through; everything else is dropped silently. Turning that off is one setting. What I'm unsure about is what should carry the safety instead with any sender allowed, the sender can't be verified the same way, and mail is untrusted text arriving at an agent that has shell access, files and accounts.
I've read about quarantining stranger mail behind a tool-less reader, approval loops, rate limits, treating mail as a queue rather than a trigger. I'd rather hear how people here actually run it.
I have a strong preference on using my own domain, so I am trying to find solutions around this instead of agent mail services.
If you've given an agent a public inbox: what did you build, what broke, what would you change? If you decided against it, what stopped you? Where do you draw the line between convenience and control?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wwk2l9/giving_a_selfhosted_agent_a_public_email_address/)
