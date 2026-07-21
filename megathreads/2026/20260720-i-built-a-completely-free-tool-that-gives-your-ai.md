---
title: "I Built a completely free tool that gives your AI agent web for free (fetch + search + crawl + Screenshot) for completely free, no API keys, everything's Local but the performance matches the paid or free tier services."
author: u/Opening_Library9560
date: 2026-07-20
score: 84
comments: 15
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v1ok4c/i_built_a_completely_free_tool_that_gives_your_ai/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# I Built a completely free tool that gives your AI agent web for free (fetch + search + crawl + Screenshot) for completely free, no API keys, everything's Local but the performance matches the paid or free tier services.

**Posted by u/Opening_Library9560 on 2026-07-20 · 84 points (100% upvoted) · 15 comments**

Hermes ships with built-in `web_search` and `web_extract`, but they need a backend. The free DDGS option is search-only (no extract). Everything else needs an API key (Firecrawl, Tavily, Exa, Parallel) or self-hosting SearXNG in Docker. If you just want your agent to search the web and read pages without setting up any of that, you're stuck.

I built Hound as a drop-in MCP server that handles all of it. No API keys, no Docker, no config wizard. Just add it to your `~/.hermes/config.yaml` and your agent gets 6 web research tools.

# The setup (manual)

First install (only time you need pip directly):

    pip install hound-mcp[all]

Then add it to your `~/.hermes/config.yaml`:

    mcp_servers:
      hound:
        command: "hound"
        supports_parallel_tool_calls: true   # hound's tools are all read-only, safe to parallelize

That's it. Restart Hermes (or run `/reload-mcp` if you're in a session). The tools show up prefixed as `mcp_hound_web_fetch`, `mcp_hound_web_search`, etc. Hermes discovers them automatically.

# Or just tell your agent to do it

Paste this into your Hermes agent:

    Install and configure the hound-mcp MCP server for web research in my Hermes setup. Follow these steps exactly.
    
    1. Install hound: pip install hound-mcp[all]
    2. Find my Hermes config file. Find config.yaml in my Hermes home directory. Do NOT create a new config file. If you cannot find it, ask me where it is.
    3. READ the file. Do NOT overwrite it. You will add to it.
    4. Find the "mcp_servers" section. If it doesn't exist, create it at the top level.
    5. Under "mcp_servers", add a "hound" entry if it doesn't already exist:
       hound:
         command: "hound"
         supports_parallel_tool_calls: true
    6. Preserve ALL existing config. Only add the hound server entry.
    7. Write the file back as valid YAML.
    8. Tell me to restart Hermes or run /reload-mcp.

After install, use `hound -v` to check for updates, `hound -u` to update, `hound --doctor` to run a health check, and `hound --reinstall` for a full reinstall with all extras.

# What you get (6 tools)

**web\_fetch** \-- Fetches any URL, extracts clean markdown. Starts with HTTP, auto-escalates to a stealthy browser when it detects bot protection, JS shells, or rate limiting. PDFs get a section map with page ranges + auto-OCR for scanned docs. Dead links (404, 410, 451) return a clean error instead of serving the error page as content.

**web\_search** \-- 10 keyless search backends in parallel: DuckDuckGo, Brave, Mojeek, Yahoo, Yandex, Startpage, Google, Qwant, Wikipedia, Grokipedia. Results are neural-reranked with a local ONNX cross-encoder (not an API call) and scored by cross-backend consensus so you can see which results multiple engines agree on. Circuit breaker trips for 60s on any backend that blocks you; the other 9 keep working.

**web\_crawl** \-- Best-first same-domain walk. Sitemap mode maps an entire site in one fetch. Focus mode crawls only pages relevant to your query, not the whole site.

**web\_screenshot** \-- Anti-bot screenshot for multimodal models that need to see the page.

**cache\_clear** \-- Clears the fetch cache.

**hound\_version** \-- Version + update status.

In Hermes, these show up as `mcp_hound_web_fetch`, `mcp_hound_web_search`, etc. Hermes's built-in `web_search` and `web_extract` stay available alongside them, Though i recommend not have them configured or removing them, since hound works the best alone when there are no other web research tool confusing the Agent.

# How it handles the hard parts

* **Bot protection**: starts with plain HTTP. If it gets a 403/429/503, it escalates to a stealthy browser (Patchright with randomized fingerprint). Manages \~95% of the web. The few sites running DataDome or Cloudflare Turnstile will block it -- at that point Hound tells the agent to switch sources instead of pretending it got content.
* **Error honesty**: any 4xx/5xx sets the error field. Before v10.4.0, a 404 error page would flow through with `error=""` and the agent could mistake the error page HTML for real data. Now it's flagged and the content is replaced with the error message. The agent gets `Page doesn't exist (404)` instead of 5KB of error-page HTML.
* **No API keys, ever**: search is 10 backends scraping in parallel (no keyless general search API exists in 2026 -- Bing Search API died summer 2025, Brave free tier died Feb 2026). Extraction is local (trafilatura + lxml + PDF OCR). The neural reranker is a local ONNX model, not an API call.
* **Token cost**: 2,746 tokens for all 6 tools + instructions combined. The tool definitions are tight.

# The [all] install is ~100MB

The `[all]` extra pulls in onnxruntime + tokenizers + rapidocr (for the neural reranker and PDF OCR). You can install without it (`pip install hound-mcp`) and fetch + crawl + search still work, just no neural reranking or PDF OCR. Full install is the recommended path.

# Links

GitHub: [https://github.com/dondai1234/master-fetch](https://reddit.comhttps://github.com/dondai1234/master-fetch) (Star the Repo if you like it 😄 )

PyPI: hound-mcp

MIT licensed. If you try it, let me know what breaks.

UPVOTE THIS TO HELP IT REACH MORE PEOPLE 🔥

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v1ok4c/i_built_a_completely_free_tool_that_gives_your_ai/)

