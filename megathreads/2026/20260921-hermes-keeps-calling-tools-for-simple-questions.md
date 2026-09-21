---
title: "Hermes keeps calling tools for simple questions"
author: u/Rianone10
date: 2026-09-21
score: 11
comments: 14
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wlfcea/hermes_keeps_calling_tools_for_simple_questions/
flair: "Help — Technical issues, errors, config, debugging"
---

# Hermes keeps calling tools for simple questions

**Posted by u/Rianone10 on 2026-09-21 · 11 points (100% upvoted) · 14 comments**

Hi everyone,
I'm having a strange issue with Hermes and I'm wondering if anyone else has experienced something similar.
I'm running Hermes with DeepSeek V4.1 Flash through OpenRouter. My relevant configuration is:
Model: deepseek/deepseek-v4.1-flash
Provider: OpenRouter
agent.execution_guidance = auto
agent.task_completion_guidance = true
agent.parallel_tool_call_guidance = true
The problem is that Hermes seems to use tools far too often, even for very simple conversational questions.
For example, if I ask "Are you there?", a simple yes/no question, or something like "What does this mean?", I would expect it to just answer in text.
Instead, it sometimes starts using Python, shell commands or other tools before answering. In some cases it makes several tool calls for something that clearly doesn't require any external information or computation.
This makes simple conversations surprisingly slow and also wastes tokens and resources.
I looked into the configuration and found that execution_guidance is set to "auto", and the comments in the code say that DeepSeek is one of the model families for which this guidance is enabled automatically.
I understand why this kind of execution discipline is useful for real agent tasks. I definitely don't want to disable it completely, because I still want Hermes to use tools properly when working with files, code, system operations, web searches, etc.
What I'm looking for is more of a "use tools only when they're actually needed" behaviour.
Something along the lines of: if the question can be answered directly from the current context/knowledge, just answer it without calling any tools. Only use tools when they are genuinely necessary.
Has anyone else noticed this behaviour with Hermes, particularly when using DeepSeek? Is there a recommended configuration or prompt setting for this?
I'd rather use the proper Hermes mechanism than just disable execution_guidance globally.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wlfcea/hermes_keeps_calling_tools_for_simple_questions/)
