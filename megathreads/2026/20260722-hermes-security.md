---
title: "Hermes security"
author: u/Centraldread
date: 2026-07-22
score: 28
comments: 18
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v3fvik/hermes_security/
flair: "Discussion - Workflows, habits, setup, best practices"
---

# Hermes security

**Posted by u/Centraldread on 2026-07-22 · 28 points (83% upvoted) · 18 comments**

A few days ago I asked my local qwen3.6 27b model to make an encrypted hidden folder. It did it and gave me this long spill about everything it was doing and how hidden it was and how it has this strong 256 bit AES encryption. Of course I bought it and was thinking it was safe. But I got this idea that turned into the most fun I’ve ever had with AI. I asked my default Hermes model (grok 4.5) to act like a hacker find the encrypted folder and break into it. I gave him a 10 minute timer and told him to start. 

Grok started the test and it took him 54 seconds to break in and read the txt file I left in it. 

We ran  the test again 4 more times. Second time 34 seconds. Third time 1m 4 seconds. Final test was a little over 2m. This was over a 3 day period every time we increased the security. By the last step the folder wasn’t even on the same machine it was on my multimedia server in the living room. Grok literally had to ssh into the machine that he’s never even been to before. The vault skill the qwen model made was encrypted I had to give it the key so it would even know where the vault was. Then it would tell me it’s at the vault door and ask for the passphrase. Grok got through all of it. 

This whole game was extremely fun I learned so much too much to post every round and how he got in. But what it came down to is models are sloppy even when you try to do everything to the T, delete clip boards, delete chats, delete caches, try to keep the keys away from the model all together. If it has seen the key at all a frontier model can and will find it. I ran one final test last night where I made my own encrypted folder and set my own key. Grok found it very fast but couldn’t break into it. If you have a local model hiding and encrypting stuff for you it’s not safe at all from another model or its self if someone did prompt injection. If any of you are running more than one profile try this game it’s really fun and I’d love to hear if y’all can actually get one model to do this and the other not find it. I think it’s impossible.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v3fvik/hermes_security/)

