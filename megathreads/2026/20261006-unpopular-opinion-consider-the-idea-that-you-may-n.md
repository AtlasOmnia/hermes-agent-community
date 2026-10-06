---
title: "Unpopular opinion: Consider the idea that you may not need an additional memory provider (yet)"
author: u/trashbytes
date: 2026-10-06
score: 27
comments: 4
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wy78uh/unpopular_opinion_consider_the_idea_that_you_may/
flair: "MEMORY & Context — Providers, context window, forgetting issues"
---

# Unpopular opinion: Consider the idea that you may not need an additional memory provider (yet)

**Posted by u/trashbytes on 2026-10-06 · 27 points (86% upvoted) · 4 comments**

There's a lot of talk going on about memory providers and I'd like to chip in to take the weight off the newcomers in this sub especially: You may not need an additional memory provider and that's okay! Don't go down a rabbit hole (unless it's fun, of course) if all you need is a simple agent that does work for you instead of simulating a friend.
For actual project-scoped engineering where every task has a clear boundary, heavy memory layers are often counterproductive. Auto-extracted memories inevitably pick up temporary edge cases, outdated debugging attempts, or one-off workarounds and treat them as permanent facts. Codebases and requirements move fast, and having an external memory provider feed your model outdated assumptions from three weeks ago can create problems you may not even pick up on until millions of tokens as well as minutes or hours of your time are already wasted.
Here's my philosophy:
Instead of hoping a model "memorizes" how your project works, put it in a carefully written and linted
AGENTS.md
file inside that projects folder. The agent will pick it up if and when it needs to know about that automatically. And I really mean it when I say carefully written and linted! In the beginning my agents constantly added anecdotal fluff. Something that happend on date x because of reason y doesn't belong. Neither does code logic or how a test works. An agent doesn't care if it's reading .md or .js, but duplicates just mean more potential errors (e.g. changes aren't in sync, where it edited the script but not the .md and they contradict) and token bloat. It should contain local conventions, folder structures, and rules locked down per project with zero cross-contamination.
Then I feel like people tend to forget that skills exist. Things like how to call an API, handle a framework edge case, or run a deployment belong in a dedicated skill or reference doc, not in memory. An agent doesn't need to memorize a workflow if that workflow is explicitly part of a skillset. This will also make sure that the agent will reliably pick it up if and when it need to.
Now I have plenty of headroom in both MEMORY.md as well as USER.md and it reduced the amount of outdated info to what feels like zero.
But this doesn't cover everything, I know that. This is a colleague, not a friend. A workhorse, not a pet. But it's reliable! And that's what matters to me and this may or may not be exactly what you're looking for.
All of the personal knowledge is stored in an LLM-Wiki, a Obsidian Vault. That's where floorplans, bank statements, insurance policy etc. are kept, so my agent "knows" or "remembers" all that without a memory provider bloating the context with my personal stuff whenever I give it an instruction to fix a bug in whatever project that happens to contain some of those words. I can ask questions about all that and get factual answers with citations, not some mushed together memory fragments.
This works much better for me! And it's also cheaper and faster!
However, you may have different needs. I'd like to hear from you, if that's the case. Why do you need a memory provider and does it work for you reliably?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wy78uh/unpopular_opinion_consider_the_idea_that_you_may/)
