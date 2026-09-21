---
title: "Building skills is not very skillful"
author: u/lbdesign
date: 2026-09-21
score: 6
comments: 10
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wll90o/building_skills_is_not_very_skillful/
flair: "Workflow — Daily habits, multi-agent setups, best practices"
---

# Building skills is not very skillful

**Posted by u/lbdesign on 2026-09-21 · 6 points (100% upvoted) · 10 comments**

I've noticed that skill files can get messy quickly. Hermes seems to default to patching or dumping quick notes into skills vs refactoring them cleanly. Like a messy kid in a rush. There is even a pitfall rule in the skill file about this, but Hermes doesn't always follow it:
> 10. "Letting skills accumulate sediment. When adding a rule, remove the old wording it replaces."
You might want to ask your Hermes to audit its own skills periodically and refactor them. (using a smart model!)
Another example from today: I found that skill rules referenced facts or resources that would not survive the chat that caused them to be created, thus creating impossible-to-follow junk. Hermes therefore added this rule:
> I also added a ## Writing rules for files in a live install section: every statement must be checkable by a session with no memory of how the file was written; cite a path, command, date or setting; never write "as discussed" or "the file we removed"; date facts that change.
My hermes has also made a local "
hermes-agent-skill-authoring-local"
file to augment its skill-making abilities.
Oh, also: prevent your Hermes from writing out skills or code from tokens/cache. This can produce tiny errors such as misplaced spaces, punctuation, syntax abnormalities. Have it create and work from on-disk files and have it diff and proofread them, as SOP.
Q: What else have you noticed about managing skills in Hermes?

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wll90o/building_skills_is_not_very_skillful/)
