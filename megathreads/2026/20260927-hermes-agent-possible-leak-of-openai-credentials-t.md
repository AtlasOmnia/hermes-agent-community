---
title: "Hermes Agent possible leak of OpenAI credentials to OpenRouter"
author: u/Undefinied
date: 2026-09-27
score: 17
comments: 10
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wqlvnu/hermes_agent_possible_leak_of_openai_credentials/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# Hermes Agent possible leak of OpenAI credentials to OpenRouter

**Posted by u/Undefinied on 2026-09-27 · 17 points (79% upvoted) · 10 comments**

There’s something concerning in Hermes’s credential handling.
If Hermes selects OpenRouter, doesn’t have an OpenRouter key, and
OPENAI_BASE_URL
is unset, it can fall back to sending your
OPENAI_API_KEY
to OpenRouter. Auto-detection can also select OpenRouter simply because an OpenAI key is present, when no provider is pinned.
Here’s the fallback code (
https://github.com/NousResearch/hermes-agent/blob/3094b5d0aa/hermes_cli/runtime_provider_backends.py#L159-L165
), and here’s the auto-detection (
https://github.com/NousResearch/hermes-agent/blob/3094b5d0aa/hermes_cli/auth.py#L1439-L1444
).
What bothers me is that this behavior is explicitly preserved. The tests (
https://github.com/NousResearch/hermes-agent/blob/3094b5d0aa/tests/hermes_cli/test_runtime_provider_resolution.py#L594-L643
) describe an earlier incident where OpenAI keys were sent to OpenRouter, then separately assert that the fallback should still work when an OpenRouter key is missing.
A subsequent fix (
https://github.com/NousResearch/hermes-agent/commit/da031c31c12b18494ea7c8cb0e433e7f9c604887
) narrowed the circumstances but kept the fallback.
The stated explanation is legacy compatibility. Maybe that’s the whole story. But it’s fair to ask whether favoring OpenRouter was a deliberate product decision and this credential exposure was an accepted consequence. If there’s a commercial relationship between Nous and OpenRouter, that question deserves a clear answer.
Why should a variable named
OPENAI_API_KEY
authorize sending that secret to another company without an explicit choice from the user?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wqlvnu/hermes_agent_possible_leak_of_openai_credentials/)
