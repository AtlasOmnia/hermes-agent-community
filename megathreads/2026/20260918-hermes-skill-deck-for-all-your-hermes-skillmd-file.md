---
title: "Hermes Skill Deck for all your Hermes skill.md files is now open source and live."
author: u/dontforgetthef
date: 2026-09-18
score: 8
comments: 0
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wj7j06/hermes_skill_deck_for_all_your_hermes_skillmd/
flair: "Showcase — Projects, tools, builds, demos"
---

# Hermes Skill Deck for all your Hermes skill.md files is now open source and live.

**Posted by u/dontforgetthef on 2026-09-18 · 8 points (100% upvoted) · 0 comments**

Follow up to my post from a couple days ago about the Hermes Skill Deck.
It's now live now here:
https://github.com/runninwithitmarketing/hermes-skill-deck
You can also watch a walkthrough I did here:
https://youtu.be/BaLOT-GPWwc
The problem we all have:
Our skills pile up across ~/.hermes and every profile, and the only way to check them is by opening files one by one. This is a small Mac app that reads all of them into one window.
Also, the top menu bar is yours. First launch it asks which skills you want up there, and you can group the rest into custom boxes however you like.
Everything runs local. The only outbound calls are the Terminal Mode AI, on your own keys. Currently supports GLM, DeepSeek, and Claude keys.
Files are still read-only in the main view. In-place editing is the next step. Agent in the AI terminal can write.
Browse by Search (see below), profile, and folder; search everything; click a skill to read it. Your files stay the source of truth. The app is just a viewer on top.
What it's built on:
Tauri - the shell that makes it a real Mac app you double-click, instead of something that only lives in a browser tab. It's the lightweight alternative to wrapping everything in a full browser (Electron), which is why it doesn't eat memory.
React - the UI layer. It draws every button, folder, and card you see, and redraws them instantly when anything changes.
Vite - the tool that serves and builds the React frontend. Makes dev preview instant and squeezes the final files small.
Tailwind - the styling. Instead of writing separate CSS files, the neon colors and layout come from utility classes right in the code.
FastAPI (Python) - the backend. A small server running on your machine that reads your skill files, indexes them, and hands them to the UI on request. Also runs the Terminal Mode AI calls.
SQLite - the index. One local database file where all your
SKILL.md
contents live after sync, so search is instant. Your actual files stay the source of truth; this is just the copy the app searches against.
Also, the quick access opens your real Profiles and Skills folder so you always have direct access to your files from the app.
More updates in the future for settings. Open to any feedback and updates you like. If you catch any bugs, let me know!
Close-up view of the agent. It opens and closes like a digital tv screen in the middle of the app. Ask it whatever you want.

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wj7j06/hermes_skill_deck_for_all_your_hermes_skillmd/)
