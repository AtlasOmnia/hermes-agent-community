---
title: "Attempts to avoid Hermes becoming a security nightmare"
author: u/syntx444
date: 2026-10-16
score: 36
comments: 30
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x6qe23/attempts_to_avoid_hermes_becoming_a_security/
flair: "Workflow — Daily habits, multi-agent setups, best practices"
---

# Attempts to avoid Hermes becoming a security nightmare

**Posted by u/syntx444 on 2026-10-16 · 36 points (95% upvoted) · 30 comments**

I've been trying to harden my local Hermes installation on my daily driver Linux PC as follows:
Dedicated user account
. Hermes runs as a "hermes" user with its home at /home/hermes, separate from my personal user account. The hermes user account has no sudo rights.
Shared workspace, not shared home
. Any files created by or needed by the agent goes to /home/hermes/workspace, owned by a "hermes" group that both accounts (my personal user and the hermes user) belong to. It uses the setgid bit and a default ACL so new files stay accessible to both.
Manual approvals
. I've set command approval to manual so that I can review every prompt.
Gateway disabled
. For now, I don't need to use Telegram etc. with Hermes, especially as I've only recently started kicking the tyres on this thing and want to first familiarise myself with desktop use. So I stopped and disabled the systemd unit for the messaging gateway.
TUI instead of desktop app
Due to the restrictions I've placed on the hermes user, running `hermes desktop` successfully installed the app but failed to launch due to the user not having access to the X session. Claude has helped by pointing out some of the risks involved and it pointed out that running the desktop app as the hermes account would let the agent see and inject input into my X session, which was discouraged, so I'm now just using the TUI instead. I do like the TUI but am also gutted I can't find a way to securely use the desktop app as a locked down user.
Residual risk
: Potential for prompt injection. Even with all this, the agent still acts on text it reads. If it fetches a web page or processes a document with hidden instructions, it may follow them, and the approval prompt (approval set to manual) is only as good as my attention and experience when reviewing it.
I'd appreciate thoughts and suggestions related to the above setup.
What are some effective methods for reducing the prompt injection risk?
I'd also be interested to know if anyone got the desktop app working safely somehow. For example, Claude suggested I try a nested X server like Xephyr, rather than sharing the main display.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x6qe23/attempts_to_avoid_hermes_becoming_a_security/)
