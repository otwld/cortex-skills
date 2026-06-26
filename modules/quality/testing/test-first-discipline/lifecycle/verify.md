# Test First Discipline Verify

## Overview

Verify that the final tests prove the intended behavior and guard the regression
risk they were chosen for.

## Workflow

1. Run the focused test, affected test file, or nearest targeted suite.
2. Confirm the test name, assertions, and fixture data describe the intended
   behavior in consumer terms.
3. Confirm the test would fail if the implementation reverted to the original bug
   or missing behavior.
4. Confirm broad refactors kept the public behavior proof green.
5. Record any untested risk, unavailable command, or exception to the test-first
   path.

## Quality Gates

- Verification evidence includes the command run and the behavior or regression
  it proves.
- The selected seam is still the highest meaningful public seam available for the
  task.
- Remaining test gaps are explicit and tied to risk, not hidden behind a broad
  passing suite.

## Hard Stops

- Do not report behavior proof from tests that never exercise the changed path.
- Do not rely on type checks, lint, or build success as the only validation for a
  behavior change.
- Do not leave a test-first exception without compensating verification.

## Phase Output

- Return targeted test commands, behavior proven, regression protection, green
  evidence, and remaining test gaps.
