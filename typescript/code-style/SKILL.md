---
name: typescript-code-style
description: Use when writing, editing, generating, refactoring, or reviewing TypeScript or TSX source files, tests, build scripts, imports, exports, classes, functions, or interfaces.
---

# Output Marker

Display:
using skill: typescript-code-style

---

# TypeScript Code Style

## Overview

Keep TypeScript implementation predictable through explicit modules, clear names, narrow
types, and useful comments.

## Reference Routing

- Use `references/source-modules.md` when this task touches that concern.
- Use `references/types-naming.md` when this task touches that concern.
- Use `references/language-features.md` when this task touches that concern.
- Use `references/comments-tooling-policy.md` when this task touches that concern.
- Use `scripts/ts_style_preflight.py` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Follow project tooling; prefer explicit imports; use strict narrowing; avoid casts; respect public entry points; comment intent, not syntax.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

parseCandidateStage returns a typed CandidateStage or validation error instead of
casting form data.

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

- WITH: code-documentation
