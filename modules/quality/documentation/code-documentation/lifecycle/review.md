# Code Documentation Review

## Overview

Review post-run code changes for missing, stale, or misleading documentation,
then fix required documentation gaps before verification.

## Workflow

1. Inspect the post-run diff for touched public, exported, reusable,
   structural, user-facing, and dense private surfaces.
2. Compare changed behavior against nearby documentation, comments, examples,
   stories, fixtures, payload samples, and generated-doc inputs.
3. Check touched interfaces, type members, properties, schema fields, DTO fields,
   config fields, component contracts, functions, and methods against
   `references/coverage-and-comments.md`.
4. Fix required documentation gaps in place when they are in scope for the
   current task.
5. Treat dense or long logic without useful flow comments as required work when
   a maintainer must infer phases, ordering, invariants, side effects, or
   failure handling from control flow.
6. Separate required documentation fixes from optional wording improvements.

## Quality Gates

- Findings name the exact surface, the stale or missing claim, and the behavior
  evidence from the diff.
- Required fixes are tied to consumer impact, maintenance risk, or incorrect
  examples.
- Required documentation gaps are fixed before the phase reports completion, or
  they name a concrete blocker.
- Comments that merely restate implementation syntax are called out as noise.

## Hard Stops

- Do not approve a changed public contract while its public docs describe the
  previous contract.
- Do not advance to verification while a fixable touched-code documentation gap
  remains.
- Do not request comment churn for simple code whose intent is already obvious.
- Do not accept examples or fixtures that contradict the changed behavior.

## Phase Output

- Return documentation gaps fixed, optional wording changes intentionally
  skipped, and blocked required gaps ordered by impact with the file or surface,
  behavior evidence, and required correction.
