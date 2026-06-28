# Minimize Cognitive Load Run

## Overview

Implement code so intent, inputs, outputs, side effects, and failure paths are
visible at the point where a maintainer reads the change.

## Workflow

1. Write the straightforward version first, then introduce complexity only when
   correctness, an external contract, a framework requirement, or measured
   performance need requires it.
2. Keep control flow linear with guard clauses, shallow nesting, explicit
   branches, focused `try` scopes, and named intermediate values where they
   clarify intent.
3. Keep data flow visible from input to transform to output; avoid routing one
   feature through unnecessary helpers, managers, services, factories, or hidden
   global state.
4. Keep dependencies visible through imports, parameters, constructors, or
   explicit providers; avoid surprising mutation, magic configuration, and
   implicit execution paths.
5. Remove unused options, parameters, exports, hooks, callbacks, extension
   points, and abstractions introduced by the change unless another module
   requires them.

## Quality Gates

- A reader can identify what changed, why it exists, and how data moves through
  the touched code.
- New files, helpers, abstractions, exports, and configuration options are
  necessary for today's behavior.
- The implementation follows local project conventions unless a simpler local
  deviation is explicitly justified.

## Hard Stops

- Do not compress code into dense expressions that hide branching, side effects,
  or error handling.
- Do not create manager, helper, util, common, or processor-style code without a
  precise role.
- Do not remove clarity comments or documentation that explain non-obvious
  intent, invariants, ordering, or side effects.

## Phase Output

- Return simplifications made, complexity retained, public surface minimized,
  noisy changes avoided, documentation or comment coordination, and validation
  commands or checks.
