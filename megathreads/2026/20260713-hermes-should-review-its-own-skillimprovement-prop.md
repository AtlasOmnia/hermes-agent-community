---
title: "Hermes should review its own skill-improvement proposals by default, not just add them"
author: u/4rt_relay
date: 2026-07-13
score: 82
comments: 25
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1uvqmyx/hermes_should_review_its_own_skillimprovement/
flair: "Discussion-Strategy, tradeoffs, opinions, comparisons, structure"
---

# Hermes should review its own skill-improvement proposals by default, not just add them

**Posted by u/4rt_relay on 2026-07-13 · 82 points (99% upvoted) · 25 comments**

**TL;DR**  
  
Hermes’s automatic self-improvement sounds great, but it can (and will) turn frequently used skills into dumping grounds for every temporary lesson.  
  
One of my most-used skills received **700+ automatic edits** and grew into **hundreds of kilobytes of Markdown files**. More “learning” was making the skill worse: bloated, repetitive, harder to load, and full of guidance tied to old incidents.  
  
Hermes should make skill maintenance a default second stage: collect proposed changes, group them by skill, then use an isolated reviewer to merge, rewrite, reject, or defer them. The reviewer should optimize for a smaller and more accurate final skill, not for accepting as many proposals as possible.

  
**The problem**  
  
I like Hermes’s self-improvement loop and don't want to turn if off, but it is missing a crucial second half: it can generate skill changes much more easily than it can responsibly maintain the resulting skill library.  
  
I saw the extreme version of this with one of my most frequently used skills. It went through **700+ automatic edits** and eventually accumulated **hundreds of kilobytes of Markdown**.  
  
Because the skill was used often, almost every session produced another supposedly reusable lesson. Temporary debugging findings, one-off recovery steps, outdated implementation details, and repeated versions of existing rules all became permanent documentation.  
  
The skill was technically “learning,” but the result was worse:  
  
\- The main [`SKILL.md`](https://reddit.comhttp://SKILL.md) stopped being a concise operating guide.  
\- The same ideas appeared in multiple forms and files.  
\- Incident-specific instructions became permanent policy.  
\- Old implementation details survived after the code changed.  
\- Important rules became harder to find among all the accumulated text.  
\- Automatic edits happened during active work, creating a moving target for testing and review.  
\- More Markdown meant more context, more review work, and more opportunities for contradictory instructions.  
  
Enabling skill-write approval helps, but only partially. Instead of immediately bloating the skill, Hermes accumulates pending proposals and leaves the maintenance job to the user.  
  
Reviewing each proposal independently is also the wrong abstraction:  
  
\- Several proposals may target the same skill and overlap or contradict each other.  
\- A suggestion can identify a real problem while proposing the wrong durable fix.  
\- Accepting every useful-looking addition still creates skill sediment.  
\- Details that belong in a reference file get added to the hot path.  
\- The proposed workflow may not match the actual CLI or implementation.  
\- Independent reviewers can overwrite each other or resolve unrelated proposals.  
\- A worker saying “done” is not proof that the final skill is valid.  
  
The choice should not be between uncontrolled automatic edits and a giant manual approval queue.  
  
**The solution**  
  
I added a nightly maintenance pass that treats pending self-improvement proposals as material to review, not instructions to execute.  
  
It:  
  
1. Groups all pending proposals by target skill.  
2. Waits until the proposals and skill files have been idle for a while.  
3. Gives each skill package to an isolated reviewer.  
4. Reads the current skill, its references, and all related proposals together.  
5. Decides per proposal:  
\- accept exactly;  
\- merge or rewrite;  
\- reject;  
\- defer if the operation is too risky.  
6. Reviews the skill holistically instead of evaluating each patch in isolation.  
7. Prefers replacing, consolidating, or deleting existing guidance over adding more text.  
8. Moves detailed material into references instead of bloating `SKILL.md`.  
9. Uses per-skill locks, backups, and exact proposal IDs.  
10. Refuses autonomous creation, deletion, renaming, executable changes, and unrelated edits.  
11. Runs an independent finalizer that rereads the resulting files, validates frontmatter and links, checks the remaining pending state, and flags unexplained growth.  
12. Sends one concise report. If nothing is ready, it stays silent and does not call a model.  
  
The important part is that the reviewer is allowed to disagree with the original self-improvement proposal.  
  
A proposal may contain a useful observation without containing the right patch. The correct outcome may be to rewrite an existing paragraph, move one sentence into a reference, fix the underlying tool, or save nothing at all.  
  
In one real review, two proposed additions were rejected because they described an unsupported recovery workflow. The reviewer kept the actual limitation in an existing reference and reduced the main skill by about 1,700 characters instead of adding another incident-specific runbook.  
  
That is what self-improvement should look like: not simply remembering more, but improving the quality of what remains.  
  
**Why this should be a Hermes default**  
  
Self-improvement without maintenance naturally tends toward accumulation.  
  
Write approval prevents surprise edits, but by itself it shifts the entire curation burden onto the user. Automatic application removes that burden, but risks turning frequently used skills into enormous append-only journals.  
  
Hermes should ship with a conservative version of this two-stage loop:

>Generate proposals during normal work. Review them later in isolation. Consolidate by skill. Validate the final artifact independently. Apply only changes that make the skill more correct, compact, and useful.

“Nothing to save” should be a normal and successful outcome.  
  
The default reviewer should optimize for:  
\- correctness;  
\- simplicity;  
\- progressive disclosure;  
\- removal of stale or duplicated guidance;  
\- consistency with the real implementation;  
\- smaller or justified skill growth.  
  
It should **not** optimize for proposal acceptance rate or treat every session observation as permanent knowledge.  
  
Without this second stage, automatic self-improvement can become automatic documentation debt. With it, Hermes could actually improve its skills over time instead of merely making them longer.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1uvqmyx/hermes_should_review_its_own_skillimprovement/)

