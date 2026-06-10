---
name: using-cortex
description: Use when starting agent work in a Cortex skill library or when deciding which Cortex governance, architecture, framework, testing, or maintenance skills should apply.
---

# Output Marker

Display:
using skill: using-cortex

---

# Using Cortex

## Overview

Use this router before non-trivial work to choose the smallest set of Cortex
skills that actually govern the task. It is mandatory as the entry point, but it
must not force speculative loading.

## Routing Rules

- Load named skills first when the user explicitly requests them.
- Load a governance skill when its trigger clearly matches the task.
- Load architecture, framework, testing, TypeScript, documentation, or
  maintenance skills only when the task or changed files touch that area.
- Treat `code-documentation` as directly triggered by any code generation,
  edit, move, split, or refactor; it is not an optional final cleanup pass.
- Prefer the strictest relevant process skill first: debugging before fixes,
  verification before success claims, workspace state before broad edits.
- Do not load skills only because they might be vaguely useful.
- User instructions override routing when they explicitly limit tool or skill
  use.

## Cascade Model

When a request touches multiple domains, read the workspace cascade reference at
`../../../references/skill-cascade.md`.

Use the cascade as a routing algorithm:

1. Classify direct signals from the user request, files, diff, project config,
   and intended operation.
2. Select root skills from those signals.
3. Expand recursive `BEFORE` edges from the skill graph.
4. Add `WITH` skills only when they have direct evidence of their own.
5. Defer `AFTER` skills until that phase is reached.

Do not convert a single user example into a permanent route. Generalize only the
reusable signal behind it.

## Common Routes

- Ambiguous, creative, user-facing, or architecture-affecting work:
  `design-intake`.
- Multi-step, cross-boundary, migration, or high-risk work:
  `implementation-plan`.
- Substantial edits or plan execution: `workspace-state-guard`.
- Behavior changes and bug fixes: `test-first-discipline`.
- Code generation, editing, moving, splitting, or refactoring:
  `code-documentation`.
- Bugs, failures, or unexpected behavior: `systematic-debugging`.
- Major changes or publish decisions: `review-gate`.
- Review feedback: `review-feedback-triage`.
- Success claims, commits, pushes, PRs, or task completion:
  `completion-verification`.
- Merge, PR, push, cleanup, or finish decisions: `branch-completion`.

## Hard Stops

- Do not skip a clearly triggered governance gate for speed.
- Do not use `using-cortex` as a substitute for the routed skill body.
- Do not create hard `BEFORE` cascades from this router to every skill.

## Usage Checklist

- The user request and local context were checked.
- Only clearly triggered skills were selected.
- Process skills were selected before implementation-specific skills.
- Any explicit user limit on skills or tools was honored.

## Cross-References

- WITH: design-intake, implementation-plan, plan-execution, agent-delegation, workspace-state-guard, test-first-discipline, systematic-debugging, completion-verification, review-gate, review-feedback-triage, branch-completion, code-documentation
