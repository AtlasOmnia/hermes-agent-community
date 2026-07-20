# Contributing to Hermes Agent Community Resources

## 1) Submit Process

This repository mirrors high-signal community content from Reddit so that the same knowledge is discoverable from GitHub and search engines.

To submit content, follow this process:

1. Cross-post the content in the [r/hermesagent subreddit](https://reddit.com/r/hermesagent) if it is not already there.
2. Copy the final Reddit post text and metadata (author, score, comments, date, permalink).
3. Run the repository sync flow (or add the file manually if the post is historical).
4. Open a PR with your new or updated markdown in the matching folder.

If submitting manually, do not invent metadata; use source truth from Reddit.

## 2) File Naming Conventions

Use predictable, crawler-friendly names:

### Guides
- Use lowercase words with hyphens.
- Examples: `start-here.md`, `installation-macos.md`, `model-guide.md`
- Keep names concise and descriptive.

### Megathreads
- Use date-first format: `YYYY-MM-topic-slug.md`
- Examples:
  - `2026-07-setup-showcase.md`
  - `2026-07-model-discussion.md`

### Showcase files
- Use lowercase hyphenated slugs:
  - `github-pr-reviewer.md`
  - `daily-news-briefing.md`

## 3) Content Selection Criteria

Mirror only content that remains useful outside a single Reddit thread.

Include posts that meet all of the following:

- Score >= 25 upvotes.
- One of these Reddit flairs is present: Guide, Tutorial, Showcase, Discussion, Announcement, Megathread.
- Content contains durable, reusable guidance (not a joke, meme, or one-off question).
- The Markdown is coherent after formatting cleanup.
- Topic has long-tail search value for **Hermes Agent** users.

Skip:
- Memes and pure banter.
- Low-effort, short threads.
- Duplicate content already mirrored.
- Posts with insufficient context or missing metadata.

## 4) Markdown Formatting Guidelines

- Use GitHub-flavored Markdown only.
- Use title case for top-level headings and sentence case for body sections.
- Use one `#` H1, and `##`/`###` for subsections.
- Keep lines readable. Avoid very long unwrapped paragraphs.
- Preserve Reddit code blocks and links where they add value.
- In frontmatter use plain scalar values; avoid tabs.
- Use fenced code blocks with a language tag when possible:
  - ```` ```bash ````
  - ```` ```python ```
- Use absolute links only for external references.

## 5) PR and moderation checks

Before opening a PR, ensure:

- File path follows naming rules.
- Frontmatter includes `title`, `date`, `author`, `permalink`, `score`, and `subreddit`.
- Any community post is linked back to Reddit.
- No secrets, private data, or non-consented screenshots are included.

The PR should include a short summary of why this content is valuable and the source URL.
