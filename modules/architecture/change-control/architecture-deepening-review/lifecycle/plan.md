# Architecture Deepening Review Plan

## Overview

Plan architecture deepening only when a clearer interface will hide meaningful
behavior and improve locality, leverage, or testability for current code.

## Workflow

1. Name the behavior the interface should protect.
2. Compare the public interface size to the hidden implementation depth.
3. Classify each dependency using the declared architecture vocabulary.
4. Decide whether to deepen, keep shallow, split responsibilities, or delete an
   unnecessary abstraction.
5. Define the public test surface and the implementation details tests should no
   longer reach.

## Quality Gates

- A deeper module increases locality or leverage for current behavior.
- A wider interface hides substantially more implementation complexity.
- Project memory constraints are applied when present.
- Validation includes tests through the intended public interface.

## Hard Stops

- Do not add adapter seams for speculative future providers.
- Do not treat undocumented assumptions as architecture constraints.
- Do not move behavior behind an interface when callers still coordinate the
  internals themselves.

## Phase Output

- Return the deepen/keep/split/delete decision, behavior to hide, interface
  changes, dependency classifications, test surface, and validation plan.
