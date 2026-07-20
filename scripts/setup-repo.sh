#!/usr/bin/env bash

# setup-repo.sh
#
# One-time bootstrap helper for the hermes-agent-community mirror repository.
#
# What it does:
# 1) Initializes a git repository (if needed)
# 2) Ensures we are on main
# 3) Creates the initial commit (README.md as required by the strategy)
# 4) Adds a GitHub remote (placeholder by default)
# 5) Pushes to origin/main
#
# The script is intentionally explicit and fails fast for missing dependencies
# or missing required files so CI operators can diagnose issues quickly.

set -euo pipefail

REPO_DIR="${1:-$(pwd)}"
REMOTE_URL="${2:-https://github.com/nousresearch/hermes-agent-community.git}"
TARGET_BRANCH="main"

log() {
  printf '[%s] %s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" "$*" >&2
}

require_command() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    log "Missing required dependency: $cmd"
    exit 1
  fi
}

ensure_inside_repo_root() {
  cd "$REPO_DIR"

  if [ ! -f "README.md" ]; then
    log "README.md is required for initial setup but was not found in $REPO_DIR"
    exit 1
  fi

  if [ ! -d ".git" ]; then
    log "Initializing new git repository"
    git init -b "$TARGET_BRANCH"
  else
    log "Existing git repository detected"
  fi

  # Force branch name to main for the mirror's canonical workflow.
  CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
  if [ "$CURRENT_BRANCH" != "$TARGET_BRANCH" ]; then
    log "Switching branch $CURRENT_BRANCH -> $TARGET_BRANCH"
    git checkout -B "$TARGET_BRANCH"
  fi
}

stage_initial_commit() {
  # Stage all repository files for the bootstrap commit.
  git add -A

  if git diff --cached --quiet; then
    log "No changes staged; nothing to commit"
  else
    log "Creating initial commit"
    git commit -m "Initial mirror repository setup"
  fi
}

set_remote() {
  if git remote | grep -qx "origin"; then
    EXISTING_URL="$(git remote get-url origin)"
    log "origin already set: $EXISTING_URL"
    if [ "$EXISTING_URL" != "$REMOTE_URL" ]; then
      log "Updating origin to placeholder URL: $REMOTE_URL"
      git remote set-url origin "$REMOTE_URL"
    fi
  else
    log "Adding origin remote: $REMOTE_URL"
    git remote add origin "$REMOTE_URL"
  fi
}

push_main() {
  log "Pushing $TARGET_BRANCH to origin/$TARGET_BRANCH"
  if git remote get-url origin >/dev/null 2>&1; then
    if git ls-remote --exit-code --heads origin "$TARGET_BRANCH" >/dev/null 2>&1; then
      git push -u origin "$TARGET_BRANCH"
    else
      # Push even if remote branch doesn't exist yet.
      git push -u origin "$TARGET_BRANCH"
    fi
  else
    log "origin remote missing; cannot push"
    exit 1
  fi
}

print_next_steps() {
  log "Repository bootstrap complete."
  log "Next steps:"
  log "  1) Review generated files"
  log "  2) Add any remaining guides / docs"
  log "  3) Configure secrets/workflows in GitHub"
  log "  4) Trigger workflow_dispatch for sync.yml once after enabling Actions"
}

require_command git
require_command mkdir

ensure_inside_repo_root
set_remote
stage_initial_commit
push_main
print_next_steps
