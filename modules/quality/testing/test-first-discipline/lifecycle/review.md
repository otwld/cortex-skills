# Test First Discipline Review

## Overview

Review behavior changes for meaningful tests, appropriate seams, and justified
exceptions.

## Workflow

1. Inspect behavior-changing diffs, tests, fixtures, mocks, snapshots, e2e flows,
   and test harness configuration.
2. Check whether at least one test would fail for the original bug or missing
   behavior.
3. Check that assertions observe public outcomes, state transitions, emitted
   events, rendered UI, command output, or integration effects.
4. Flag tests that only pin private implementation or duplicate the implementation
   without proving behavior.
5. Review any skipped test-first step for an explicit reason and compensating
   validation.

## Quality Gates

- Findings name the unproven behavior or regression risk.
- Review distinguishes weak test design from missing coverage.
- Harness changes include a smoke path that would fail if setup were broken.
- Refactor-only changes prove the public contract stayed stable.

## Hard Stops

- Do not approve behavior changes whose only tests assert private implementation
  structure.
- Do not accept a test-first exception that omits residual risk.
- Do not treat snapshot churn as sufficient behavior proof unless the snapshot is
  the reviewed public contract.

## Phase Output

- Return review findings with unproven behavior, weak seam, missing regression, or
  unjustified exception.
