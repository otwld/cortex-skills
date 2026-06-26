# Issue Decomposition Plan

## Overview

Convert broad work into slices or briefs that can be checked independently and
published only through configured tracker rules.

## Workflow

1. Prefer thin end-to-end behavior over database-only, API-only, UI-only, or
   tests-later work.
2. For each issue or agent brief, capture current behavior, desired behavior, key
   interfaces, acceptance criteria, validation, out-of-scope items, blockers, and
   dependency notes.
3. Classify each slice as AFK-ready only when requirements, interfaces,
   acceptance criteria, validation, and out-of-scope items are settled.
4. Use human-in-loop classification when product review, credentials, production
   access, or design approval is required.
5. Publish only through configured tracker mode, project identifier, and label
   map; otherwise produce local markdown briefs.

## Quality Gates

- Each slice is independently verifiable and names blockers.
- Briefs avoid fragile line numbers and file paths unless the target is a stable
  public entry point.
- Labels map to configured canonical roles; labels are not invented in chat.
- Publishing gaps are reported as missing tracker setup.

## Hard Stops

- A slice is only a technical layer when a vertical slice is possible.
- A brief still asks the implementer to make product, API, or validation choices.
- Acceptance criteria depend on another unimplemented slice without naming that
  dependency.
- Tracker publishing would use unconfigured labels, project IDs, or permissions.

## Phase Output

Return:

- Ordered slices or issue briefs.
- AFK-ready versus human-in-loop classification and reason.
- Acceptance criteria and validation evidence per slice.
- Publishing result or local markdown fallback.
