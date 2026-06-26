# Design Intake Activate

## Overview

Determine whether the request lacks enough stable intent to plan or edit without
choosing user-visible behavior on the user's behalf.

## Workflow

1. Read the user's exact words for desired outcome, target artifact, audience,
   constraints, and success criteria.
2. Inspect existing source, docs, memory, examples, generated artifacts, and tests
   that can answer context questions.
3. Check similar screens, APIs, modules, commands, or naming conventions already
   present in the repository.
4. Separate repository facts from assumptions, preferences, and unresolved user
   choices.
5. Identify the smallest set of questions whose answers would change the outcome.

## Quality Gates

- The target result, audience, task type, success criteria, or non-goals are
  missing or conflict with repository evidence.
- The request affects public behavior, UX, architecture, data contracts, or
  workflow semantics.
- A reasonable implementation path would differ depending on the missing answer.
- The missing answer cannot be recovered from repository facts.

## Hard Stops

- Do not ask the user for file locations, commands, conventions, or current
  behavior that can be inspected locally.
- Do not convert uncertain intent into an implementation plan.
- Do not proceed on an assumption that would change public behavior, data shape,
  permissions, or compatibility.
- Do not ask broad preference questions when one blocking decision is enough.

## Phase Output

Return:

- Known facts, each tied to source evidence or user text.
- Unknowns that still affect the outcome.
- Clarifying questions limited to decision-changing gaps.
- Recommended defaults for preference choices the repository cannot decide.
