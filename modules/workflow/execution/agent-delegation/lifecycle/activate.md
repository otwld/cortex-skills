# Agent Delegation Activate

## Overview

Decide whether work can be assigned to isolated workers while the main thread keeps
ownership of decisions, integration, and final validation.

## Workflow

1. Inspect the user request, current plan, or review objective that might be split.
2. Identify the files, APIs, docs, and commands each worker would need.
3. Check current dirty-tree state for any path a worker might edit.
4. Select the matching prompt reference: `code-reviewer-prompt.md`,
   `implementer-prompt.md`, or `spec-reviewer-prompt.md`.
5. Record mutation boundaries and the evidence the main thread must re-check.

## Quality Gates

- Each candidate task has a bounded input, explicit non-goals, and a verifiable
  output format.
- Workers do not need another worker's uncommitted changes, private context, or
  live decisions.
- At most one worker is allowed to mutate a given path or public contract.
- The main thread can name the evidence it must re-check once results return.

## Hard Stops

- A delegated task would decide product behavior, API shape, ownership, or
  acceptance criteria that the main thread has not settled.
- Multiple workers need to edit the same file, generated artifact, migration, or
  public contract.
- The work requires secrets, local credentials, or external state that is not
  already available to the main thread.
- The expected result cannot be verified from cited files, commands, or concrete
  observations.

## Phase Output

Return:

- Delegation decision: `use workers` or `keep in main thread`.
- Candidate worker tasks, each labeled `read-only`, `implementation`, `spec
  review`, or `code review`.
- Required prompt reference for each task.
- Mutation boundaries, evidence sources, validation commands, and integration
  checks the main thread must perform.
