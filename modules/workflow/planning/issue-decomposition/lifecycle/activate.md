# Issue Decomposition Activate

## Overview

Confirm that broad work should be decomposed into independently verifiable
vertical slices, agent briefs, or issue-tracker items.

## Workflow

1. Read the PRD, plan, roadmap, user request, or design artifact to decompose.
2. Inspect source context for current behavior, affected interfaces, tests, and
   ownership.
3. Use `vertical-slices.md` for slice quality.
4. Use `agent-briefs.md` for AFK implementation contracts.
5. Use `issue-tracker-setup.md` for publishing mode, labels, and tracker rules.

## Quality Gates

- The work contains multiple behaviors, acceptance areas, or implementation units.
- The desired output is issues, briefs, slices, or tracker-ready work items.
- Enough source context exists to describe current behavior and expected behavior.
- Tracker publishing is configured, or local markdown output is acceptable.

## Hard Stops

- Core product, API, ownership, or validation decisions are still open.
- The request can be handled as one small implementation task.
- Source context is insufficient to write independently verifiable acceptance
  criteria.
- The user expects issue publishing but tracker mode, project identifier, or
  labels are unavailable.

## Phase Output

Return:

- Decomposition scope and source evidence inspected.
- Publishing mode: tracker, local markdown, or blocked.
- Candidate behaviors to slice.
- Decisions or tracker setup gaps that block decomposition.
