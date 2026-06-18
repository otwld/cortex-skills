
# Output Marker

Display:
using module: architecture-deepening-review

---

# Architecture Deepening Review

## Overview

Find modules whose interfaces are too wide for the behavior they hide and propose deeper
seams that increase leverage and locality.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.
- Use `shared/project-memory.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Use the architecture vocabulary exactly; apply the deletion test; classify dependencies; identify the interface that tests should cross.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

Candidate matching rules scattered across routes, repositories, and UI filters suggest a
deep Matching module tested through Application outcomes.

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

## Cross References

- WITH: architecture-drift-detector, library-placement-decision, public-api-design, test-first-discipline, code-documentation
- AFTER: skill-evolution
