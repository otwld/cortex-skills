# Systematic Debugging Verify

## Overview

Verify that the original failure path is closed and the debugging artifacts are
cleaned up.

## Workflow

1. Run the original failing command, reduced reproduction, or closest available
   targeted validation.
2. Run the new regression guard and confirm it covers the original failure mode.
3. Inspect the final diff for temporary diagnostics, widened sleeps, unrelated
   speculative changes, or guards placed only at the crash site.
4. Confirm lower-layer validation exists when upper-layer checks can be bypassed.
5. Record any failure that could not be reproduced and the evidence used instead.

## Quality Gates

- Verification includes the command, reproduction, or trace that proves the
  investigated failure path is handled.
- Regression coverage fails for the original bug or directly asserts the
  corrected invariant.
- Remaining uncertainty is stated as a validation gap, not hidden behind passing
  unrelated tests.

## Hard Stops

- Do not claim a bug is fixed from a broad test pass that never exercises the
  failure path.
- Do not leave temporary diagnostics or probe-only assertions in final code.
- Do not close an unreproduced issue without documenting the localization evidence
  and residual risk.

## Phase Output

- Return verification commands, regression evidence, cleanup confirmation,
  unreproduced gaps, and residual risk.
