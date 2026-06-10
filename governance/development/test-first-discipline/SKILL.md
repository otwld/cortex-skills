---
name: test-first-discipline
description: Use before behavior changes, bug fixes, or refactors where tests can prove the intended behavior or regression.
---

# Output Marker

Display:
using skill: test-first-discipline

---

# Test First Discipline

## Overview

Prefer a failing test before changing production behavior. The goal is not
ceremony; it is proof that the test can catch the missing behavior or regression.

## Workflow

1. State the behavior or regression to prove.
2. Write the smallest meaningful failing test.
3. Run the focused test and confirm it fails for the expected reason.
4. Implement the minimal change.
5. Run the focused test again, then the relevant broader suite.
6. Refactor only after tests are green.

## Safe Exceptions

Document the reason when test-first is impractical:

- Configuration-only changes.
- Generated code.
- Throwaway prototypes.
- Legacy seams where characterization tests must come first.
- Behavior that can only be validated manually or externally.

For existing untested code, prefer characterization or regression tests before
changing behavior. Do not delete user work to enforce test-first discipline.

## Hard Stops

- A bug fix has no reproduction or regression check.
- A behavior change is claimed complete without a relevant test or documented
  exception.
- Tests pass immediately and do not prove missing behavior.

## Usage Checklist

- Desired behavior or regression is named.
- The test failed for the expected reason before implementation, or an exception
  is documented.
- The focused test passes after the change.
- Relevant broader validation was run or deferred with reason.

## Cross-References

- WITH: systematic-debugging, completion-verification, jest-conventions, vitest-conventions, playwright-conventions
