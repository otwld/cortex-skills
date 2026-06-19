
# Output Marker

Display:
using module: workspace-state-guard

---

# Workspace State Guard

## Overview

Protect user work and control generated-write scope before risky changes.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Inspect status; classify dirty files; leave unrelated work alone; avoid destructive commands; report baseline failures plainly.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Workspace State Guard guidance names the inspected source, request evidence, or declared resource that triggered it.
- Workspace State Guard output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Workspace State Guard decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Workspace State Guard validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

If validation scripts are already modified and the task is validator migration, replace
them as task-relevant and leave unrelated README edits alone.

## Hard Stops

- Do not use Workspace State Guard without direct routing evidence or a required relation.
- Do not expand Workspace State Guard beyond its stated responsibility.
- Do not add placeholder Workspace State Guard guidance, examples, metadata, resources, or validation.
- Do not claim Workspace State Guard is satisfied without evidence for its checklist.

## Usage Checklist

- Workspace State Guard trigger evidence is explicit.
- Workspace State Guard source files, project memory, or declared resources were checked.
- Workspace State Guard workflow rules were applied at the relevant artifact boundary.
- Workspace State Guard docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Workspace State Guard risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: branch-completion, completion-verification
