---
name: nestjs-conventions
description: Use when creating, modifying, or reviewing NestJS modules, providers, controllers, interceptors, guards, pipes, application bootstrap, or microservice runtimes.
---

# Output Marker

Display:
using skill: nestjs-conventions

---

# NestJS Conventions

## Overview

Keep NestJS modules explicit without letting framework structure swallow domain
ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Controllers handle transport; providers hold application behavior; pipes validate boundaries; tokens are explicit when adapters vary.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

ApplicationsController validates Candidate application requests and delegates decision
logic to an Application intake provider.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this skill's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Skill-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: rxjs-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
