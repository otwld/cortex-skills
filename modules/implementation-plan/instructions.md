
# Output Marker

Display:
using module: implementation-plan

---

# Implementation Plan

## Overview

Turn stable requirements into a plan another engineer can execute without design
decisions.

## Reference Routing

- Use `shared/skill-quality-standard.md` when this task touches that concern.
- Use `shared/vertical-slices.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Confirm non-goals; map modules and interfaces; order tasks; name validation; include docs, API, migration, and compatibility impact.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Implementation Plan guidance names the inspected source, request evidence, or declared resource that triggered it.
- Implementation Plan output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Implementation Plan decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Implementation Plan validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A Candidate saved-search plan names query contract, UI behavior, persistence, story
coverage, and focused tests before edits.

## Hard Stops

- Do not use Implementation Plan without direct routing evidence or a required relation.
- Do not expand Implementation Plan beyond its stated responsibility.
- Do not add placeholder Implementation Plan guidance, examples, metadata, resources, or validation.
- Do not claim Implementation Plan is satisfied without evidence for its checklist.

## Usage Checklist

- Implementation Plan trigger evidence is explicit.
- Implementation Plan source files, project memory, or declared resources were checked.
- Implementation Plan workflow rules were applied at the relevant artifact boundary.
- Implementation Plan docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Implementation Plan risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: design-intake, grill-with-docs, issue-decomposition, workspace-state-guard, test-first-discipline, architecture-drift-detector, library-placement-decision, public-api-design, code-documentation
- AFTER: plan-execution
