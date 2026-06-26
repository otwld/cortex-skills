
# Output Marker

Display:
using module: systematic-debugging

---

# Systematic Debugging

## Overview

Build a reliable feedback loop before fixing, then test falsifiable hypotheses instead
of guessing.

## Reference Routing

- Use `references/root-cause-tracing.md` when this task touches that concern.
- Use `references/defense-in-depth.md` when this task touches that concern.
- Use `references/condition-based-waiting.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read complete evidence; reproduce; rank hypotheses; probe one variable; fix root cause; add regression; remove instrumentation.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Investigation reproduces or localizes the failure before proposing a fix.
- Hypotheses are ranked and probed one variable at a time with evidence preserved.
- The final fix removes temporary instrumentation and adds a regression guard when behavior changed.

## Example

If Candidate search drops results intermittently, replay one filter fixture until the
failure rate is debuggable before changing query code.

## Hard Stops

- Do not patch symptoms before reproducing, reducing, or localizing the failure.
- Do not change several suspected causes at once unless the evidence already isolates them together.
- Do not leave temporary diagnostics in production code or tests without making them permanent observability.

## Usage Checklist

- Failure evidence, reproduction path, and relevant logs or traces were collected.
- Root-cause hypothesis was tested with the smallest useful probe.
- Fix, regression guard, and cleanup of instrumentation were verified.

## Cross References

- WITH: test-first-discipline, completion-verification, architecture-drift-detector
- AFTER: skill-evolution
