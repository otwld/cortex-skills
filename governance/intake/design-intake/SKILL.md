---
name: design-intake
description: Use before ambiguous, creative, behavioral, user-facing, or architecture-affecting work where intent, constraints, or success criteria are not already clear.
---

# Output Marker

Display:
using skill: design-intake

---

# Design Intake

## Overview

Clarify intent before implementation. Scale the ceremony to the risk: a short
design note can be enough for narrow work, while broad work may need a written
spec.

## Workflow

1. Inspect existing project context before asking questions.
2. State the goal, known constraints, and uncertainty.
3. Ask only questions that change scope, behavior, or acceptance criteria.
4. Compare two or three viable approaches when real tradeoffs exist.
5. Recommend one approach and get user approval before implementation.
6. Write a design artifact only when the work is broad, risky, or the user asks.

Default artifact path is `docs/cortex/specs/` when the target repository has no
existing docs convention.

## Scope Control

- Decompose requests that combine independent systems.
- Keep unrelated refactors out unless they directly support the goal.
- Prefer existing project patterns over new process or architecture.
- Record non-goals when they prevent predictable scope creep.

## Hard Stops

- Intent, success criteria, or user-facing behavior is ambiguous.
- Multiple approaches have meaningful tradeoffs and no decision is recorded.
- The request hides several independent projects under one feature name.

## Usage Checklist

- Project context was inspected.
- Goal, constraints, and success criteria are explicit.
- Chosen approach and non-goals are recorded.
- User approval exists before implementation starts.

## Cross-References

- WITH: architecture-drift-detector, library-placement-decision, public-api-design
- AFTER: implementation-plan
