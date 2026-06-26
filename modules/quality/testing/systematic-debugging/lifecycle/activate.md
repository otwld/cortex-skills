# Systematic Debugging Activate

## Overview

Identify failure work that needs evidence collection and hypothesis testing
rather than immediate patching.

## Workflow

1. Match this module when the request or repository state contains a failing
   test, build failure, CI failure, runtime bug, performance regression, flaky
   workflow, or unexplained behavior.
2. Capture the visible symptom, expected behavior, actual behavior, failing
   command, logs, traces, stack frames, and environment facts already available.
3. Choose the relevant local reference: root-cause tracing for distant symptoms,
   defense-in-depth for invalid data crossing layers, or condition-based waiting
   for sleeps and flaky readiness.
4. Decide what would count as a useful reproduction, reduction, or localization
   if the failure cannot be reproduced immediately.

## Quality Gates

- Activation evidence includes a concrete failure signal: command output, stack
  trace, log line, failing assertion, repro step, or user-observed symptom.
- The selected reference matches the failure shape instead of being loaded by
  default.
- The first debugging action is evidence-gathering, reproduction, reduction, or
  localization.

## Hard Stops

- Do not activate for planned feature work that has no failure or diagnostic
  request.
- Do not patch code from a hunch when no reproduction, localization, or failure
  evidence has been collected.
- Do not treat increasing a timeout as diagnosis of a flaky async failure.

## Phase Output

- Return the failure evidence, selected reference, reproduction or localization
  plan, and the first hypothesis to test.
