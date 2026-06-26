# Diary Finalize

## Overview

Create or report a diary record that future agents can inspect without treating
it as a substitute for source, tests, issues, ADRs, or commits.

## Workflow

### Write Rules

- Use the declared diary script for appends and reads.
- For append operations, provide a short title and at least one summary bullet.
- Prefer separate bullets for actions, decisions, done items, validation,
  blockers, changed files, and next steps instead of a single dense paragraph.
- Use `dry-run` when entry content is uncertain or when the user asked for a
  preview.
- Append only once redaction and qualification decisions are complete.

### Script Patterns

```bash
python3 modules/workflow/memory/diary/scripts/diary.py dry-run --title "<title>" --summary "<summary>"
python3 modules/workflow/memory/diary/scripts/diary.py append --title "<title>" --summary "<summary>"
python3 modules/workflow/memory/diary/scripts/diary.py recent --limit 3
```

## Quality Gates

- Diary content is redacted and scoped to durable work history.
- The script output or written path is captured.
- The entry points to verifiable artifacts when later proof matters.

## Hard Stops

- Do not bypass the script for normal diary writes.
- Do not copy full command logs, secrets, or large diffs into a diary entry.
- Do not claim the diary is authoritative proof; point to commands, files, or
  durable artifacts when verification matters.

## Phase Output

- Diary path written or inspected, or the preview output when no write occurred.
- Summary of redactions, qualifications, and omitted unsafe content.
- Entry title, key facts recorded, and next steps captured.
