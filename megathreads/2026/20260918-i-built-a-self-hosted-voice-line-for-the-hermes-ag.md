---
title: "I built a self hosted voice line for the Hermes agent, is it worth putting on github?"
author: u/giulioc84
date: 2026-09-18
score: 6
comments: 3
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wj40l1/i_built_a_self_hosted_voice_line_for_the_hermes/
flair: "Showcase — Projects, tools, builds, demos"
---

# I built a self hosted voice line for the Hermes agent, is it worth putting on github?

**Posted by u/giulioc84 on 2026-09-18 · 6 points (87% upvoted) · 3 comments**

Ciao everyone,
since a couple of nights I've been working on giving a real phone number to Hermes, the self hosted assistant agent I run. Basically humans can call (or Hermes can initiate a call) an actual number and you just talk to it, normal speech, full duplex, quite low latency, and it answers, takes messages, and after the call it writes everything into the Hermes' workspace, Hermes sends me a short summary via Telegram with potential actions asking for permission to execute. I can ofc query Hermes on telegram re full transcripts, calls made, whatever.
Works well, just ironing out some bugs and tuning persona / hooks / triggers etc. etc. but so far it worked well to reschedule some appointments, check availability of items at 5-6 shops...
I know there are some (paid) services out there, but I thought the pricing was not ok and I could just pay directly couple of providers and make savings. Also I did not want to use readymade all-in-one services due to costs and... just for fun (I knew little about SIP / audio agents / etc.). So my drivers were: costs, security, configurability.
The setup works like this. A small VPS runs Asterisk, which handles the SIP/RTP coming from the carrier (the one I wired, the cheapest available in my country hahah!). On the same VPS a bridge service connects the call audio to a realtime speech model over a websocket. The bridge is provider agnostic behind an adapter layer, so it currently runs on OpenAI's Realtime API (using gpt-live-1), with adapters also written for Gemini (now testing gemini 3.8 live), ElevenLabs, Deepgram and Ultravox etc., switchable with a single flag.
The bridge itself holds no intelligence. When a call needs real knowledge, it calls back to my home server over a private mesh network (wired meshnet of nordvpn, but could be tailscale), through a narrow HTTP shim that is bearer gated and rate limited and exposes only two verbs, a "brief" at the start of the call and an "ask" during it. That shim passes the query to Hermes, which has the full memory, tools and persona. When the call ends, the box fires HMAC signed webhooks to the agent, which runs a job to persist the conversation and ping me on Telegram.
The isolation was something i cared about as I do not want my home server exposed anywhere. The audio never touches my home box, it stays on the VPS, and the home side only ever sees text. The agent's own API is never exposed to the public VPS either, the only surface it presents to the telephony side is those two verbs and nothing more. Also added and enforced allowlists etc. so us humans have to authorize explictly numbers to be called or call won't start.
Right now I'm building a dashboard for it (choose the voice provider and the voice, the mode, the number routing, and so on) with visualizations (e.g. costs, minutes, whatever), testing everything end to end and adjusting things as they come up. I am also looking into ways to have the voice agent trigger keypad sounds (I do not know how they are called in eng!) to go through auto responders.
So my question for you guys, do you think there is interest for something like this as open source?
Honestly I am not sure if its too niche or not and don't want to spend some additional million tokens on security reviews / bugfixing / polishing if no one uses this... also, not going to spend time to add voip providers , features etc. as I do not have much free time - but happy to "donate" to the community what I built if it can be useful.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wj40l1/i_built_a_self_hosted_voice_line_for_the_hermes/)
