# Completion Verification Activate

## Overview

Convert a pending success statement into a set of claims that can be checked
against the latest request, the current workspace, and current validation
evidence.

## Workflow

### Inspect

- Read the latest user request, including constraints that arrived later in the
  thread.
- Identify every completion claim that will appear in the response: files
  changed, behavior implemented, validation run, artifact created, issue fixed,
  branch state changed, or blocker resolved.
- Inspect the current workspace state that could contradict the claim:
  modified files, generated files, failed commands, and unfinished edits.
- Identify evidence sources for each claim: command output, file diff, runtime
  observation, review result, or explicit blocker.

### Decide

- Decide which user requirements are satisfied, which are partially satisfied,
  and which remain unverified.
- Decide whether evidence is fresh enough. Earlier command output is stale when
  code, config, generated artifacts, dependencies, or relevant data changed
  afterward.
- Decide whether the final answer may say "done" or must use narrower wording
  such as "implemented but not fully validated."

## Quality Gates

- Every completion claim maps to a user requirement, changed artifact, or
  validation result.
- Evidence freshness is checked against the current workspace.
- Final status wording is constrained by the weakest mandatory evidence.

## Hard Stops

- Do not claim completion from memory, intent, or a successful command that no
  longer matches the current workspace.
- Do not merge several user requirements into one vague pass statement.
- Do not suppress skipped checks, blocked commands, or unverifiable scope.

## Phase Output

- Requirement-to-evidence map for the pending completion claim.
- Evidence that is fresh, evidence that is stale, and checks still missing.
- Allowed final wording for completion, partial completion, or blocked status.
