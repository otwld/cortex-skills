# Code Documentation Review

## Overview

Review code changes for missing, stale, or misleading documentation that would
mislead a future caller or maintainer.

## Workflow

1. Inspect the diff for public surface changes, dense implementation logic,
   moved code, examples, stories, fixtures, and generated-doc inputs.
2. Compare changed behavior against nearby documentation and comments.
3. Treat missing or stale docs on touched public surfaces as review findings,
   not optional polish.
4. Treat dense logic without intent comments as a finding only when a maintainer
   must infer non-obvious sequencing, invariants, or failure handling from code.
5. Separate required documentation fixes from optional wording improvements.

## Quality Gates

- Findings name the exact surface, the stale or missing claim, and the behavior
  evidence from the diff.
- Required fixes are tied to consumer impact, maintenance risk, or incorrect
  examples.
- Comments that merely restate implementation syntax are called out as noise.

## Hard Stops

- Do not approve a changed public contract while its public docs describe the
  previous contract.
- Do not request comment churn for simple code whose intent is already obvious.
- Do not accept examples or fixtures that contradict the changed behavior.

## Phase Output

- Return review findings ordered by impact, each with the file or surface,
  documentation gap, and required correction.
