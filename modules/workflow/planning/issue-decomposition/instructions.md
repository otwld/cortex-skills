
# Output Marker

Display:
using module: issue-decomposition

---

# Issue Decomposition

## Overview

Convert broad work into independently verifiable vertical slices and durable agent
briefs.

## Reference Routing

- Use `shared/vertical-slices.md` when this task touches that concern.
- Use `shared/agent-briefs.md` when this task touches that concern.
- Use `shared/issue-tracker-setup.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read source context; break end-to-end slices; classify AFK or human-in-loop; write behavioral briefs; publish only through configured tracker rules.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Slices describe end-to-end behavior with independently verifiable acceptance criteria.
- AFK-ready briefs have no open design decisions, hidden dependencies, or vague ownership.
- Tracker publishing follows configured GitHub, GitLab, or local markdown rules.

## Example

Candidate saved searches decomposes into persistence, query API, saved-search UI, and
delete behavior slices.

## Hard Stops

- Do not split work into database-only, API-only, UI-only, or tests-later tasks when a vertical slice is possible.
- Do not mark a slice AFK-ready while product, API, or validation decisions remain open.
- Do not publish issues to an unconfigured tracker or with labels invented in chat.

## Usage Checklist

- Source context and tracker memory were inspected before slicing.
- Each slice has behavior, interfaces, acceptance checks, blockers, and out-of-scope notes.
- Publishing mode, labels, and human-in-loop steps were followed or blocked explicitly.

## Cross References

- WITH: implementation-plan, grill-with-docs
- AFTER: plan-execution
