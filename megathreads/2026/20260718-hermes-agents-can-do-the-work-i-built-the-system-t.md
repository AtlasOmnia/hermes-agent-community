---
title: "Hermes agents can do the work. I built the system that helps them run a company."
author: u/Informal_Cap_5247
date: 2026-07-18
score: 53
comments: 20
type: text
reddit_url: https://reddit.com/r/hermesagent/comments/1v0azd8/hermes_agents_can_do_the_work_i_built_the_system/
flair: "SHOWCASE — Projects, tools, builds, demos, GitHub repos"
---

# Hermes agents can do the work. I built the system that helps them run a company.

**Posted by u/Informal_Cap_5247 on 2026-07-18 · 53 points (87% upvoted) · 20 comments**

Hey everyone,

Hermes agents are already capable of doing real work.

They can research, browse, analyze, create content, use tools and complete complex tasks.

But once you start running several agents for an actual business, the hard problem is no longer just execution.

The hard problem becomes:

* What does each agent know about the company?
* Which client is it working for?
* Which instructions must it never forget?
* Who owns each task?
* What happens when an agent stops responding?
* Where are the reports, files and deliverables stored?
* Which actions need human approval?
* How do multiple agents and humans work from the same operational context?

That is why I built **EmperorClaw**.

**EmperorClaw is a self-hosted operations platform for companies that use Hermes agents as part of their workforce.**

Hermes performs the work.

EmperorClaw gives that work structure, context, ownership and accountability.

# Turn Hermes agents into an organized company workforce

With EmperorClaw, you can create your company, invite your team, add clients, organize projects and connect specialized Hermes agents.

For example, a small company could run:

* an accounting assistant
* a research agent
* a content agent
* a project-management agent
* a customer-support agent
* an operations-monitoring agent

All of them can operate from one shared company system instead of separate prompts, folders and conversations.

# Give every agent the right knowledge

One of the core features is the **Company Brain**.

You can store:

* internal company procedures
* SOPs
* customer information
* project documentation
* financial rules
* writing guidelines
* templates
* operating instructions

Knowledge can be structured by:

* company
* client
* project
* agent

You can also force important documents to always be included in a specific agent’s context.

For example:

* the accounting agent always receives your financial procedures
* the content agent always receives your brand guidelines
* any agent working for Client A receives Client A’s rules
* a project agent receives only the context relevant to that project

The goal is simple:

>

# Make agent work durable

When an agent claims a task, EmperorClaw can assign it through a time-limited lease.

If the agent keeps working, its heartbeat renews the lease.

If it disappears or fails:

* the lease expires
* the task can retry
* failed work can move to a dead-letter state
* an incident can be created for a human to review

This means work does not silently disappear inside logs or abandoned sessions.

Every task can have:

* an owner
* a deadline
* a history
* a recovery path
* an output
* a human escalation path

# Keep humans in control

EmperorClaw is not designed to remove people from the company.

It is designed to help people manage a growing agent workforce.

Your human team can:

* assign and review work
* approve sensitive actions
* communicate with agents
* edit company knowledge
* inspect files and deliverables
* resolve incidents
* manage permissions
* see what happened and when

# Store the actual outputs

Agents create more than chat messages.

They create:

* reports
* research
* screenshots
* files
* spreadsheets
* evidence
* customer deliverables

EmperorClaw stores these as durable artifacts connected to the relevant task, project and client.

# Built for self-hosted company operations

The first release is focused on one private company instance.

You can deploy it on:

* a VPS
* a private server
* a company VM
* infrastructure you control

It includes:

* PostgreSQL
* persistent storage
* team accounts
* role-based permissions
* optional email invitations
* WebSocket updates
* Docker deployment
* Hermes integration
* MCP-compatible APIs

It was originally designed with a future hosted SaaS version in mind, but I decided to launch the self-hosted version first so companies and Hermes users can operate it privately and help shape the product.

# Why this is different from another agent dashboard

Most agent tools focus on:

* starting agents
* watching agents
* viewing logs
* triggering workflows

EmperorClaw is focused on the business around the agents:

* company knowledge
* client context
* operational procedures
* durable task ownership
* artifacts
* approvals
* incidents
* human accountability

The goal is not only to monitor agents.

The goal is to help a small company build a reliable AI-assisted back office.

# I would genuinely value feedback from Hermes users

I am especially interested in learning:

* How are you currently organizing multiple Hermes agents?
* What information do your agents repeatedly forget?
* How do you separate context between clients?
* Where do you keep agent-generated files and deliverables?
* What happens today when an agent fails halfway through a task?
* Which company workflows would you want agents to operate together?

Repository:

[**https://github.com/emperorclaw/emperorclaw**](https://reddit.com)

I would appreciate honest criticism, feature requests and integration feedback.

The goal is to build this around real Hermes users and real company operations—not around an imaginary use case.

---

**Original Post:** [View on Reddit](https://reddit.com/r/hermesagent/comments/1v0azd8/hermes_agents_can_do_the_work_i_built_the_system/)

