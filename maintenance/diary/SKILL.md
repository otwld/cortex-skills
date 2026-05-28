---
name: diary
description: Use when the user asks to log, journal, summarize, hand off, or preserve agent work history, decisions, blockers, validations, or completed outcomes.
---

# Output Marker

Display:
using skill: diary

---

# Diary

## Overview

Use diary entries to preserve durable project history for AI-assisted work. Keep
entries concise, summary-first, append-only, and safe to commit.

## Operating Policy

- Write entries for important actions, decisions, blockers, validations, handoffs, and user preference changes.
- Do not log every turn, transient thought, raw transcript, or long command output.
- Redact credentials, tokens, private keys, auth headers, passwords, and other sensitive values.
- Prefer summaries over raw code or private conversation text.
- If writing fails, report the failure and include the would-be summary in the response.

## Readback

Read recent diary entries when they materially improve continuity:

- The user asks to resume, continue, reconstruct, or explain previous work.
- Current work depends on prior agent decisions.
- Context appears missing or contradictory and diary files exist.

Use:

```bash
python3 scripts/diary.py recent --repo path/to/target-project --limit 3
```

from this skill directory. Always pass `--repo` when the diary should belong to
a project other than the current working directory.

## Writing Entries

Preview without writing:

```bash
python3 scripts/diary.py append --dry-run \
  --repo path/to/target-project \
  --title "Preview entry" \
  --summary "Show the diary format before writing."
```

Append an entry:

```bash
python3 scripts/diary.py append \
  --repo path/to/target-project \
  --title "Updated skill library" \
  --summary "Reworked reusable skills and validated the structure." \
  --action "Updated skill metadata." \
  --validation "scripts/validate-skills.py passed"
```

## Entry Shape

The script writes `.diary/YYYY-MM-DD.md` and appends stable Markdown sections:

- Summary
- Actions
- Decisions
- Done
- Validation
- Blockers
- Changed Files
- Next

`Summary`, `Blockers`, and `Next` are always present. Other sections appear
only when supplied.

## Usage Checklist

- Entry captures durable context, not routine chatter.
- Sensitive values are redacted.
- Validation commands and outcomes are included when relevant.
- Old entries are not rewritten unless the user asks.

## Cross-References

- None
