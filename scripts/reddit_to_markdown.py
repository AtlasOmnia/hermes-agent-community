#!/usr/bin/env python3
"""Convert Reddit JSON to markdown files for the Hermes Agent mirror repo.

This script is intentionally standalone and uses only the Python standard library.
It supports two input modes:

1. --input-file: load a reddit JSON response saved by the shell sync script.
2. --subreddit: directly fetch r/<subreddit>/top.json from Reddit.

The second mode exists for local testing and includes a built-in 0.5s request
throttle to stay within API politeness constraints.
"""

from __future__ import annotations

import argparse
import io
import html
import json
import logging
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, Tuple


REQUEST_LOG = []
LAST_REQUEST_TS = 0.0


def configure_logger(level: str) -> None:
    """Set up structured logging for script diagnostics and CI visibility."""

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )
    logging.Formatter.converter = time.gmtime


def rate_limited_sleep(min_interval: float) -> None:
    """Enforce a minimum interval between outbound HTTP requests."""

    global LAST_REQUEST_TS
    now = time.monotonic()
    delta = now - LAST_REQUEST_TS
    if LAST_REQUEST_TS > 0 and delta < min_interval:
        sleep_for = min_interval - delta
        logging.debug("Rate limiting: sleeping %.2fs", sleep_for)
        time.sleep(sleep_for)
    LAST_REQUEST_TS = time.monotonic()


def download_json(url: str, user_agent: str, timeout: int = 20, max_attempts: int = 3, rate_limit: float = 0.5) -> dict:
    """Fetch JSON from Reddit with retry + timeout + throttling + logging."""

    headers = {"User-Agent": user_agent, "Accept": "application/json"}
    backoff = 1.5

    for attempt in range(1, max_attempts + 1):
        rate_limited_sleep(rate_limit)
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", 0)
                payload = response.read().decode("utf-8", errors="replace")

                if status != 200:
                    logging.error("HTTP %s while requesting %s", status, url)
                    raise urllib.error.HTTPError(url, status, "HTTP status error", response.headers, None)

                logging.info("Fetched %s (attempt %d)", url, attempt)
                return json.loads(payload)
        except urllib.error.HTTPError as error:
            # Retry rate-limit / transient server-side failures.
            code = getattr(error, "code", None)
            if code in {429, 500, 502, 503, 504} and attempt < max_attempts:
                logging.warning("Attempt %d failed with HTTP %s; retrying in %.1fs", attempt, code, backoff)
                time.sleep(backoff)
                backoff *= 2
                continue
            logging.error("HTTP error on %s: %s", url, error)
            raise
        except (urllib.error.URLError, TimeoutError, ValueError) as error:
            if attempt < max_attempts:
                logging.warning("Attempt %d failed: %s. Retrying in %.1fs", attempt, error, backoff)
                time.sleep(backoff)
                backoff *= 2
                continue
            logging.error("Permanent failure requesting %s: %s", url, error)
            raise

    raise RuntimeError(f"Exhausted retries for {url}")


def clean_title_for_slug(title: str, max_len: int = 90) -> str:
    """Normalize a title into a safe, SEO-friendly filename slug."""

    if not title:
        return "untitled"

    # Normalize unicode and strip apostrophes from terms like "Hermes'" etc.
    value = unicodedata.normalize("NFKD", title)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower().strip()

    # Replace brackets, punctuation, and markdown artifacts with spaces.
    value = re.sub(r"[`*_~|>[\]{}()#]+", " ", value)
    # Convert remaining disallowed chars to nothing.
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    # Collapse whitespace/hyphens to single hyphen.
    value = re.sub(r"[\s_-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")

    if not value:
        return "post"
    if len(value) > max_len:
        value = value[:max_len].rstrip("-")
    return value or "post"


