---
title: "I built a standalone Hermes Agent APK that runs a real Linux VM on Android — no root, no Termux"
author: u/romeo_florence
date: 2026-10-08
score: 7
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wzts6l/i_built_a_standalone_hermes_agent_apk_that_runs_a/
flair: "Discussion"
---

# I built a standalone Hermes Agent APK that runs a real Linux VM on Android — no root, no Termux

**Posted by u/romeo_florence on 2026-10-08 · 7 points (88% upvoted) · 4 comments**

I've been working on something I wanted to share with the Hermes community:
Hermes Agent running directly on Android inside a real embedded Linux VM — packaged into a single APK.
👉 GitHub:
https://github.com/romeomile/Hermes-Android-Linux
The idea is pretty simple:
Made by Hermes, for Hermes.
Instead of requiring Termux, root, a separate Linux environment, or another device, the APK contains the pieces needed to run Hermes locally on the phone.
What it does
The app contains:
🐧 An Alpine Linux guest
⚙️ QEMU running the Linux VM
🤖 Hermes Agent preinstalled inside the VM
💬 A native Android chat interface
🖥️ Access to a real Linux shell inside the guest
🔧 Hermes tools and userspace
💾 Persistent guest storage across restarts
🎙️ Voice support
🖼️ Images
📡 Streaming responses
⚡ Agent lifecycle controls
🔐 Device-generated authentication for the local APIs
The Android app communicates with Hermes through its local OpenAI-compatible API, while a separate control API handles the VM and agent lifecycle.
The important part
You don't need:
Root
Termux
UserLAnd
A PC/server
A separate Linux installation
You install the APK, launch it, and the Linux environment + Hermes engine start from the app itself.
It currently targets Android 8+ on arm64 devices. The VM needs roughly 2 GB of free RAM while running, and the bundled Linux environment takes additional storage.
But this is VERY much a testing release
I'm putting this out because I want other people to actually break it.
There are almost certainly bugs, device-specific problems, performance issues and things I haven't thought about yet.
So if you're interested in Hermes, Android, QEMU, embedded Linux, or just want to see how far you can push an AI agent from a phone:
Please test it.
Try different Android phones.
Try different Hermes configurations.
Try stressing the VM.
Try killing the app and restarting it.
Try using the terminal.
Try things I didn't think of.
And if something breaks, open an issue or submit a PR.
I'd genuinely like people to work on the bugs they find rather than just reporting them. Fork it, modify it, experiment with it, improve it.
Why I made it
I wanted Hermes to be something you could actually carry around as a self-contained environment rather than an Android client that depends on another machine.
The end goal is basically:
Phone → launch Hermes → Linux environment → agent → tools
with as little external infrastructure as possible.
It's still early, so I'm interested in seeing what the community does with it.
If you try it, I'd especially appreciate:
📱 Device model + Android version
🧠 RAM available
🚀 Whether the VM starts successfully
⏱️ Startup time
🐛 Anything that crashes or behaves strangely
🔥 Performance observations
💡 Features you'd like to see
🔧 Pull requests fixing things
And please don't be gentle with it. Find the bugs.
GitHub: Hermes-Android-Linux
I'd love to turn this from a personal experiment into something the Hermes community can actually use and improve.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wzts6l/i_built_a_standalone_hermes_agent_apk_that_runs_a/)
