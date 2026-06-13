---
name: bricks
description: "Use when working with Bricks in consumer Nx repositories: inspecting or running Bricks init, source, install, merge, diff, status, doctor, or contribute commands; reviewing installed-brick edits; updating installed copies; or helping contribute consumer edits back to source repos through Bricks worktree workflows. Do not use for Nx release, npm publishing, or source-repo maintainer release workflows unless Bricks consumer state is directly involved."
---

# Output Marker

Display:
using skill: bricks

---

# Bricks

## Overview

Operate Bricks installed-source workflows without confusing consumer edits, source
worktrees, and release flows.

## Reference Routing

- Use `references/product-model.md` when this task touches that concern.
- Use `references/cli-workflows.md` when this task touches that concern.
- Use `references/contribution-workflow.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this skill governs.
3. Apply the skill-specific rules: Inspect Bricks status; identify workflow branch; use Bricks commands instead of manual copies; protect consumer edits; run doctor or diff checks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this skill's scope and route to the appropriate governance skill.

## Quality Gates

- Guidance is grounded in current files or explicit user intent.
- Output uses project vocabulary and the recruitment example universe when examples are needed.
- Decisions are recorded in the right artifact instead of hidden in transient chat.
- Validation or acceptance criteria are named when the skill changes behavior or workflow.

## Example

If a Candidate UI brick has local consumer edits, inspect Bricks diff before merging an
upstream update.

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

- WITH: workspace-state-guard, nx-conventions, completion-verification
