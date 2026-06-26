# Code Documentation Verify

## Overview

Verify that final documentation, comments, and examples match the code state that
will be delivered.

## Workflow

1. Re-read changed docs, comments, examples, stories, fixtures, and generated-doc
   inputs next to the final code.
2. Confirm every touched public or reusable surface has current ownership,
   constraints, side effects, and failure-mode documentation when those details
   matter to consumers.
3. Confirm dense comments preserve intent or invariants and do not narrate syntax.
4. Search for stale names, import paths, commands, payload fields, and examples
   made invalid by the change.
5. Record the validation command or manual inspection that covered each remaining
   documentation risk.

## Quality Gates

- Documentation validation names the surfaces checked and the files changed.
- No reachable docs describe removed, renamed, or obsolete behavior.
- Any remaining documentation gap has an owner, blocker, and reason it cannot be
  closed in the current task.

## Hard Stops

- Do not report completion while known stale documentation remains unmentioned.
- Do not count tests or type checks as documentation validation unless they
  directly exercise generated docs, examples, or usage snippets.
- Do not leave temporary explanatory notes in code when they should become
  durable public documentation.

## Phase Output

- Return validation evidence, documentation files inspected, unresolved gaps,
  and the exact command or manual check used.
