---
title: "[Update v4.0.0] Hermes Improvements: Native SQLite WAL Engine, Model Lineage & Scale Benchmarks (Sub-80ms Retrieval)"
author: u/rednicv
date: 2026-10-12
score: 81
comments: 7
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1x3ck79/update_v400_hermes_improvements_native_sqlite_wal/
flair: "Memory & Context"
---

# [Update v4.0.0] Hermes Improvements: Native SQLite WAL Engine, Model Lineage & Scale Benchmarks (Sub-80ms Retrieval)

**Posted by u/rednicv on 2026-10-12 · 81 points (97% upvoted) · 7 comments**

Hey everyone!
Following up on the great feedback and questions from the v3 release, I’m excited to share that **v4.0.2** of `hermes-improvements` is officially live
👉 **GitHub Release:**
https://github.com/rednicv/hermes-improvements/releases/tag/v4.0.2
👉 **Repository:**
https://github.com/rednicv/hermes-improvements
### 🚀 What's New in v4.x?
**Native SQLite WAL Engine (`memory_vectors.sqlite`)**:
- We completely eliminated $O(N)$ JSON file rewrites.
- Vector storage and metadata now run inside SQLite in WAL mode with instant, atomic row-level transactions.
- Includes automatic one-shot migration: existing JSON installations are seamlessly migrated on first boot and safely archived.
2. **Decoupled Strategy Pattern & Total Fallback Isolation**:
- Clean `EmbeddingBackend` architecture.
- `SentenceTransformersBackend` remains the primary high-precision neural engine (`all-MiniLM-L6-v2`, with multilingual model support via `HERMES_EMBEDDING_MODEL`).
- The zero-dependency `TfidfBackend` fallback is now strictly quarantined: vocabulary drift and cold starts are self-contained without polluting the storage layer.
3. **Strict Model Lineage & Non-Padded Math**:
- Every stored vector tracks its originating `model_id` and dimensionality. If your embedding backend changes or recovers, stale vectors are re-computed from source text on demand. No synthetic zero-padding.
4. **Real-World Scale Benchmark Harness**:
- Added an automated evaluation benchmark (`benchmarks/eval_scale.py`) testing across realistic distractors (50 to 500+ memories).
- Validated **1.00 Recall@1/3/5**, **1.00 MRR**, with p50 latency under **60ms** and p95 retrieval latency dropped from ~270ms down to **~87ms**.
5. **Anti-Prompt Injection Hardening**:
- Injected memories are explicitly marked as passive data.
- Cross-script homoglyph defanging and markdown image exfiltration prevention built-in.
If you are running Hermes Agent in production or long multi-turn sessions, feel free to try it out! Stars and feedback on GitHub are always deeply appreciated. ⭐️

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1x3ck79/update_v400_hermes_improvements_native_sqlite_wal/)
