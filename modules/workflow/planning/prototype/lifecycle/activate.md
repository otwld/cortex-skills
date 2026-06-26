# Prototype Activate

## Overview

Confirm that a throwaway prototype is the right way to answer a bounded design,
UI comparison, or state-model question.

## Workflow

1. State the single question the prototype should answer.
2. Identify existing production paths that must remain untouched.
3. Inspect UI states, domain rules, state transitions, or constraints the
   prototype must model.
4. Use `prototype-guidance.md` for isolation, in-memory state, and disposal
   expectations.
5. Define the command, screenshot, fixture, or observation that can prove the
   result.

## Quality Gates

- The goal is learning, comparison, or decision support rather than production
  delivery.
- The prototype can answer one question through a small isolated shell.
- A runnable command or observable demo can prove the result.
- The disposal path can be stated at the start: delete, absorb selected learning,
  or discard.

## Hard Stops

- The request is to ship production behavior, not learn.
- Multiple unrelated questions are bundled into one prototype.
- The prototype would require backend persistence, external credentials, or
  production wiring that the question does not need.
- The result cannot be evaluated by a command, screenshot, fixture, or concrete
  observation.

## Phase Output

Return:

- Prototype question.
- Prototype type: UI comparison, logic/state model, or other isolated shell.
- Isolation boundary, command, and allowed data/state.
- Disposal path and evidence needed to answer the question.
