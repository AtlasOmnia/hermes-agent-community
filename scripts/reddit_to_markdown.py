#!/usr/bin/env python3
"""
Convert Reddit posts to Markdown for GitHub mirror.
Scrapes old.reddit.com HTML (no OAuth/API key required).
"""

import sys
import os
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
BASE_URL = 'https://old.reddit.com'
SESSION = requests.Session()
SESSION.headers.update({'User-Agent': USER_AGENT, 'Accept': 'text/html,application/xhtml+xml'})


def extract_reddit_posts(subreddit='hermesagent', limit=25, time_filter='day', score_threshold=5):
    """
    Fetch top posts from subreddit by scraping old.reddit.com HTML.
    No authentication required.
    """
    time_map = {'hour': 'hour', 'day': 'day', 'week': 'week', 'month': 'month', 'year': 'year', 'all': 'all'}
    t = time_map.get(time_filter, 'day')
    
    url = f'{BASE_URL}/r/{subreddit}/top/?t={t}&limit={limit}'
    print(f"Fetching {url}...", file=sys.stderr)
    
    response = SESSION.get(url, timeout=30)
    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}", file=sys.stderr)
        print(response.text[:500], file=sys.stderr)
        sys.exit(1)
    
    soup = BeautifulSoup(response.text, 'lxml')
    posts = []
    
    # old.reddit.com listing: each post is in a <div class="thing" data-type="link">
    for thing in soup.find_all('div', class_='thing', attrs={'data-type': 'link'}):
        try:
            post = parse_listing_thing(thing, subreddit)
            if post and post['score'] >= score_threshold:
                posts.append(post)
        except Exception as e:
            print(f"  ⚠ Skipping post (parse error: {e})", file=sys.stderr)
            continue
        
        if len(posts) >= limit:
            break
    
    print(f"Fetched {len(posts)} posts meeting threshold (≥{score_threshold})", file=sys.stderr)
    return posts


def parse_listing_thing(thing, subreddit):
    """Parse a single .thing element from the listing page."""
    data = {}
    data['id'] = thing.get('data-fullname', '') or thing.get('id', '')
    
    # Title and permalink
    title_elem = thing.find('a', class_='title')
    if not title_elem:
        return None
    data['title'] = title_elem.get_text(strip=True)
    
    permalink = title_elem.get('href', '')
    if permalink.startswith('/'):
        data['permalink'] = urljoin(BASE_URL, permalink)
    else:
        data['permalink'] = permalink
    
    # Author
    author_elem = thing.find('a', class_='author')
    data['author'] = author_elem.get_text(strip=True) if author_elem else '[deleted]'
    
    # Score
    score_elem = thing.find('div', class_='score')
    score_text = score_elem.get_text(strip=True) if score_elem else '0'
    score_text = score_text.replace('points', '').replace('point', '').strip()
    try:
        data['score'] = int(score_text)
    except ValueError:
        data['score'] = 0
    
    # Upvote ratio (not available on old.reddit listing, default to 0)
    data['upvote_ratio'] = 0
    
    # Comments count
    comments_elem = thing.find('a', class_='comments')
    if comments_elem:
        comments_text = comments_elem.get_text(strip=True)
        comments_match = re.search(r'(\d+)', comments_text)
        data['num_comments'] = int(comments_match.group(1)) if comments_match else 0
    else:
        data['num_comments'] = 0
    
    # Timestamp from data attribute
    data['created_utc'] = int(thing.get('data-timestamp', '0')) // 1000 if thing.get('data-timestamp') else 0
    
    # URL (external link or self post)
    domain = thing.find('span', class_='domain')
    external_link = title_elem.get('href', '')
    if domain and '(self.' in domain.get_text(strip=True):
        data['url'] = data['permalink']
    elif external_link.startswith('http'):
        data['url'] = external_link
    else:
        data['url'] = data['permalink']
    
    # Flair
    flair_elem = thing.find('span', class_='linkflairlabel')
    data['flair'] = flair_elem.get_text(strip=True) if flair_elem else ''
    
    # For self posts, fetch the actual content
    data['selftext'] = ''
    if 'self.' in subreddit.lower() or data['url'] == data['permalink'] or not data['url']:
        data['selftext'] = fetch_selftext(data['permalink'])
    
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
    print(f"  Method: scraping old.reddit.com HTML", file=sys.stderr)
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
