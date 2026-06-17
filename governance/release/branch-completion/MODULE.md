---
name: branch-completion
description: Internal Cortex module applied when implementation is complete and the user asks to merge, push, open a pull request, publish, discard, clean up, or finish branch work.
---

# Output Marker

Display:
using module: branch-completion

---

# Branch Completion

## Overview

Turn local work into a durable handoff or published change without sweeping unrelated
files into release steps.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Inspect status; verify; review if major; summarize scope; commit scoped changes only when requested; push or PR only with user direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

Commit module bodies, references, catalog, graph, and validator tests together while
leaving unrelated README edits uncommitted.

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

- BEFORE: workspace-state-guard, completion-verification
- WITH: review-gate
