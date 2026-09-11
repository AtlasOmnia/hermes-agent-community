---
title: ""Use a better model" shouldn't be the answer to an unstable foundation."
author: u/shadow666gamble
date: 2026-09-11
score: 109
comments: 45
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wcbou0/use_a_better_model_shouldnt_be_the_answer_to_an/
flair: "Discussion — General thoughts, opinions, comparisons"
---

# "Use a better model" shouldn't be the answer to an unstable foundation.

**Posted by u/shadow666gamble on 2026-09-11 · 109 points (94% upvoted) · 45 comments**

Hey again - today I'm coming with some feedback. This post is fully human written.
I been using the Hermes agent for a few days already, I think the idea is good, and so far it has become my main agent workflow. However, I see an attitude in this community that feels like every problem with the app can be solved by asking the agent to solve it or figure it out, and if it can't, use a better model.
I think this is fundamentally the wrong approach, and it's similar to game developers releasing increasingly unoptimized games because the hardware gets powerful enough to run them. I think spending more time simply polishing the already implemented things would be better, because right now a lot of things are shipped broken:
Desktop app:
- The "Review" panel doesn't even work at all when on a remote gateway. It feels very awkward having the agent edit files and not being able to see what changed.
- The UI feels glitchy, menus don't move freely and get stuck. I like the style, I just wish it worked properly and I could resize things.
-
I'd like to be able to just open a file and see what's in it
. It doesn't have to become an IDE, but I constantly have to find myself having Hermes Agent on one window and then an IDE on another window on the same workspace just to see what the agent is doing.
- The chat box scrolling lags and randomly jumps up to random points in the conversation out of nowhere.
- Many of the included skills or tools shipped just don't work out of the box and I feel it would be better if they were not shipped by default.
Memory system:
This has been a major pain point. The whole selling point of this product (for me) was having the agent build it's own memory that evolves over time, so I think one of the main features of the Desktop app or any related UI should have been to
easily view all the memory related files in one place
, and get a clear explanation of what each file does, and
where it's being added to the context when you speak to your agent
.
Right now, if I want to see in real time what the agent is doing with it's memory, I need to open another IDE, navigate to the .hermes folder, and then find the SOUL, MEMORY and USER files.
And then there's the fact that models don't really respect the line between MEMORY and USER files, and so I found removing the USER file completely actually made the memory better and simpler, and I just told it short memory = MEMORY.MD. I didn't really have a need for two separate files that end up just working against each other.
And then I tried the external memory. The pain. I tried OpenViking, and that's when everything went to shit. OpenViking, by default, has its own Identity AND Soul files, and you end up with
5 different identity memory files
, and then OpenViking starts doing it's own LLM on the knowledge base which by the way will completely kill your performance if you are using a single local model, because it will constantly load and unload the model ctx for the summarization.
So I ended up having to create a brand new memory system based on short term (MEMORY.md) and long term memory with Obsidian, but it would have better if I didn't have to spend so much time figuring things out and the UI made a better work at explaining to me how the system works and made it easy for me, and for my models.
Conclusion
Many of this issues APPEAR to work if you run the very best model like Astra or Fable, but the reality is the models are wasting tokens and time fixing the floor they are walking on as they run their turn,  where it would be very much better if the foundation of house was solid, so all models can walk comfortably, if that makes any sense.
Just my two cents, I will keep using hermes for now because it's the project that fits my needs best in the market right now, but I really hope the focus can shift towards quality rather than to keep adding more and more features on an unstable foundation.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wcbou0/use_a_better_model_shouldnt_be_the_answer_to_an/)
