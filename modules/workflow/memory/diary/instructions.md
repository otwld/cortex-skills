
# Output Marker

Display:
using module: diary

---

# Diary

## Overview

Preserve useful work history without replacing authoritative plans, issues, ADRs, or
commits.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Determine log type; reference existing artifacts; redact sensitive data; record scope, decisions, validation, blockers, and next steps.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Diary entries capture decisions, validation, blockers, and handoff context without exposing secrets.
- Logged facts point to durable artifacts or commands when future agents need to verify them.
- The entry type matches the user request: summary, handoff, decision log, or validation record.

## Example

Log that Candidate search refactor passed validation and link the ADR rather than
copying it.

## Hard Stops

- Do not store sensitive credentials, private tokens, or unnecessary personal data in work history.
- Do not write a diary entry when the user only asked for an immediate answer.
- Do not record unverified assumptions as durable project truth.

## Usage Checklist

- Requested log type and destination were identified.
- Scope, decisions, validation, blockers, and next steps were recorded where relevant.
- Sensitive data and unverifiable claims were omitted or clearly qualified.

## Cross References

- None
