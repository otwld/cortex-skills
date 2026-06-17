---
name: architecture-drift-detector
description: Internal Cortex module applied when starting significant work, reviewing recent changes, planning refactors, or seeing commit bursts that may indicate structural drift.
---

# Output Marker

Display:
using module: architecture-drift-detector

---

# Architecture Drift Detector

## Overview

Detect early structural risk from churn, repeated fixes, and ownership drift before it
becomes a rewrite.

## Reference Routing

- Use `../../references/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Use concrete signals; escalate only when risk is tied to a module, seam, package, or project area; recommend focused review instead of broad rewrites.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

Three changes touch Candidate search, Application persistence, and query helpers;
recommend reviewing the search seam before adding another filter.

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

- WITH: architecture-deepening-review, library-placement-decision, nx-module-boundaries
