# Test First Discipline Run

## Overview

Use tests as the feedback loop that defines behavior, then implement the smallest
change that satisfies that proof.

## Workflow

1. Write or update one focused test that expresses the target behavior through the
   chosen public seam.
2. Run the focused test and capture the red state when practical; for regression
   work, the test should fail against the original bug.
3. Implement the smallest behavior change that makes the test pass.
4. Refactor only once the behavior proof is green and still protects the public
   contract.
5. For test harness or framework setup, add a smoke path that proves the harness
   can execute representative project code.
6. When test-first is not feasible, record the exception, reason, and compensating
   validation.

## Quality Gates

- The test asserts externally meaningful behavior rather than private call order,
  storage shape, or incidental implementation structure.
- The red or newly relevant state is captured, or the exception explains why it
  could not be observed.
- Implementation remains scoped to the behavior under test.
- Refactors retain the behavior proof and do not widen the change without new
  evidence.

## Hard Stops

- Do not implement behavior first and add a test only as a retrospective checkbox
  unless an exception is recorded.
- Do not pin mocks, snapshots, or private helpers when a public outcome is
  observable.
- Do not continue broad refactoring while the behavior proof is absent or failing.

## Phase Output

- Return the behavior test, red or newly relevant evidence, implementation scope,
  green validation, and any test-first exception.
