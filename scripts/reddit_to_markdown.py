#!/usr/bin/env python3
"""
Convert Reddit posts to Markdown for GitHub mirror.
Scrapes old.reddit.com HTML (no OAuth/API key required).
"""

import sys
import os
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
BASE_URL = 'https://www.reddit.com'
SESSION = requests.Session()
SESSION.headers.update({'User-Agent': USER_AGENT, 'Accept': 'text/html,application/xhtml+xml'})


def extract_reddit_posts(subreddit='hermesagent', limit=25, time_filter='day', score_threshold=5):
    """Fetch top posts from Reddit's current server-rendered feed."""
    time_map = {'hour': 'HOUR', 'day': 'DAY', 'week': 'WEEK', 'month': 'MONTH', 'year': 'YEAR', 'all': 'ALL'}
    t = time_map.get(time_filter, 'DAY')

    # Reddit retired the old HTML listing and now serves post metadata through
    # this public partial used by the current web frontend. It includes scores,
    # unlike the public RSS feed, so the configured threshold remains enforceable.
    url = f'{BASE_URL}/svc/shreddit/community-more-posts/top/'
    params = {
        't': t,
        'limit': str(limit),
        'name': subreddit,
        'navigationSessionId': str(uuid.uuid4()),
        'feedLength': '0',
    }
    print(f"Fetching {url}...", file=sys.stderr)
    
    response = SESSION.get(
        url,
        params=params,
        headers={'Referer': f'{BASE_URL}/r/{subreddit}/top/?t={time_filter}&limit={limit}'},
        timeout=30,
        allow_redirects=False,
    )
    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}", file=sys.stderr)
        print(response.text[:500], file=sys.stderr)
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    listing_posts = soup.find_all('shreddit-post')
    if not listing_posts:
        title = soup.title.get_text(' ', strip=True) if soup.title else 'untitled response'
        raise RuntimeError(
            f"Reddit feed returned no post records (title: {title!r}); refusing to treat an error page as empty"
        )
    
    posts = []
    for post_element in listing_posts:
        try:
            post = parse_shreddit_post(post_element)
            if post and post['score'] >= score_threshold:
                posts.append(post)
        except Exception as exc:
            print(f"  ⚠ Skipping post (parse error: {exc})", file=sys.stderr)
            continue
        
        if len(posts) >= limit:
            break
    
    print(f"Listing returned {len(listing_posts)} posts; fetched {len(posts)} posts meeting threshold (≥{score_threshold})", file=sys.stderr)
    return posts


def parse_shreddit_post(post_element):
    """Parse one current Reddit ``<shreddit-post>`` feed element."""
    title = post_element.get('post-title', '').strip()
    permalink = post_element.get('permalink', '').strip()
    if not title or not permalink:
        return None
    
    data = {
        'id': post_element.get('id', ''),
        'title': title,
        'permalink': urljoin(BASE_URL, permalink),
        'author': post_element.get('author', '[deleted]') or '[deleted]',
        'score': int(post_element.get('score', '0') or '0'),
        'upvote_ratio': float(post_element.get('upvote-ratio', '0') or '0'),
        'num_comments': int(post_element.get('comment-count', '0') or '0'),
        'flair': '',
        'selftext': '',
    }

    timestamp = post_element.get('created-timestamp', '')
    if timestamp:
        try:
            parsed_timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            if parsed_timestamp.tzinfo is None:
                parsed_timestamp = parsed_timestamp.replace(tzinfo=timezone.utc)
            data['created_utc'] = int(parsed_timestamp.timestamp())
        except ValueError:
            data['created_utc'] = 0
    else:
        data['created_utc'] = 0
    
    content_href = (post_element.get('content-href') or '').strip()
    post_type = (post_element.get('post-type') or '').lower()
    data['url'] = content_href if content_href and content_href != data['permalink'] else data['permalink']
    
    flair_element = post_element.find('shreddit-post-flair')
    if flair_element:
        data['flair'] = flair_element.get_text(' ', strip=True)
    
    if post_type == 'text' or data['url'] == data['permalink']:
        text_body = post_element.find('shreddit-post-text-body')
        if text_body:
            data['selftext'] = text_body.get_text('\n', strip=True)
    
    return data


def fetch_selftext(permalink):
    """Fetch the full self-text of a post."""
    try:
        response = SESSION.get(permalink, timeout=15)
        if response.status_code != 200:
            return ''
        soup = BeautifulSoup(response.text, 'lxml')
        # old.reddit.com: self text is in a <div class="md"> in the usertext-body
        usertext = soup.find('div', class_='usertext-body')
        if usertext:
            md = usertext.find('div', class_='md')
            if md:
                # Convert HTML back to rough markdown
                text = md.get_text('\n', strip=True)
                return text
        return ''
    except Exception:
        return ''