def normalize_markdown(text: str) -> str:
    """Clean Reddit text while preserving markdown code blocks, links and images."""

    if not text:
        return ""

    value = html.unescape(text)
    value = value.replace("\r\n", "\n")
    value = value.replace("\r", "\n")

    # Keep code fences intact; this regex trims accidental leading spaces outside fenced blocks.
    value = re.sub(r"\n{3,}", "\n\n", value)

    return value.strip()


def yaml_value(value: object) -> str:
    """Serialize a scalar for YAML frontmatter with robust escaping."""

    if value is None:
        return '""'
    return json.dumps(str(value), ensure_ascii=False)


def should_include_post(post: dict, score_threshold: int, allowed_flairs: Iterable[str]) -> bool:
    """Apply score and flair filters."""

    score = int(post.get("score", 0) or 0)
    if score < score_threshold:
        return False

    flair = (post.get("link_flair_text") or "").lower()
    if not flair:
        # The caller requested flair-based filtering; posts without flair are skipped.
        return False

    lowered = [entry.strip().lower() for entry in allowed_flairs if entry.strip()]
    return any(f in flair for f in lowered)


def unique_path(base_dir: Path, stem: str) -> Path:
    """Generate a unique filename by adding -2/-3 suffixes if needed."""

    base = base_dir / f"{stem}.md"
    if not base.exists():
        return base

    i = 2
    while True:
        candidate = base_dir / f"{stem}-{i}.md"
        if not candidate.exists():
            return candidate
        i += 1


def convert_posts(payload: dict, output_dir: Path, score_threshold: int, flairs: List[str]) -> Tuple[int, int, int]:
    """Convert valid posts to markdown files. Returns counters."""

    children = (
        payload.get("data", {})
        .get("children", [])
    )

    if not isinstance(children, list):
        raise ValueError("Unexpected payload structure: 'data.children' is not a list")

    processed = 0
    skipped_filter = 0
    skipped_invalid = 0

    output_dir.mkdir(parents=True, exist_ok=True)

    for entry in children:
        data = entry.get("data") if isinstance(entry, dict) else None
        if not isinstance(data, dict):
            skipped_invalid += 1
            logging.warning("Skipping malformed child entry: %s", str(entry)[:200])
            continue

        if not should_include_post(data, score_threshold, flairs):
            skipped_filter += 1
            continue

        title = (data.get("title") or "Untitled").strip()
        author = (data.get("author") or "[deleted]").strip()
        permalink = (data.get("permalink") or "").strip()
        score = int(data.get("score", 0) or 0)
        num_comments = int(data.get("num_comments", 0) or 0)

        utc = data.get("created_utc")
        try:
            created_ts = float(utc)
            created = datetime.fromtimestamp(created_ts, tz=timezone.utc)
        except (TypeError, ValueError):
            logging.warning("Invalid created_utc for post '%s'; using now", title)
            created = datetime.now(tz=timezone.utc)

        date_str = created.strftime("%Y-%m-%d")
        iso_date = created.isoformat()
        year_dir = output_dir / created.strftime("%Y")
        year_dir.mkdir(parents=True, exist_ok=True)

        slug = clean_title_for_slug(title)
        file_stem = f"{date_str}-{slug}"
        file_path = unique_path(year_dir, file_stem)

        # Keep subreddit links as canonical https://www.reddit.com URLs.
        full_permalink = (
            permalink
            if permalink.startswith("http")
            else f"https://www.reddit.com{permalink}" if permalink
            else ""
        )

        subreddit = data.get("subreddit", "hermesagent")
        selftext = normalize_markdown(data.get("selftext", "") or data.get("selftext_html", ""))

        fm = "\n".join(
            [
                "---",
                f"title: {yaml_value(title)}",
                f"date: {yaml_value(iso_date)}",
                f"author: {yaml_value(author)}",
                f"permalink: {yaml_value(full_permalink)}",
                f"score: {score}",
                f"comment_count: {num_comments}",
                f"subreddit: {yaml_value(subreddit)}",
                "---",
                "",
            ]
        )

        body = "".join(
            [
                f"# {title}\n\n",
                f"- **author:** {author}\n",
                f"- **score:** {score}\n",
                f"- **comments:** {num_comments}\n",
                f"- **posted:** {date_str}\n",
                f"- **source:** [{subreddit}]({full_permalink})\n\n",
            ]
        )

        content = fm + body

        # Preserve explicit markdown blocks and links in the self-post body.
        if selftext:
            content += "## Content\n\n" + selftext + "\n\n"
        else:
            content += "## Content\n\n_No selftext provided in the source post._\n\n"

        try:
            file_path.write_text(content, encoding="utf-8")
            processed += 1
            logging.info("Wrote %s", file_path)
        except OSError as error:
            skipped_invalid += 1
            logging.error("Failed to write %s: %s", file_path, error)

    return processed, skipped_filter, skipped_invalid


