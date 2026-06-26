# Systematic Debugging Run

## Overview

Build a reliable feedback loop, test one hypothesis at a time, and fix the
earliest responsible cause.

## Workflow

1. Reproduce the failure, reduce it, or localize it to a boundary narrow enough
   to test a hypothesis.
2. Rank hypotheses by evidence and choose one variable to probe.
3. Add temporary diagnostics only when static reading and existing logs cannot
   distinguish hypotheses; remove them or convert them into intentional
   observability.
4. Fix the earliest owner of the invalid state, missing invariant, race, or
   incorrect assumption.
5. Add a regression guard that fails for the original behavior when behavior
   changed.
6. For async readiness issues, wait for the condition that proves readiness and
   include a timeout message that names the missing condition.

## Quality Gates

- The investigation records symptom, reproduction or localization path,
  hypothesis, probe, and conclusion.
- Only one suspected cause changes per probe unless the evidence already proves a
  coupled cause.
- The fix addresses the source of bad state, not only the line where it crashed.
- Temporary diagnostics are removed or intentionally retained as permanent
  observability.

## Hard Stops

- Do not patch only the visible failure site when earlier code can still pass
  invalid state into it.
- Do not combine unrelated fixes during diagnosis.
- Do not replace a flaky sleep with a larger sleep unless the test is explicitly
  verifying elapsed time.

## Phase Output

- Return the reproduction path, hypotheses tested, root cause, code change,
  regression guard, and diagnostics cleanup.
