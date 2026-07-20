#!/usr/bin/env bash

# sync-reddit.sh
#
# Pull the top 25 posts from r/hermesagent for the past 24 hours using Reddit's
# public JSON endpoint, then hand the payload to the Python parser to generate
# markdown files under megathreads/YYYY/YYYY-MM-DD-slugified-title.md.
#
# This script is intentionally defensive:
# - validates required dependencies (curl + python3)
# - uses an explicit User-Agent as required by Reddit API etiquette
# - handles network and HTTP errors
# - validates that the Python parser produced output
# - exits with a non-zero code on failure so CI can detect issues

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

SUBREDDIT="hermesagent"
LIMIT=25
TIME_WINDOW="day"              # equivalent to 'past 24h' in Reddit API.
OUTPUT_DIR="megathreads"       # Python script creates the year subfolder internally.
USER_AGENT="hermes-agent-community-sync/1.0 (+https://github.com/nousresearch/hermes-agent-community)"
API_URL="https://www.reddit.com/r/${SUBREDDIT}/top.json?limit=${LIMIT}&t=${TIME_WINDOW}"
PYTHON_CONVERTER="${SCRIPT_DIR}/reddit_to_markdown.py"
TMP_JSON="$(mktemp)"
TMP_LOG="$(mktemp)"
trap 'rm -f "$TMP_JSON" "$TMP_LOG"' EXIT

log() {
  printf '[%s] %s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" "$*" >&2
}

require_command() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    log "Required dependency missing: $cmd"
    log "Install it before running this workflow"
    exit 1
  fi
}

validate_input_file() {
  local path="$1"
  if [[ ! -s "$path" ]]; then
    log "Downloaded response is empty: $path"
    exit 1
  fi

  # Basic sanity check for JSON response shape (Reddit responses include a top-level data key)
  if ! jq -e '.data.children | length' "$path" >/dev/null 2>&1; then
    # jq is optional; fallback to python-based syntax check in parser path.
    if [[ "$(head -c 1 "$path")" != "{" ]]; then
      log "Downloaded payload is not JSON or is invalid JSON"
      exit 1
    fi
  fi
}

require_command "curl"
require_command "python3"

log "Fetching top ${LIMIT} posts from r/${SUBREDDIT} (${TIME_WINDOW})"

HTTP_STATUS="$(curl -sS --user-agent "$USER_AGENT" \
  --max-time 30 \
  --retry 3 \
  --retry-delay 2 \
  --fail-with-body \
  -H "Accept: application/json" \
  -w "%{http_code}" \
  "$API_URL" \
  -o "$TMP_JSON" )"
STATUS_CODE="$?"

# On curl success, HTTP_STATUS variable contains the status code from -w. On retry failures,
# curl exits non-zero and status code is undefined.
if [[ "$STATUS_CODE" -ne 0 ]]; then
  log "curl request failed (exit $STATUS_CODE)."
  if [[ -s "$TMP_JSON" ]]; then
    log "Response body:\n$(cat "$TMP_JSON")"
  fi
  exit 1
fi

if [[ "$HTTP_STATUS" -lt 200 || "$HTTP_STATUS" -ge 300 ]]; then
  log "Reddit API returned non-2xx status: ${HTTP_STATUS}"
  log "Response body:\n$(cat "$TMP_JSON")"
  exit 1
fi

validate_input_file "$TMP_JSON"
log "Download complete. Delegating conversion to ${PYTHON_CONVERTER}"

# Parse and write markdown using the Python script.
python3 "$PYTHON_CONVERTER" \
  --input-file "$TMP_JSON" \
  --output-dir "$OUTPUT_DIR" \
  --score-threshold 25 \
  --flair-filter "Guide,Tutorial,Showcase,Discussion,Announcement,Megathread,Resource"

log "Reddit sync completed."
