# Systematic Debugging Review

## Overview

Review bug fixes for evidence quality, root-cause coverage, and regression
protection.

## Workflow

1. Inspect the reported failure, reproduction notes, logs, traces, and final diff.
2. Check whether the fix changes the earliest responsible boundary or only masks
   the visible symptom.
3. Look for multiple unrelated changes that make the diagnosis unverifiable.
4. Check that temporary diagnostics, debug prints, sleeps, broad retries, or
   widened timeouts are removed or justified.
5. Require a regression guard when behavior changed or a bug path was closed.

## Quality Gates

- Findings cite the failure evidence and the code path that remains unsafe or
  under-proven.
- Review distinguishes missing diagnosis from missing validation.
- Async fixes wait on observable conditions rather than guessed timing.
- Data validation fixes protect all reachable entry points that can violate the
  invariant.

## Hard Stops

- Do not approve a fix that cannot be connected to the reproduced or localized
  failure.
- Do not accept diagnostic leftovers in delivered code unless they are deliberate
  observability.
- Do not accept broad retries, sleeps, or null guards as root-cause fixes without
  evidence that they own the invariant.

## Phase Output

- Return review findings with failure evidence, suspected missed cause,
  diagnostic leftovers, and required regression coverage.
