# Architecture Drift Detector Review

## Overview

Review drift findings for inspectable evidence, bounded scope, preserved
ownership, and validation that the repeated-change path is contained.

## Workflow

1. Inspect diff or commit evidence named by the drift record.
2. Inspect ownership and dependency changes introduced by the fix.
3. Inspect tests, lint, graph checks, or searches used to confirm the risk is
   contained.

## Quality Gates

- Every drift claim has inspectable evidence.
- The response is scoped to the named area and current risk.
- Dependency direction and ownership are preserved or intentionally corrected.
- Validation demonstrates the repeated-change path is reduced or contained.

## Hard Stops

- Reject drift claims based only on file count, size, or preference.
- Reject recommendations that do not name the affected owner or dependency edge.
- Reject fixes that add new layers while leaving the repeated-change source
  untouched.
- Reject scope expansion into unrelated architecture cleanup.

## Phase Output

- Return drift-review findings with evidence paths, unsupported claims, scope
  risks, and validation status.
