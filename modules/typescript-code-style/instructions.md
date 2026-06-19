
# Output Marker

Display:
using module: typescript-code-style

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
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Follow project tooling; prefer explicit imports; use strict narrowing; avoid casts; respect public entry points; comment intent, not syntax.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- TypeScript Code Style guidance names the inspected source, request evidence, or declared resource that triggered it.
- TypeScript Code Style output uses this workspace's terms and the recruitment example universe only when examples are needed.
- TypeScript Code Style decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- TypeScript Code Style validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

parseCandidateStage returns a typed CandidateStage or validation error instead of
casting form data.

## Hard Stops

- Do not use TypeScript Code Style without direct routing evidence or a required relation.
- Do not expand TypeScript Code Style beyond its stated responsibility.
- Do not add placeholder TypeScript Code Style guidance, examples, metadata, resources, or validation.
- Do not claim TypeScript Code Style is satisfied without evidence for its checklist.

## Usage Checklist

- TypeScript Code Style trigger evidence is explicit.
- TypeScript Code Style source files, project memory, or declared resources were checked.
- TypeScript Code Style workflow rules were applied at the relevant artifact boundary.
- TypeScript Code Style docs, metadata, tests, or generated artifacts affected by the change were updated together.
- TypeScript Code Style risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: code-documentation
