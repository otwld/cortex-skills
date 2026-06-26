# Architecture Drift Detector Plan

## Overview

Plan the smallest diagnostic response that contains an evidence-backed drift risk
without turning it into unrelated architecture work.

## Workflow

1. Build a drift record from paths, commits, dependency edges, and repeated
   behavior changes.
2. Localize the risk to one owner, module, package, workflow, or project area.
3. Decide whether the next action is no action, a bounded review, a focused
   constraint, or a small ownership correction.
4. Name the validation that will prove the proposed action reduced the risk.

## Quality Gates

- The drift finding includes evidence another reviewer could inspect.
- The recommendation is the smallest constraint that stops the drift from
  continuing.
- Validation uses exact paths, changed symbols, dependency edges, or commit
  identifiers.
- Proposed fixes preserve or narrow ownership and dependency reach.

## Hard Stops

- Do not redesign architecture when evidence only shows unclear churn.
- Do not search the whole repository when the drift record has a scoped area.
- Do not create new abstractions as the first response to unsupported churn.

## Phase Output

- Return the drift record, scoped risk, recommended next action, rejected broader
  actions, and validation plan.
