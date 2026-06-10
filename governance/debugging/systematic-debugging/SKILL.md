---
name: systematic-debugging
description: Use when encountering bugs, failing tests, build failures, performance problems, or unexpected behavior before proposing fixes.
---

# Output Marker

Display:
using skill: systematic-debugging

---

# Systematic Debugging

## Overview

Find the root cause before fixing symptoms. Guessing may look fast, but it
usually creates extra changes and weaker evidence.

## Workflow

1. Read the complete error, log, stack trace, or failing assertion.
2. Reproduce the failure or gather enough evidence to explain why it is not
   reproducible.
3. Check recent changes and environment differences.
4. Trace the failing data or control flow to the source.
5. Compare with nearby working examples or documented patterns.
6. Form one hypothesis and test it with the smallest possible change or probe.
7. Add a regression test or documented reproduction before the final fix when
   feasible.

## References

Load only when needed:

- `references/root-cause-tracing.md` for failures deep in a call stack.
- `references/defense-in-depth.md` after invalid data reaches dangerous code.
- `references/condition-based-waiting.md` for flaky async or timing tests.

## Escalation

If three reasonable fix attempts fail, stop and question the architecture,
assumptions, or test model before trying another patch.

## Hard Stops

- A fix is proposed before the failure is understood.
- Multiple fixes are bundled into one untestable change.
- A test failure is handled by relaxing expectations without proving behavior
  changed intentionally.

## Usage Checklist

- Failure evidence was read and summarized.
- Reproduction or evidence gap is known.
- Root cause hypothesis is explicit.
- Fix addresses the source, not only the symptom.
- Regression or verification path is named.

## Cross-References

- WITH: test-first-discipline, completion-verification, architecture-drift-detector
- AFTER: skill-evolution
