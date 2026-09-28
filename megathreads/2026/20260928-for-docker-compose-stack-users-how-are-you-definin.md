---
title: "For Docker Compose stack users how are you defining your Hermes Agent deployment stack?"
author: u/Key_Sock4870
date: 2026-09-28
score: 5
comments: 5
type: text
reddit_url: https://www.reddit.com/r/hermesagent/comments/1wrdwhz/for_docker_compose_stack_users_how_are_you/
flair: "Infra / Hosting - VPS, Docker, Coolify, Proxmox, Remote, uptime"
---

# For Docker Compose stack users how are you defining your Hermes Agent deployment stack?

**Posted by u/Key_Sock4870 on 2026-09-28 · 5 points (100% upvoted) · 5 comments**

Hello!
New the the Hermes scene and loving it so far. I know there have been a couple different posts regarding using docker vs. direct install of the agent/gateway on the host, and I have decided to migrate the local stack to a Docker compose deployment to make it repeatable for different environments and refreshes etc.
I am curious how others are bootstrapping their configuration. The stack works but I feel it is quite messy and a little tedious to configure everything correctly out of the box, especially getting the TUI and Desktop App post deployment talking correctly to the docker hosted agent gateway.
Anyone have any tips or tricks, how are you deploying your Hermes Agent docker stack?
OS:
Linux (x64)
Distro:
Xubuntu 26.04 (Ubuntu)
Docker Engine
Version:
29.8.1
Docker Compose Version:
v5.5.1
Hermes Version:
Latest (docker)
Hermes WebUI (nesquena):
Latest (docker)
compose.yaml (Hermes Agent + Hermes Dashboard + Hermes Webui):
services:
  gateway:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped
    ports:
      - "8642:8642"
    volumes:
      - ~/.hermes:/opt/data
      - ~/:/workspace
      - hermes-agent-src:/opt/hermes
    environment:
      - HERMES_UID=${HERMES_UID:-1000}
      - HERMES_GID=${HERMES_GID:-1000}
      - API_SERVER_HOST=${API_SERVER_HOST:-0.0.0.0}
      - API_SERVER_KEY=${API_SERVER_KEY:-}
    command: ["gateway", "run"]
    deploy:
      resources:
        limits:
          memory: 32G
          cpus: "8.0"

  dashboard:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-dashboard
    restart: unless-stopped
    ports:
      - "9119:9119"
    volumes:
      - ~/.hermes:/opt/data
    environment:
      - HERMES_UID=${HERMES_UID:-1000}
      - HERMES_GID=${HERMES_GID:-1000}
    command: ["dashboard", "--host", "0.0.0.0", "--port", "9119", "--no-open", "--insecure"]
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: "1"
    depends_on:
      - gateway
  
  webui:
    image: ghcr.io/nesquena/hermes-webui:latest
    container_name: hermes-webui
    restart: unless-stopped
    ports:
      - "8787:8787"
    volumes:
      - ~/.hermes:/home/hermeswebui/.hermes
      - ~/:/workspace
      - hermes-agent-src:/home/hermeswebui/.hermes/hermes-agent:ro
    environment:
      - WANTED_UID=${UID:-1000}
      - WANTED_GID=${GID:-1000}
      - HERMES_HOME=/home/hermeswebui/.hermes
      - HERMES_WEBUI_AGENT_DIR=/home/hermeswebui/.hermes/hermes-agent
      - HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui
      - HERMES_WEBUI_PASSWORD=${HERMES_WEBUI_PASSWORD:-}
      - HERMES_WEBUI_GATEWAY_API_KEY=${API_SERVER_KEY:-}
      - HERMES_API_URL=http://hermes-agent:8642
      - HERMES_WEBUI_HOST=0.0.0.0
      - HERMES_WEBUI_PORT=8787
    depends_on:
      - gateway

volumes:
  hermes-agent-src:

---
**Original Post:** [View on Reddit](https://www.reddit.com/r/hermesagent/comments/1wrdwhz/for_docker_compose_stack_users_how_are_you/)
