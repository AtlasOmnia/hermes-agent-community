---
title: "PSA: OpenCode is emailing customers about a possible API key breach. If you saved provider keys in an opencode.ai workspace, rotate them"
author: u/Jonathan_Rivera
date: 2026-10-18
score: 9
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x8g56x/psa_opencode_is_emailing_customers_about_a/
flair: ""
---

# PSA: OpenCode is emailing customers about a possible API key breach. If you saved provider keys in an opencode.ai workspace, rotate them

**Posted by u/Jonathan_Rivera on 2026-10-18 · 9 points (100% upvoted) · 0 comments**

OpenCode customers are getting a breach notice, and it's credible enough to act on now.
What the notice says
The email has the subject "Action Required: Potential provider key breach." It says OpenCode found unauthorized access to a legacy system it was in the process of shutting down. Third-party provider keys (like OpenAI or Anthropic)
saved in your OpenCode workspace may have been exposed
.
They're asking customers to:
revoke and replace those keys in each provider's dashboard
update any apps that use them
check recent usage for anything unexpected
What's confirmed and what isn't
Multiple OpenCode users have posted the same notice in
r/opencode
(
thread
), and several report real unauthorized spend on Anthropic, OpenAI and Google keys they had saved in OpenCode (roughly $10 to $400 each). One user
reported misuse
hours
before
the notice went out.
OpenCode appears to have expired existing OpenCode API keys, and some users can't log in right now (
thread
).
As of this post, OpenCode hasn't published a statement or incident report beyond the email.
It's about keys stored in your
OpenCode cloud workspace
. The email doesn't say keys kept only on your own machine (local config or
auth.json
) are affected.
What to do
If you ever saved an OpenAI, Anthropic, Google, or other provider key in an opencode.ai workspace, revoke it and make a new one. Don't wait for an official statement; rotating costs nothing.
Check each provider's usage and billing pages for spending you don't recognize.
If Hermes, or anything else, uses one of those keys, put the new key in your config. Otherwise the old one will just start failing.
If you use OpenCode Zen/Go keys, expect to generate new ones; existing keys appear to have been expired.
Going forward:
give each tool its own key and set a spending cap on it. That way one leak hits one budget, not everything.
Source:
Matt Johansen on X

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x8g56x/psa_opencode_is_emailing_customers_about_a/)
