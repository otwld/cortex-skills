# Code Documentation Verify

## Overview

Verify that final documentation, comments, and examples satisfy the required
documentation standard for the code state that will be delivered.

## Workflow

1. Re-read changed docs, comments, examples, stories, fixtures, and
   generated-doc inputs next to the final code.
2. Confirm every touched public, reusable, structural, user-facing, or behavioral
   surface satisfies `references/coverage-and-comments.md`.
3. Confirm touched interfaces, type members, properties, schema fields, DTO
   fields, config fields, component contracts, functions, and methods have
   current ownership documentation plus any relevant constraints, side effects,
   and failure modes.
4. Confirm named functions and methods over five body lines are documented.
5. Confirm long and dense function comments preserve flow, intent, or invariants
   and do not narrate syntax.
6. Search for stale names, import paths, commands, payload fields, and examples
   made invalid by the change.
7. Record the validation command or manual inspection that covered each remaining
   documentation risk.

## Quality Gates

- Documentation validation names the surfaces checked and the files changed.
- No reachable docs describe removed, renamed, or obsolete behavior.
- No touched required surface from the coverage standard remains undocumented
  without a concrete blocker.
- Any remaining documentation gap has an owner, blocker, and reason it cannot be
  closed in the current task.

## Hard Stops

- Do not report completion while known stale documentation remains unmentioned.
- Do not count tests or type checks as documentation validation unless they
  directly exercise generated docs, examples, or usage snippets.
- Do not leave temporary explanatory notes in code when they should become
  durable public documentation.

## Phase Output

- Return validation evidence, touched surfaces checked, documentation files
  inspected, unresolved gaps, and the exact command or manual check used.
