
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

- The plan is decision-complete: scope, interfaces, order, validation, docs, migration, and compatibility impact are fixed.
- Tasks are ordered so tests, public seams, generated artifacts, and docs move with the behavior they govern.
- Assumptions and non-goals are explicit enough that an implementer does not need to choose later.

## Example

A Candidate saved-search plan names query contract, UI behavior, persistence, story
coverage, and focused tests before edits.

## Hard Stops

- Do not publish a plan that still contains product, API, ownership, or validation decisions for the implementer.
- Do not bury migration or compatibility risk under generic refactor language.
- Do not skip tests and documentation planning when behavior or public surfaces change.

## Usage Checklist

- Requirements, non-goals, interfaces, and affected modules were mapped.
- Implementation order includes tests, docs, generated outputs, and validation checkpoints.
- Assumptions, accepted defaults, and residual risks are explicit.

## Cross References

- WITH: design-intake, grill-with-docs, issue-decomposition, workspace-state-guard, test-first-discipline, architecture-drift-detector, library-placement-decision, public-api-design, code-documentation
- AFTER: plan-execution
