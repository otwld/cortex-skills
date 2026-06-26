# Review Feedback Triage Review

## Overview

Classify technical feedback into evidence-backed dispositions prior to changing
code or responding to the reviewer.

## Workflow

### Inspect

- Read the exact feedback text, line reference, CI log, or suggested patch.
- Inspect the relevant code, tests, docs, configuration, and current diff.
- Check whether the feedback still applies to the current branch state.
- Identify the underlying concern: correctness, test coverage, public contract,
  maintainability, security, documentation, performance, or style preference.

### Dispositions

- `apply`: the feedback is correct and the requested fix is appropriate.
- `adapt`: the concern is valid, but a different fix better matches the codebase.
- `defer`: the concern is valid but outside the requested scope or needs product
  direction.
- `reject`: the concern is contradicted by code, tests, requirements, or current
  behavior.
- `clarify`: the feedback cannot be verified from available evidence.

### Review Checks

- Every disposition must cite the evidence inspected.
- Applied or adapted fixes must stay scoped to the reviewer concern.
- Re-run focused validation for changed behavior, or record the blocked check.
- Reviewer responses must address the technical concern, not the person or the
  process.

## Quality Gates

- Each feedback item receives one evidence-backed disposition.
- Fixes stay scoped to the reviewed concern.
- Reviewer responses cite technical evidence or the clarification needed.

## Hard Stops

- Do not implement feedback blindly when the claim is unverified, outdated, or
  ambiguous.
- Do not reject feedback unless the contradiction is backed by concrete
  evidence.
- Do not turn triage into broad cleanup unrelated to the reviewed concern.

## Phase Output

- Feedback items grouped by disposition.
- Evidence for each item and the planned action.
- Fixes applied, validation run, blocked checks, and response text when needed.
