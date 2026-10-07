---
title: "Hermes Charm - I built an ESP32-S3 pocket voice assistant with an e-paper display and Hermes task routing"
author: u/K8s-monk
date: 2026-10-07
score: 16
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wyyzyw/hermes_charm_i_built_an_esp32s3_pocket_voice/
flair: "Showcase"
---

# Hermes Charm - I built an ESP32-S3 pocket voice assistant with an e-paper display and Hermes task routing

**Posted by u/K8s-monk on 2026-10-07 · 16 points (100% upvoted) · 4 comments**

Meet Hermes Charm — my DIY ESP32-S3 pocket voice assistant. Think Muse Charm–style hardware, connected to a self-hosted Hermes agent that can use local AI models on your own computer/server. I built it to talk to an assistant without opening my phone.
To clarify the local AI part: the ESP32 handles microphone/speaker audio and an e-paper status display, not model inference. This version uses cloud-based Gemini Live for voice conversations; the separate Hermes backend can run locally and handle delegated tasks and completion notifications. It is not a fully offline device.
The firmware includes acoustic echo cancellation, battery status, light sleep and backup Wi-Fi. The engineering focus has been combining real-time audio with asynchronous agent tasks on a small battery-powered device. The backend can be replaced through a compatible API/adapter.
Short demo:
https://www.youtube.com/shorts/2kSqseHDv_8
Source and build/setup guides in video description
I would appreciate feedback on the audio/power tradeoffs or what you would improve in a device like this.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wyyzyw/hermes_charm_i_built_an_esp32s3_pocket_voice/)
