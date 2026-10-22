# How to Run Hermes Agent From Your Phone: Telegram vs Discord vs Matrix vs Mobile Apps (What 100+ Users Said)

> **r/hermesagent** — 115,000+ members building with Hermes Agent.
> [Join the community →](https://reddit.com/r/hermesagent) | [Official Docs](https://hermes-agent.nousresearch.com/docs)

**Meta Description:** Which messaging platform or mobile app should you use to operate Hermes Agent remotely? A comparison of Telegram, Discord, Matrix, Slack, WhatsApp, Signal and community mobile apps (Cadu, Hermex, Conduit, Hermes Relay), based on 97 answers from r/hermesagent.

---

## Table of Contents

- [Where This Comes From](#where-this-comes-from)
- [The Short Answer](#the-short-answer)
- [What People Use](#what-people-use)
- [Comparison Table](#comparison-table)
- [Messaging Platforms](#messaging-platforms)
  - [Telegram](#telegram)
  - [Discord](#discord)
  - [Matrix (self-hosted)](#matrix-self-hosted)
  - [Slack](#slack)
  - [WhatsApp, Signal, iMessage and Others](#whatsapp-signal-imessage-and-others)
- [Dedicated Mobile Apps and Web UIs](#dedicated-mobile-apps-and-web-uis)
- [Reaching Your Server Safely: Tailscale and Friends](#reaching-your-server-safely-tailscale-and-friends)
- [Tips From People Who Run It Daily](#tips-from-people-who-run-it-daily)
- [How to Choose](#how-to-choose)
- [FAQ](#faq)
- [Sources](#sources)

---

## Where This Comes From

In October 2026, r/hermesagent asked: **["How are you managing your Hermes agents from your phone?"](https://www.reddit.com/r/hermesagent/comments/1xavwj1/how_are_you_managing_your_hermes_agents_from_your/)** The thread collected 139 comments, including **97 top-level answers** describing what people actually use. This guide summarizes those answers and links to the official setup docs for each option.

Counts below are mentions in top-level answers (one person can mention more than one tool). They are a community snapshot, not a census or an endorsement.

---

## The Short Answer

- **Most people start with Telegram.** It was the most mentioned option by a wide margin, and it is the quickest to set up.
- **Discord is the most common upgrade**, mainly for its threads and per-agent channels.
- **Privacy-focused users self-host Matrix** and reach it over Tailscale.
- **A growing group uses a dedicated Hermes app** (Hermex, Conduit, Cadu, Hermes Relay) or a web UI, usually over Tailscale, for a full chat interface instead of a "message in a bottle."
- Whatever you pick, **keep your Hermes server off the open internet** and reach it through a private network.

---

## What People Use

| Option | Mentions (of 97 answers) |
|---|---|
| Telegram | 31 |
| Discord | 15 |
| Hermex (mobile app) | 11 |
| Web UI / Open WebUI / dashboard | 7 |
| Conduit (iOS app) | 7 |
| SSH / terminal (incl. mosh, Termux) | 7 |
| Matrix (self-hosted) | 6 |
| Hermes Relay (Android app) | 5 |
| Built their own app | 5 |
| Cadu (mobile app) | 3 |
| WhatsApp | 3 |
| Slack | 2 |
| iMessage (via BlueBubbles) | 2 |
| Signal, Mattermost, Herald, Redde | 1–2 each |

**Tailscale** came up in 18 answers as the way people reach their Hermes server from a phone.

---

## Comparison Table

| | Setup effort | Organization | Privacy | Best for |
|---|---|---|---|---|
| **Telegram** | Lowest | One bot per agent; topics/threads | Messages pass through Telegram | Getting started, approvals, cron notifications |
| **Discord** | Low | Channels per agent/project, auto-threads | Messages pass through Discord | Several agents or projects, team-style setups |
| **Matrix** | High (you host a server) | Rooms | You control the server | Privacy, off-cloud setups |
| **Slack** | Low if you already use it | Channels per repo/project, @-mentions between agents | Messages pass through Slack | Work setups, agent-to-agent review |
| **Dedicated app / web UI** | Medium (needs a private network) | Full session view, profiles, kanban (varies by app) | Direct to your server | A real chat interface on your phone |

---

## Messaging Platforms

### Telegram

The most common choice. People like that each agent can have its own bot so conversations don't mix, and that approvals and cron results arrive like messages from a colleague.

- **Community tip:** turn on **threaded mode / topics** (set in BotFather) so each conversation gets its own thread instead of one long chat.
- Several people use Telegram only for **notifications and quick tasks**, and something else for longer work.
- The main complaint is privacy: messages pass through Telegram's servers.

Setup: [Official Telegram docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram) · [Community Telegram gateway guide](telegram-gateway-setup.md)

### Discord

The most common "I moved from Telegram" destination. Users set up **one channel per agent or project**, and messages automatically become threads that keep each session contained. Agents can post into each other's channels or be @-mentioned in a shared channel.

- "Even if you hate Discord, for this purpose it's great" was a recurring theme.
- One user runs a **second recovery agent** on an older version, started by the main agent during updates, so something can still fix things from Discord if an update breaks.

Setup: [Official Discord docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)

### Matrix (self-hosted)

The privacy pick. Users run their own server (Continuwuity, Tuwunel or Dendrite were mentioned), use Element or Element X on the phone, and keep everything **off the public internet behind Tailscale or NetBird**. One user described Telegram as feeling like having their "[backside] out on the internet" by comparison.

- Community guides for hosting your own Matrix server: [using Tailscale](https://www.reddit.com/r/hermesagent/comments/1v8zslq/guide_host_your_own_private_matrix_server/) · [using a reverse proxy](https://www.reddit.com/r/hermesagent/comments/1vg7rte/guide_host_your_own_private_matrix_server_using/)

Setup: [Official Matrix docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix)

### Slack

Recommended by people who already use Slack for work: **one channel per repo**, multiple agents in a channel, and @-mentions make agent-to-agent review easy. The free tier was reported to be enough (the main limit is 90-day message history).

Setup: [Official Slack docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack)

### WhatsApp, Signal, iMessage and Others

- **WhatsApp:** a few people use it because it's already on their phone; others avoid it for privacy reasons. [Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)
- **Signal:** used for a main agent and quick "offload a thought" messages; one early adopter said it didn't gel for them. [Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/signal)
- **iMessage:** via BlueBubbles. [Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
- **Mattermost:** self-hosted and good for organizing key projects; slash commands didn't work for one user, but approvals did. [Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost)

The official docs list many more gateways (email, SMS, Teams, SimpleX and others): [Messaging docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)

---

## Dedicated Mobile Apps and Web UIs

Messaging apps felt "too message-in-a-bottle" for some users: you send a request and get little visibility into what the agent is doing. These options give you a full interface to your own Hermes server instead. All are community projects unless noted; most need a private network such as Tailscale to reach your server.

| App | Platform | What people said |
|---|---|---|
| **Cadu** ([cadu.bot](https://cadu.bot)) | iOS (Android in progress) | Reported in the thread as the base for the forthcoming official Hermes mobile app; supports sessions and bots. |
| **Hermex** | iOS | Access to all profiles, bots and the kanban board; a few users hit a Python-version issue after updates that Hermes itself fixed. |
| **Conduit** ([hermesconduit.app](https://hermesconduit.app)) | iOS | Praised; one user runs it through Cloudflare so no ports are open. |
| **Hermes Relay** ([GitHub](https://github.com/Codename-11/hermes-relay)) | Android (Google Play) | Favorite of users avoiding Telegram for privacy; used over Tailscale or WireGuard. |
| **Hermes Web UI** ([GitHub](https://github.com/nesquena/hermes-webui)) + [hermes-android](https://github.com/hermes-webui/hermes-android) | Any browser, Android | Full UI on any device; continue where you left off. |
| **Open WebUI** | Any browser | Works through the Hermes API. [Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui) |
| **Herald**, **Redde**, **Hermes Mobile**, **bighelp**, **Kite**, **Personae** | Various | Mentioned by individual users; several were built by the commenters themselves. |

There is also an official experimental **Relay** gateway: [Relay docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/relay).

Five people simply **built their own app** with Hermes or Claude, including a native iOS app, an Android launcher with a built-in chat, and an app that pipes audio to bone-conduction headphones.

---

## Reaching Your Server Safely: Tailscale and Friends

The most repeated advice in the thread: **don't expose your Hermes server to the public internet.** People reach it with:

- **Tailscale** (18 mentions): phone and server on the same private network; works with web UIs, apps and SSH.
- **WireGuard** or **NetBird**: self-managed alternatives.
- **Cloudflare Tunnel**: no open ports on your router.
- **SSH / mosh over Tailscale**: for running bigger tasks in the terminal UI from a phone or tablet (Termux on Android, ServerBox or Moshi on iOS).

---

## Tips From People Who Run It Daily

- **One bot or channel per agent** so conversations don't mix.
- **Let approvals come to you:** risky commands and outbound messages ping your phone for a yes/no.
- **Send a short daily digest** (what ran, what failed, what's waiting) instead of constant updates, or your phone becomes noise.
- **Keep a separate recovery agent** that can fix things if an update breaks your main one.
- **Use Telegram for notifications and a fuller app for real work** if one tool doesn't cover both.

---

## How to Choose

1. **Just want to try it?** Telegram. Ten minutes, and you get approvals and cron results on your phone.
2. **Running several agents or projects?** Discord or Slack, with a channel per agent or project.
3. **Care most about privacy?** Self-hosted Matrix, or a dedicated app over Tailscale.
4. **Want a real chat interface, not messages?** Hermex or Conduit (iOS), Hermes Relay (Android), or Hermes Web UI, over Tailscale.

---

## FAQ

**What is the most popular way to run Hermes Agent from a phone?**
Telegram, by a wide margin in the October 2026 r/hermesagent thread, followed by Discord.

**Is there an official Hermes mobile app?**
Not yet as of October 2026. Commenters reported that the developer of Cadu joined Nous Research and that Cadu is the base for a forthcoming official app.

**Do I need to open ports on my router?**
No. Most users reach their server through Tailscale, WireGuard, NetBird or a Cloudflare Tunnel instead.

**Can I use more than one platform?**
Yes. A common setup is Telegram for notifications and quick tasks, plus a web UI or app for longer sessions.

---

## Sources

- Reddit thread: [How are you managing your Hermes agents from your phone?](https://www.reddit.com/r/hermesagent/comments/1xavwj1/how_are_you_managing_your_hermes_agents_from_your/) (r/hermesagent, October 20, 2026; 139 comments, 97 top-level answers)
- [Hermes Agent messaging docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)

*Community summary, not official Nous Research documentation. Third-party apps are listed as reported by users and are not reviewed or endorsed.*
