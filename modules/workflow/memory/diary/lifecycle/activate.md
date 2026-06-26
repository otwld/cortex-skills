# Diary Activate

## Overview

Classify the requested memory action and collect only the facts that should
become durable repo-local work history.

## Workflow

### Inspect

- Determine whether the user asked to append a diary entry, preview an entry, or
  read recent entries.
- Resolve the project root that should own `.diary/YYYY-MM-DD.md`.
- Identify the entry type: work summary, handoff, decision log, validation
  record, blocker note, or next-step record.
- Collect durable facts: scope, actions taken, decisions and reasons,
  validation, blockers, changed files, and follow-up work.
- Screen the source material for credentials, tokens, private keys, unnecessary
  personal data, and unverified claims.

### Decide

- Decide whether the requested memory belongs in the diary or in an
  authoritative artifact such as an issue, ADR, plan, or commit message.
- Decide which facts require qualification because they are inferred, stale, or
  not validated.
- Decide whether to preview using `scripts/diary.py dry-run`, append using
  `scripts/diary.py append`, or inspect entries using `scripts/diary.py recent`.

## Quality Gates

- The diary action, target root, and entry type are explicit.
- Durable facts are separated from assumptions and sensitive material.
- The selected script command matches append, preview, or recent-entry use.

## Hard Stops

- Do not write a diary entry unless the user requested logging, journaling,
  handoff, or durable work history.
- Do not persist secrets, tokens, private keys, credentials, or unnecessary
  personal data.
- Do not record assumptions as durable project truth. Qualify them or omit them.

## Phase Output

- Memory action: append, preview, or recent-entry inspection.
- Target project root and diary path when known.
- Entry facts to include, facts to omit, and facts that need qualification.
- Script command to use or reason no diary write should occur.
