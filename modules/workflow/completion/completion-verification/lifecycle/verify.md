# Completion Verification Verify

## Overview

Check each requirement and completion claim against evidence that can be
inspected again by another agent.

## Workflow

### Verification Method

- Build a short checklist from the latest user request and any explicit
  acceptance criteria.
- For each item, attach one of these evidence types:
  - command result, including command name and outcome;
  - file or diff inspection;
  - runtime or UI observation;
  - durable artifact identifier;
  - explicit blocker and reason no proof exists.
- Re-run focused validation when the last relevant command predates material
  changes.
- Inspect negative space: files that should not change, generated artifacts that
  should not be hand-edited, and requirements that were easy to overlook.

### Failure Modes

- A passing broad validation command masks that a requested artifact was never
  created.
- A final answer says tests passed, but the command failed, was cancelled, or ran
  against an older revision.
- A blocked check is described as unnecessary when it is actually acceptance
  evidence.

## Quality Gates

- Each mandatory requirement has fresh evidence or an explicit blocker.
- Validation commands are rerun when material changes make prior output stale.
- Missing proof is carried into the phase output rather than normalized away.

## Hard Stops

- Stop short of a success claim when any mandatory requirement lacks evidence.
- Stop short of release-readiness wording when validation is blocked or stale.
- Stop and report the contradiction when current files no longer match earlier
  validation output.

## Phase Output

- Checklist of requirements and the evidence attached to each one.
- Commands or inspections run during this phase.
- Missing evidence, blocked checks, and residual risk that must appear in the
  final answer.
