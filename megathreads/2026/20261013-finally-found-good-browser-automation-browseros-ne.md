---
title: "Finally found good browser automation: BrowserOS neo"
author: u/freshbeantacos
date: 2026-10-13
score: 25
comments: 6
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x421vm/finally_found_good_browser_automation_browseros/
flair: "Showcase — Projects, tools, builds, demos"
---

# Finally found good browser automation: BrowserOS neo

**Posted by u/freshbeantacos on 2026-10-13 · 25 points (96% upvoted) · 6 comments**

Took some time to get my web and browser agent capabilities and wanted to share what's been working for me:
Forms/Human in the loop: BrowserOS neo
Concrete jobs it's done for me: filling out travel/booking forms (yes, family paperwork — a form-filling agent earns its keep fast), reading JS-rendered pages that come back empty through a raw fetch, checking a checkout flow visually, anything that needs actual clicking.
BrowserOS neo
is an open-source (AGPL-3.0) Chromium fork built for agents instead of humans, and it shows up as an MCP server. What makes it work for me:
It uses my real, logged-in browser.
Form filling on sites behind logins just works — no cookie wrangling, no fresh-profile walls, no "please enable JavaScript" pages.
It's a
real
browser, so the nasty stuff — SPA re-renders, consent modals, finicky date pickers — behaves like it does when I click it myself.
The agent reads the page as an accessibility tree with element refs, so even my 2.6-bit quant handles browser loops reliably.
Before this I tried
BrowserClaw
(the browser-tools-mcp-based personal agent) and it didn't work well for me — never stuck. (Confusingly, BrowserOS neo itself used to be called "BrowserClaw" before they renamed — completely different project. Search before you cite.)
The headless side: web-search-plus
When I don't need a browser in the foreground — searches, facts, prices, reading docs — I use Hermes'
web-search-plus
plugin instead. Search + extract, no window, fast and cheap.
One reminder:
don't run it without a search API key.
The no-key fallback scrapes Brave's HTML and gets rate-limited almost immediately. Put a real key in your
.env
. I have two set up:
Serper
— Google results API, 2,500 free queries/month. My workhorse.
Tavily
— search built for LLM agents, generous free tier. Set as my default.
That's the division of labor: search-plus
finds
things, neo
touches
things.
The model doing all of it
Everything above runs on
Qwen3.8-Flash-Next Sushi 2.6bpw
served locally by the
sushi
engine —  on my 96GB Ultra, which matters here because a browser agent is a
loop
of tool calls: slow decode = sluggish clicks. Tool calling has been rock solid through long multi-step browser sessions. If you're on 64GB or less, I'd go with
Ornith-1.5-35B-A3B (8-bit)
— I ran that for before this and it drives browser tools fine too.
Also made a post earlier on my non-coding Mac Ultra 96gb setup in case interested:
https://www.reddit.com/r/LocalLLM/comments/1wxeqcr/local_ai_on_a_96gb_mac_m5_studio_for_noncoding/

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x421vm/finally_found_good_browser_automation_browseros/)
