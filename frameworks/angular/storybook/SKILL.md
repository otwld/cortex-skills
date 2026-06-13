---
name: storybook-angular-conventions
description: Use when creating, modifying, or reviewing Angular Storybook stories, Angular story providers, module metadata, standalone story setup, or Angular story mocks.
---

# Output Marker

Display:
using skill: storybook-angular-conventions

---

# Storybook Angular Conventions

## Overview

Use Angular Storybook as executable documentation for component states and provider
contracts.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Match standalone or module setup; keep args typed; mock dependencies at the story boundary; use deterministic recruitment data.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

CandidateCard stories cover shortlisted, rejected, and interview-scheduled states with
stable Candidate fixtures.

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

- BEFORE: storybook-conventions, angular-conventions
- WITH: typescript-code-style, code-documentation
- AFTER: skill-evolution
