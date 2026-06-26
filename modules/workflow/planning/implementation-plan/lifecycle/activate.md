# Implementation Plan Activate

## Overview

Confirm that requirements are stable enough to produce an implementation plan
that another engineer can execute without inventing product or technical
decisions.

## Workflow

1. Read user requirements, acceptance criteria, constraints, and non-goals.
2. Inspect current repository structure, public interfaces, tests, docs,
   generated files, and validation commands that the plan will affect.
3. Use `skill-quality-standard.md` when planning skill artifacts.
4. Use `vertical-slices.md` when the work can be delivered as end-to-end
   increments.
5. Identify affected surfaces, compatibility concerns, migration impact, and
   validation expectations.

## Quality Gates

- The user asks for a plan, roadmap, phases, migration sequence, or written
  execution path.
- Requirements are known enough to name affected surfaces, validation, and
  compatibility concerns.
- The work has enough risk, sequencing, or cross-boundary impact that direct
  implementation would hide decisions.
- Planning can produce concrete tasks rather than broad research prompts.

## Hard Stops

- Product behavior, API contract, ownership, or validation expectations are still
  undecided.
- Source context has not been inspected for affected surfaces and existing
  conventions.
- The user asked for immediate implementation rather than a written plan.
- The plan would be a generic phase list without file areas, acceptance checks,
  and validation commands.

## Phase Output

Return:

- Planning scope, non-goals, and affected surfaces.
- Evidence inspected and assumptions accepted.
- Required validation, docs, generated outputs, migration, and compatibility
  concerns.
- Open decisions that block a decision-complete plan.
