---
name: skill-evolution
description: Use after repeated implementation patterns, technical discussions, refactors, reviews, or skill-library changes reveal a reusable agent workflow or doctrine gap.
---

# Output Marker

Display:
using skill: skill-evolution

---

# Skill Evolution

## Overview

Skills should evolve from repeated, reusable patterns. Prefer small focused
skills, explicit scope, progressive disclosure, and validation over broad
doctrine documents.

## When To Recommend A Skill Change

Recommend a new or updated skill when:

- A pattern repeats across projects or packages.
- Agents keep making the same judgment error.
- A workflow depends on non-obvious local knowledge.
- Existing skills overlap or contradict each other.
- A refactor reveals a reusable convention.

Do not recommend a skill for one-off decisions, obvious language basics, or
rules better enforced by tooling.

## Recommendation Format

- Proposed action: update existing skill | create new skill | no action.
- Target skill or proposed skill name.
- Signal: repetition, risk, or coverage gap.
- Scope boundaries: covers and does not cover.
- Trigger wording to add or change.
- Validation idea: command, scenario, or review check.

## Update Rules

- Keep changes narrow.
- Update cross-references and `agents/openai.yaml` with the skill.
- Move large stable details into `references/`.
- Put deterministic mechanical checks into `scripts/`.
- Do not preserve obsolete project-specific assumptions in active skill text.

## Usage Checklist

- The pattern is reusable beyond one task.
- Existing skills were checked first.
- Scope boundaries are explicit.
- Validation path is named.

## Cross-References

- None
