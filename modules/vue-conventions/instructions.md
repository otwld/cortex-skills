
# Output Marker

Display:
using module: vue-conventions

---

# Vue Conventions

## Overview

Keep Vue component public surfaces small, typed, and aligned with reactive ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Use local Vue style; type props and emits; prefer computed derived state; extract composables only for real reuse; document slots.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

CandidateStagePicker emits stageSelected with a typed stage payload and documents
disabled-stage behavior.

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

- WITH: typescript-code-style, rxjs-conventions, code-documentation
- AFTER: skill-evolution
