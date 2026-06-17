---
name: grill-with-docs
description: Internal Cortex module applied when stress-testing a plan against project vocabulary, documented decisions, domain rules, or when a deep questioning session should update glossary and ADR artifacts.
---

# Output Marker

Display:
using module: grill-with-docs

---

# Grill With Docs

## Overview

Run a deep alignment interview that challenges language and decisions against project
memory.

## Reference Routing

- Use `../../../references/project-memory.md` when this task touches that concern.
- Use `../../../references/domain-glossary.md` when this task touches that concern.
- Use `../../../references/adr-format.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Read memory first; explore facts instead of asking; ask one decision-changing question at a time; update glossary terms inline; offer ADRs sparingly.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

If “active candidate” is fuzzy, ask whether it means submitted, interviewing, or not
rejected, then record the chosen term.

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

- WITH: design-intake, implementation-plan
- AFTER: issue-decomposition
