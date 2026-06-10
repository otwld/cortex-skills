---
name: review-gate
description: Use after major features or refactors, before merge, pull request, push, publish, or when a completed change needs independent quality review.
---

# Output Marker

Display:
using skill: review-gate

---

# Review Gate

## Overview

Review significant work before it compounds. Use subagent review when available;
otherwise perform a local self-review against the same checklist.

## Workflow

1. Identify the requirements, summary, and diff range.
2. Choose review mode: delegated review when available, local review otherwise.
3. Check requirement fit before code quality.
4. Classify findings by severity.
5. Fix critical and important issues before publishing.
6. Run `completion-verification` after fixes.

## Review Focus

- Requirement coverage and scope control.
- Correctness, edge cases, and failure modes.
- Tests verify real behavior.
- Public API, naming, ownership, and module boundaries.
- Documentation and migration needs when public behavior changes.

## References

Use `agent-delegation` templates when delegating review.

## Hard Stops

- A major change is published without review.
- Requirement compliance is skipped because tests pass.
- Important review findings are ignored without technical justification.

## Usage Checklist

- Requirements and diff range are known.
- Requirement fit was reviewed before quality details.
- Findings are classified by severity.
- Required fixes were verified.

## Cross-References

- WITH: agent-delegation, completion-verification, review-feedback-triage, public-api-design, architecture-drift-detector
