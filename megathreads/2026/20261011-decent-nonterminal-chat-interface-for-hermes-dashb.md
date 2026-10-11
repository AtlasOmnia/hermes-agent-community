---
title: "Decent (non-terminal) chat interface for Hermes? (dashboard, desktop, webui all let me down in different ways)"
author: u/Ori_553
date: 2026-10-11
score: 15
comments: 47
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x2q29o/decent_nonterminal_chat_interface_for_hermes/
flair: "Discussion"
---

# Decent (non-terminal) chat interface for Hermes? (dashboard, desktop, webui all let me down in different ways)

**Posted by u/Ori_553 on 2026-10-11 · 15 points (80% upvoted) · 47 comments**

I’ve been trying Hermes agent for a few days and the agent itself is great, but I can’t find a decent non-terminal interface to actually work with it day to day, so I’m hoping I’m just missing something.
What I tried:
-
Hermes Desktop app
: Curious design decision: It's an actual App, not a web UI you open in a browser, so if it’s running somewhere without a display you can reach (headless server, sandboxed container, etc.), you can’t use it unless you resort to workarounds like forwarding the display out of the container (X11/Wayland sockets, VNC, that kind of thing). No Linux AppImage, it’s install-on-your-host or GTFO.
-
Open WebUI
: Functions but doesn't show anything other than text, not even context window usage, no tool calls, nothing. You have no idea what is happening under the hood.
-
Hermes dashboard
(the official admin panel) -> It's the opposite extreme, the dashboard itself seems to have all you'd need, but the chat section is a terminal loaded in the web dashboard (xterm.js terminal-chat). I'm sure that competent terminal users get more done from terminal, but I personally see no point in using terminals when I have a big screen with colors and reasonably good mouse skills, can't even copy-paste things in and out of terminal normally (the usual Ctrl+C/Ctrl+V)
-
hermes-webui
: It's exactly the UI I wanted, it has schedules, kanban, UI chat that actually shows tool calls, context, et-cetera, but it's heavily bugged/unusable, I swear messages I send sometimes get lost, scroll position jumps by itself, it freezes as if I have 20 MB RAM, and other random issues.
(In case it's useful, my setup: Strata for local LLM inference (running as pod), Host OS is Fedora 44 , I run everything as pods/vms that i can easily delete to keep the host OS free from clutter, so my random experiments/projects don't keep accumulating in random directories in the host OS.)
This is what I tried. Am I missing something, or is this just the current state of Hermes UIs?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x2q29o/decent_nonterminal_chat_interface_for_hermes/)
