---
name: implementation-plan
description: Internal Cortex module applied when requirements are known and the work is multi-step, cross-boundary, migration-related, high-risk, or needs a written execution path before edits.
---

# Output Marker

Display:
using module: implementation-plan

---

# Implementation Plan

## Overview

Turn stable requirements into a plan another engineer can execute without design
decisions.

## Reference Routing

- Use `../../../references/skill-quality-standard.md` when this task touches that concern.
- Use `../../../references/vertical-slices.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Confirm non-goals; map modules and interfaces; order tasks; name validation; include docs, API, migration, and compatibility impact.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

A Candidate saved-search plan names query contract, UI behavior, persistence, story
coverage, and focused tests before edits.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this module's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Module-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- WITH: design-intake, grill-with-docs, issue-decomposition, workspace-state-guard, test-first-discipline, architecture-drift-detector, library-placement-decision, public-api-design, code-documentation
- AFTER: plan-execution