def parse_args() -> argparse.Namespace:
    """CLI parser and argument validation."""

    parser = argparse.ArgumentParser(description="Convert Reddit JSON posts to markdown")
    parser.add_argument("--input-file", help="Path to reddit JSON file", default=None)
    parser.add_argument("--subreddit", help="Fetch from /r/<subreddit> directly", default="hermesagent")
    parser.add_argument(
        "--output-dir",
        default="megathreads",
        help="Directory where files are written (year is appended automatically)",
    )
    parser.add_argument("--score-threshold", type=int, default=25, help="Minimum score to include")
    parser.add_argument(
        "--flair-filter",
        default="Guide,Tutorial,Showcase,Discussion,Announcement,Megathread,Resource",
        help="Comma-separated list of flair keywords to include",
    )
    parser.add_argument("--user-agent", default="hermes-agent-community-sync/1.0", help="HTTP User-Agent string")
    parser.add_argument("--rate-limit", type=float, default=0.5, help="Delay between external requests")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def load_json_from_stream(stream) -> dict:
    """Load and decode JSON from a file-like stream."""

    try:
        return json.load(stream)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON input: {error}") from error


def load_payload(args: argparse.Namespace) -> dict:
    """Load payload from file, network, or stdin."""

    if args.input_file:
        logging.info("Loading Reddit payload from file: %s", args.input_file)
        with open(args.input_file, "r", encoding="utf-8") as input_fh:
            return load_json_from_stream(input_fh)

    if not sys.stdin.isatty():
        stdin_data = sys.stdin.read()
        if stdin_data and stdin_data.strip():
            logging.info("Loading Reddit payload from stdin")
            return load_json_from_stream(io.StringIO(stdin_data))
        logging.info("stdin is empty; falling back to direct fetch")

    # Fallback mode: fetch directly.
    url = f"https://www.reddit.com/r/{args.subreddit}/top.json?limit=25&t=day"
    logging.info("Fetching top posts directly from %s", url)
    return download_json(
        url=url,
        user_agent=args.user_agent,
        rate_limit=args.rate_limit,
        timeout=20,
        max_attempts=4,
    )


def main() -> int:
    """Run conversion and return process exit code."""

    args = parse_args()
    configure_logger(args.log_level)

    output_dir = Path(args.output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    flairs = [item for item in args.flair_filter.split(",") if item.strip()]

    try:
        payload = load_payload(args)
    except Exception as exc:  # Keep failure explicit and actionable.
        logging.error("Could not load Reddit payload: %s", exc)
        return 1

    try:
        processed, skipped_filter, skipped_invalid = convert_posts(
            payload=payload,
            output_dir=output_dir,
            score_threshold=args.score_threshold,
            flairs=flairs,
        )
    except Exception as exc:
        logging.error("Conversion failed: %s", exc)
        return 1

    logging.info(
        "Done. Wrote=%d, skipped_filter=%d, skipped_invalid=%d",
        processed,
        skipped_filter,
        skipped_invalid,
    )

    if processed == 0:
        logging.warning("No posts met the filter criteria; no files were written")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
