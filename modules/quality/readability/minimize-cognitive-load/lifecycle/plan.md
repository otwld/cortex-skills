# Minimize Cognitive Load Plan

## Overview

Plan code changes so the simplest correct implementation is the default and any
necessary complexity is visible, local, and reviewable.

## Workflow

1. Choose the implementation path that a maintainer can follow with the fewest
   jumps across files, layers, abstractions, and hidden runtime mechanisms.
2. Prefer explicit data flow, early returns, shallow branching, clear names,
   small parameter lists, local helpers, narrow exports, and direct dependency
   wiring.
3. Keep related behavior together unless splitting reduces an actual reader
   burden or another module owns the boundary decision.
4. Reject speculative abstractions, generic utilities, factories, interfaces,
   extension points, configuration options, and public methods that do not solve
   a current repeated problem.
5. Separate readability-only cleanup from feature behavior unless the cleanup is
   required to make the current change correct or reviewable.

## Quality Gates

- The plan names the reader path through the changed code.
- Any new abstraction, file, export, interface, option, or helper has a current
  purpose that reduces reader effort.
- Any retained complexity has a named constraint and an isolation strategy.

## Hard Stops

- Do not add a new abstraction because code might be reused later.
- Do not scatter one feature across layers merely to match a pattern.
- Do not mix broad churn with a feature change when the behavior can be
  reviewed in a smaller diff.

## Phase Output

- Return the chosen simple path, rejected complexity, accepted complexity,
  locality decisions, reviewability constraints, and verification targets.
