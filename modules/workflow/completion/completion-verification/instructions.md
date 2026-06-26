
# Output Marker

Display:
using module: completion-verification

---

# Completion Verification

## Overview

Treat completion as a current-state claim that requires authoritative evidence for every
requirement.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Derive requirements; identify proof; run or inspect fresh evidence; compare evidence to claim; report gaps and risks.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Completion claims map each user requirement to fresh evidence, not memory of earlier commands.
- Validation proof includes command results, inspected artifacts, or explicit blocked checks.
- Residual risks and unverified areas are reported before saying the task is complete.

## Example

After a module migration, validation ok is necessary but also confirm new modules,
references, catalog, graph, and tests exist.

## Hard Stops

- Do not claim success from stale output, assumptions, or partial validation.
- Do not collapse multiple requirements into a single vague pass statement.
- Do not hide skipped checks; name why they were skipped and what risk remains.

## Usage Checklist

- Requirements were derived from the latest user request and inspected work.
- Fresh proof was collected for each requirement or gap.
- Final response distinguishes completed work from remaining risk.

## Cross References

- WITH: review-gate, branch-completion
