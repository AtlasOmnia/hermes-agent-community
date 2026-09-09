---
title: "TalkToHermes: Native SwiftUI voice client for Hermes Agent — private, self-hosted STT/TTS with iPhone & iPad push-to-talk."
author: u/AF360
date: 2026-09-09
score: 11
comments: 2
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wagsuz/talktohermes_native_swiftui_voice_client_for/
flair: "Showcase — Projects, tools, builds, demos"
---

# TalkToHermes: Native SwiftUI voice client for Hermes Agent — private, self-hosted STT/TTS with iPhone & iPad push-to-talk.

**Posted by u/AF360 on 2026-09-09 · 11 points (86% upvoted) · 2 comments**

TalkToHermes turns your self-hosted Hermes Agent into a native iPhone/iPad voice assistant — while STT, TTS and voice data can remain entirely on infrastructure you control.
I originally built it because I wanted a simple way to talk to my Hermes Agent from an iPhone without turning the whole voice path into another cloud service.
The iOS client is written natively in SwiftUI and uses push-to-talk rather than an always-listening microphone. It connects to a small per-user TalkToHermes Voice Bridge, which in turn talks to the official Hermes sessions/runs API.
Some of the things it currently supports:
Native iPhone/iPad SwiftUI client
Push-to-talk voice interaction
Full conversation visible on screen
Live Hermes approvals and cancellation
Keychain-backed authentication
Separate Hermes instances/users with isolated bridge processes
Configurable STT and TTS provider chains with automatic fallback
Local Faster-Whisper / MLX-Whisper / Piper / Wyoming providers
Optional OmniVoice for cloned voices
English and German UI, with UI and spoken language independently selectable
Handover content summary to Telegram session
My own setup, for example, uses a high-quality STT/TTS service as the primary path, local network services as fallback, and finally completely local STT/TTS on the Hermes host as the last resort.
The important part for me was that speech recordings and transcripts don't have to leave my own infrastructure. The voice path itself remains local even when Hermes uses a cloud-hosted LLM: audio files stay on your own infrastructure, while only the transcribed text is sent to the model provider. If Hermes also uses a local LLM such as Ollama, the entire interaction can remain local end-to-end.
The architecture is roughly:
iPhone/iPad
→ private HTTPS endpoint
→ TalkToHermes Voice Bridge
→ Hermes Agent
→ configurable local/private STT + TTS providers
It is
not an all-in-one standalone app
: you need a running Hermes Agent, the bridge component and your own HTTPS endpoint. The repository contains the iOS client, bridge/backend code, deployment documentation, API contract, security notes and examples for the voice services.
The project is MIT licensed.
I'd be interested to hear how other Hermes users are approaching voice interaction — especially people running local STT/TTS stacks. Feedback, testing and ideas are very welcome.
GitHub Repository TalkToHermes

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wagsuz/talktohermes_native_swiftui_voice_client_for/)
