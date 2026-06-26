# Extraction Decision Activate

## Overview

Activate when duplicated logic, DTO shapes, contracts, UI composition,
data-access patterns, or orchestration may deserve an owned abstraction.

## Workflow

1. Read `shared/architecture-deepening.md` when extraction depends on interface
   depth, dependency classification, or whether a seam is justified.
2. Inspect each current copy, its owner, callers, tests, and variation points.
3. Compare whether the repeated code expresses the same behavior or only the same
   shape.
4. Identify dependency direction created by a shared owner.
5. Inspect existing packages or modules that already own the behavior.

## Quality Gates

- Activation evidence includes at least two current consumers or a clear
  owner-level contract need.
- Behavior and variation are compared before matching names or similar structure
  are treated as extraction evidence.
- The possible owner and dependency-direction constraint are named.

## Hard Stops

- Do not extract because code is repeated once.
- Do not create shared, common, helper, or util surfaces without a named owner.
- Do not invert dependency direction to make an extraction convenient.

## Phase Output

- State the duplicated behavior, current copies, consumers, variation points,
  possible owner, dependency-direction constraint, and resource usage.
