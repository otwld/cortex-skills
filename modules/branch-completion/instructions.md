
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
3. Inspect status; verify; review if major; summarize scope; commit scoped changes only when requested; push or PR only with user direction.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Branch Completion guidance names the inspected source, request evidence, or declared resource that triggered it.
- Branch Completion output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Branch Completion decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Branch Completion validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

Commit module bodies, references, catalog, graph, and validator tests together while
leaving unrelated README edits uncommitted.

## Hard Stops

- Do not use Branch Completion without direct routing evidence or a required relation.
- Do not expand Branch Completion beyond its stated responsibility.
- Do not add placeholder Branch Completion guidance, examples, metadata, resources, or validation.
- Do not claim Branch Completion is satisfied without evidence for its checklist.

## Usage Checklist

- Branch Completion trigger evidence is explicit.
- Branch Completion source files, project memory, or declared resources were checked.
- Branch Completion workflow rules were applied at the relevant artifact boundary.
- Branch Completion docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Branch Completion risks, rejected paths, and validation gaps are stated.

## Cross References

- BEFORE: workspace-state-guard, completion-verification
- WITH: review-gate
