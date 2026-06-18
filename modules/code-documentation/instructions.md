
# Output Marker

Display:
using module: code-documentation

---

# Code Documentation

## Overview

Make documentation part of the code change rather than a cleanup pass.

## Reference Routing

- Use `shared/skill-quality-standard.md` when this task touches that concern.
- Use `shared/recruitment-universe.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Apply the module-specific rules: Document touched public or reusable surfaces; move docs with code; update Storybook or MDX where that is the docs surface; avoid placeholder comments.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the module changes behavior or workflow.

## Example

A reusable CandidateCard documents required data, empty states, and selection behavior
instead of commenting each template line.

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

- WITH: example-universe-enforcer, storybook-conventions
- AFTER: skill-evolution
