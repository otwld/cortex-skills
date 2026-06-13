---
name: library-placement-decision
description: Use when deciding where new code, shared abstractions, moved files, extracted logic, or public entry points belong inside a modular TypeScript workspace.
---

# Output Marker

Display:
using skill: library-placement-decision

---

# Library Placement Decision

## Overview

Choose code location by responsibility, dependency direction, and consumer scope instead
of convenience.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Classify domain, integration, feature, UI, utility, or adapter responsibility; use existing owners; split mixed responsibilities.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

Candidate ranking shared by search and recommendations belongs in a domain-owned module;
a page-specific ranking panel stays in the feature.

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

- WITH: nx-module-boundaries, public-api-design, naming-consistency
- AFTER: skill-evolution