def clean_markdown(text):
    """Clean up Reddit markdown for GitHub compatibility."""
    if not text:
        return ''
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    return text.strip()


def post_to_markdown(post_data):
    """Convert a Reddit post dict to Markdown file content."""
    title = post_data.get('title', 'Untitled')
    author = post_data.get('author', '[deleted]')
    score = post_data.get('score', 0)
    upvote_ratio = post_data.get('upvote_ratio', 0)
    num_comments = post_data.get('num_comments', 0)
    created_utc = post_data.get('created_utc', 0)
    permalink = post_data.get('permalink', '')
    selftext = post_data.get('selftext', '')
    url = post_data.get('url', '')
    flair = post_data.get('flair', '')
    
    if created_utc:
        created_date = datetime.fromtimestamp(created_utc, tz=timezone.utc).strftime('%Y-%m-%d')
    else:
        created_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    
    # Determine post type
    is_self = (permalink == url) or not url
    
    # Build YAML frontmatter
    frontmatter = f"""---
title: "{title}"
author: u/{author}
date: {created_date}
score: {score}
comments: {num_comments}
type: {"text" if is_self else "link"}
reddit_url: {permalink}
flair: "{flair}"
---"""
    
    # Build Markdown body
    pct = int(upvote_ratio * 100) if upvote_ratio else ''
    score_line = f'**Posted by u/{author} on {created_date} · {score} points'
    if pct:
        score_line += f' ({pct}% upvoted)'
    score_line += f' · {num_comments} comments**\n\n'
    
    body = f'# {title}\n\n{score_line}'
    
    if selftext:
        body += f'{clean_markdown(selftext)}\n\n'
    elif not is_self and url:
        body += f'**Link:** [{url}]({url})\n\n'
    
    body += f"""---
**Original Post:** [View on Reddit]({permalink})
"""
    
    return frontmatter + '\n\n' + body


def generate_filename(title, created_utc, max_length=50):
    """Generate a sanitized filename from post title."""
    filename = title.lower()
    filename = re.sub(r'[^a-z0-9\s]', '', filename)
    filename = re.sub(r'\s+', '-', filename.strip())
    
    if len(filename) > max_length:
        filename = filename[:max_length].rstrip('-')
    
    date_str = datetime.fromtimestamp(created_utc, tz=timezone.utc).strftime('%Y%m%d') if created_utc else datetime.now(timezone.utc).strftime('%Y%m%d')
    return f"{date_str}-{filename}"


def save_post_markdown(post_data, output_dir):
    """Save a Reddit post as a Markdown file."""
    title = post_data.get('title', 'Untitled')
    created_utc = post_data.get('created_utc', 0)
    
    filename = generate_filename(title, created_utc)
    filepath = Path(output_dir) / f"{filename}.md"
    
    markdown_content = post_to_markdown(post_data)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"  ✓ {filename}.md", file=sys.stderr)
    return str(filepath)


def main():
    """Main entry point."""
    subreddit = os.environ.get('SUBREDDIT', 'hermesagent')
    output_dir = os.environ.get('OUTPUT_DIR', 'megathreads/2026')
    limit = int(os.environ.get('LIMIT', '25'))
    time_filter = os.environ.get('TIME_FILTER', 'day')
    score_threshold = int(os.environ.get('SCORE_THRESHOLD', '5'))
    
    print(f"Configuration:", file=sys.stderr)
    print(f"  Subreddit: r/{subreddit}", file=sys.stderr)
    print(f"  Output: {output_dir}", file=sys.stderr)
    print(f"  Limit: {limit}", file=sys.stderr)
    print(f"  Time filter: {time_filter}", file=sys.stderr)
    print(f"  Score threshold: ≥{score_threshold}", file=sys.stderr)
    print(f"  Method: Reddit server-rendered feed partial", file=sys.stderr)
    print(file=sys.stderr)
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Extract posts
    posts = extract_reddit_posts(
        subreddit=subreddit,
        limit=limit,
        time_filter=time_filter,
        score_threshold=score_threshold
    )
    
    if not posts:
        print("No posts matched the criteria.", file=sys.stderr)
        return
    
    # Save posts
    print(f"\nSaving {len(posts)} posts to {output_dir}...", file=sys.stderr)
    saved_files = []
    for post in posts:
        filepath = save_post_markdown(post, output_dir)
        saved_files.append(filepath)
    
    print(f"\n✓ Done! Saved {len(saved_files)} files.", file=sys.stderr)
    for f in saved_files:
        print(f"  {f}", file=sys.stderr)


if __name__ == '__main__':
    main()
