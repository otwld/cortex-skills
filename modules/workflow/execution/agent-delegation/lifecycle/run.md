# Agent Delegation Run

## Overview

Issue bounded worker briefs, enforce isolation, and integrate returned evidence
without outsourcing the main thread's judgment.

## Workflow

1. Write each worker brief with a complete task statement, allowed files,
   commands, evidence sources, non-goals, forbidden mutations, validation command,
   and report shape.
2. Use `implementer-prompt.md` for isolated implementation,
   `spec-reviewer-prompt.md` for requirement compliance, and
   `code-reviewer-prompt.md` for implementation quality review.
3. Keep one writer per path. Review and investigation workers remain read-only
   unless their brief explicitly permits edits.
4. Inspect cited files, diffs, command output, or screenshots prior to relying on
   a worker conclusion.
5. Reconcile conflicting worker reports by checking primary evidence.

## Quality Gates

- No worker infers missing requirements from another worker's result.
- Secrets, private credentials, and unrelated repository context are not passed to
  workers.
- Generated outputs are mutable only when the brief names the source command and
  generated paths.
- Results lacking citations, file references, or validation evidence are rejected
  rather than integrated.

## Hard Stops

- A worker reports a new design decision, overlapping mutation, or missing
  requirement.
- A worker changed paths outside the brief.
- A worker's validation cannot be reproduced or is inconsistent with the changed
  files.

## Phase Output

Return:

- Worker briefs issued.
- Worker reports received.
- Evidence the main thread rechecked.
- Integrated conclusions, discarded conclusions, and validation still required.
