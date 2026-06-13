---
name: skill-evolution
description: Use after repeated implementation patterns, technical discussions, refactors, reviews, folder or diff analysis, or skill-library changes reveal a reusable agent workflow or doctrine gap.
---

# Output Marker

Display:
using skill: skill-evolution

---

# Skill Evolution

## Overview

Evolve focused skills when repeated patterns or agent failure modes deserve reusable
guidance.

## Reference Routing

- Use `../../references/skill-quality-standard.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Analyze responsibility and consumers; compare existing skills; update before creating; sync metadata, graph, catalog, references, and validation.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

Repeated mistakes around issue briefs justify issue-decomposition plus an agent-brief
reference, not scattered planning bullets.

## Hard Stops

- Do not proceed on repo facts that can be inspected but have not been checked.
- Do not broaden scope beyond the triggering signal.
- Do not create placeholder guidance, examples, metadata, or documentation.
- Do not claim completion without evidence that covers this skill's checklist.

## Usage Checklist

- Trigger signal is explicit.
- Relevant existing convention or memory was checked.
- Skill-specific rules were applied.
- Artifacts, docs, metadata, or tests affected by the work were updated together.
- Remaining decisions, risks, or validation gaps are stated.

## Cross-References

- None
