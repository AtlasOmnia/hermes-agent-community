---
title: "Teknium dropped an X post today laying out where Hermes' architecture is headed, and it's a bigger shift than the opening line makes it sound."
author: u/Jonathan_Rivera
date: 2026-09-18
score: 110
comments: 27
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wj7x11/teknium_dropped_an_x_post_today_laying_out_where/
flair: "News — Official Releases, announcements, major changes"
---

# Teknium dropped an X post today laying out where Hermes' architecture is headed, and it's a bigger shift than the opening line makes it sound.

**Posted by u/Jonathan_Rivera on 2026-09-18 · 110 points (93% upvoted) · 27 comments**

What changed:
• Bundled memory providers are getting pulled from core. They'll be maintained by their own creators in their own org repos and distributed through the plugins marketplace instead of shipping with every Hermes install.
• This is a test run, not a one-off — the plan is to keep pulling integrations out of the core codebase into maintainer-owned repos going forward. Stated reasoning: less bloat, less user confusion, and fewer people ending up off the "happy path"without realizing it.
• The plugins catalog already existed (tool providers, memory systems, etc. could already plug in) — the missing piece was discoverability. That's what's solved now, which is what's unlocking this move.
• First real-world case: Honcho (@honchodotdev) and Mem0 (@mem0ai). Nous is working with them directly (in Discord) to figure out how to auto-migrate existing users to the independent plugin versions with no interruption to their current setup.This migration model is what they'll reuse as more bundled integrations get shed.
The clarification that had to happen:
The "more like Pi, less like OpenClaw" opener got read by some as Hermes pivoting away from being a personal assistant toward a coding agent. Teknium clarified: that's not it - this is strictly about what ships bundled in core vs. what lives as a plugin. Leaner core, more plugins. Hermes is still aimed at being the personal assistant agent, not a coding agent.
Why it matters if you're running Hermes today:
If you're on one of the bundled memory providers, the stated goal is an automatic migration path to the plugin version, not removal-without-notice — worth watching how that actually lands when it ships. It's also a signal: expect more bundled integrations to follow this same core→plugin path over time.
Source (thread):
https://x.com/Teknium/status/2100645382552428963

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wj7x11/teknium_dropped_an_x_post_today_laying_out_where/)
