---
title: "I started running Hermes Agent inside Docker instead of giving it access to my whole machine"
author: u/viky_shetye
date: 2026-09-23
score: 45
comments: 21
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wnds9i/i_started_running_hermes_agent_inside_docker/
flair: "Guide — Tutorials, walkthroughs, repeatable how-tos"
---

# I started running Hermes Agent inside Docker instead of giving it access to my whole machine

**Posted by u/viky_shetye on 2026-09-23 · 45 points (90% upvoted) · 21 comments**

I’ve been using Hermes Agent for a while, and one thing that kept bothering me was how much access an autonomous agent can potentially have when it’s running directly on your machine.
Hermes can execute terminal commands, install packages, modify files, and work through multi-step tasks autonomously. Those capabilities are useful, but I don’t necessarily want an agent to have access to my entire home directory, SSH keys, personal files, etc.
So I put together a tutorial showing how I run
Hermes Agent inside a Docker container
with a much smaller trust boundary.
The setup is fairly simple:
Hermes runs completely inside the container
A dedicated
~/.hermes-docker
directory is mounted to
/opt/data
Config, sessions, memory, skills, profiles, etc. persist outside the disposable container
The rest of the host filesystem is
not
mounted
Hermes Gateway + Dashboard run through explicitly mapped ports
Hermes Desktop connects to the container through the remote gateway
One thing I want to emphasize:
Docker doesn’t magically make an AI agent secure.
An agent can still encounter malicious content or prompt injection and attempt something you didn’t intend. The useful part of containerization is limiting what the agent can reach if that happens.
My basic rule is:
Give the agent access to what it needs to do its job, not your entire computer.
Video:
https://youtu.be/inzB_q34QCA
Curious how others here are isolating autonomous agents. Docker, VM, dedicated VPS, sandbox, or just running them directly on the host?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wnds9i/i_started_running_hermes_agent_inside_docker/)
