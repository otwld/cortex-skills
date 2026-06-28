---
name: setup-agent-instructions
description: Use only when the user explicitly includes $setup-agent-instructions; sets up or audits workspace AI-agent instruction files such as AGENTS.md, nested AGENTS.md, CLAUDE.md, .github/copilot-instructions.md, .cursorrules, .cursor/rules, .windsurf, or .clinerules.
---


# Setup Agent Instructions

## Overview

This command skill runs only when directly invoked as `$setup-agent-instructions`.


Set up durable workspace instructions with `AGENTS.md` as the canonical
default. Challenge assumptions before writing instructions that future agents
will treat as operating rules.

## Workflow

1. Inspect before asking: find existing root and nested `AGENTS.md` files,
   tool-specific AI files, repo docs, manifests, task runners, CI config,
   generated-file markers, and release or contribution docs.
2. Separate evidence from preference: record discovered repo facts, then ask the
   user about only the choices that cannot be derived from files.
3. Run a strict grill before creating durable instructions: challenge unclear
   claims about commands, protected files, ownership, generated outputs, secrets,
   release steps, and agent autonomy.
4. Draft `AGENTS.md` first: include repo-specific orientation, edit targets,
   validation commands, documentation obligations, safety boundaries, generated
   artifacts, routed-skill handoff boundaries, and release cautions.
5. Add nested `AGENTS.md` only when a subtree has materially different rules,
   commands, generated outputs, or ownership boundaries.
6. Treat tool-specific files as secondary: update existing files only when they
   conflict or drift; create new ones only when explicitly requested. Keep
   `AGENTS.md` canonical and make secondary files thin pointers or narrow
   supplements.
7. Re-read the final instructions against the repository before claiming they
   are ready. Remove generic agent advice, stale guesses, copied docs, and
   instructions that cannot be backed by current files or explicit user intent.

## Quality Gates

- Instructions are grounded in inspected files or explicit user decisions.
- `AGENTS.md` is the source of truth unless the user explicitly chooses another
  canonical file.
- Tool-specific files do not contradict `AGENTS.md`.
- Generated files, protected paths, security boundaries, and verification
  commands are concrete and checkable.
- Routed hidden modules are described as active only when the entry skill is
  explicitly invoked or project instructions define a concrete handoff
  convention.
- The output avoids broad doctrine such as "be helpful" and focuses on
  repository-specific operating facts.
- The strict grill happens before writing or replacing durable agent
  instructions.

## Example

For a recruitment job board workspace, discover that backend tests use one
command, frontend tests use another, generated API clients must not be
hand-edited, and release notes live in a contributor guide. Grill the user on
whether agents may create nested instructions for the admin app, then write a
root `AGENTS.md` plus a nested app guide only if the app has distinct rules.

## Hard Stops

- Do not set up instructions from memory when repo facts can be inspected.
- Do not create an AI instruction bundle by default; start with `AGENTS.md`.
- Do not copy large sections from `README`, contribution docs, or architecture
  docs when a link and short operating rule is enough.
- Do not invent commands, owners, path rules, or release processes.
- Do not imply hidden routing applies to direct requests unless a public entry
  invocation or handoff convention makes that boundary explicit.
- Do not preserve conflicting instructions across multiple AI files.
- Do not claim completion without checking the generated guidance against the
  current repository.

## Completion Checklist

- Existing agent instruction files and repo docs were inspected.
- User preferences were challenged where files could not answer the decision.
- Canonical file choice and secondary-file policy are explicit.
- Repo map, validation, safety, docs, generated artifacts, and release guidance
  are covered only where relevant.
- Nested or tool-specific files are justified by concrete scope differences.
- Final instructions were re-read against current files.

## Source Artifacts

- None
