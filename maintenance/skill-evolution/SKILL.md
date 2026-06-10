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

## Convention Gap Analysis

Use this workflow when the user provides a folder path, a diff, or a changed-file
list to assess whether implementation patterns should become skill guidance.

1. Summarize the area by responsibility, layer, likely consumers, and dominant
   technologies.
2. Identify repeated naming, layout, documentation, testing, API, or architecture
   patterns.
3. Compare those patterns with existing skills before proposing anything new.
4. Flag gaps where guidance is absent, unclear, contradictory, or too broad to
   prevent repeated mistakes.
5. Return recommendations only unless the user explicitly asks to update skills.

Prefer updating an existing skill when the pattern fits its scope. Propose a new
skill only when the workflow is distinct, reusable, and not covered by a focused
existing skill.

## Recommendation Format

- Proposed action: update existing skill | create new skill | no action.
- Target skill or proposed skill name.
- Signal: repetition, risk, or coverage gap.
- Scope boundaries: covers and does not cover.
- Trigger wording to add or change.
- Documentation impact: metadata, graph, reference, or catalog updates needed.
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
- Folder, diff, or changed-file analysis summarized responsibility and consumers when provided.
- Scope boundaries are explicit.
- Validation path is named.

## Cross-References

- None
