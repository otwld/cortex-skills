# Prototype Plan

## Overview

Plan the smallest isolated implementation that can answer the named question.
The contract must prevent prototype code from becoming an accidental production
dependency.

## Workflow

1. State the question and success condition.
2. Name prototype type and isolation boundary.
3. Choose a data strategy, defaulting to in-memory state or fixtures.
4. Provide a runnable command or demo path.
5. List observations to capture and the disposal path: delete, absorb selected
   learning, or discard.

## Quality Gates

- UI comparisons present structurally different variants and the states needed to
  judge them.
- Logic prototypes model transitions, constraints, and edge cases in a portable
  shell.
- Persistence, authentication, backend wiring, and design-system expansion are
  absent unless the specific question requires them.
- Production imports stay one-way and temporary; production code does not depend
  on prototype files.

## Hard Stops

- The plan answers more than one unrelated question.
- Success criteria are subjective without observable states, cases, or command
  output.
- The prototype cannot be removed cleanly.
- The plan lacks a command or demo path.

## Phase Output

Return:

- Prototype implementation plan.
- Command or demo path.
- Evidence to capture and how it answers the question.
- Delete-or-absorb recommendation criteria.
