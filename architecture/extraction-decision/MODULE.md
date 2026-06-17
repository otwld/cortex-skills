---
name: extraction-decision
description: Internal Cortex module applied when repeated logic, DTOs, contracts, data-access patterns, UI composition, or orchestration suggest extracting a reusable abstraction.
---

# Output Marker

Display:
using module: extraction-decision

---

# Extraction Decision

## Overview

Decide whether duplication is stable enough to extract, and whether extraction improves
ownership, leverage, and locality.

## Reference Routing

- Use `../../references/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Inventory consumers; separate stable behavior from coincidental shape; choose owner before API; preserve dependency direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

Three Application status mappers with identical business rules may become one domain
mapper; similar Candidate cards may remain local if behavior differs.

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

- BEFORE: library-placement-decision, nx-module-boundaries
- WITH: public-api-design, naming-consistency, bundle-performance, code-documentation
- AFTER: skill-evolution
