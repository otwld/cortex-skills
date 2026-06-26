# Library Placement Decision Activate

## Overview

Activate when a task adds, moves, extracts, or shares code and the durable owner
or package location is not already settled by surrounding files.

## Workflow

1. Inspect the behavior, data shape, UI, adapter, or utility being placed.
2. Inspect existing owners in nearby directories, package metadata, path aliases,
   public entry points, and tests.
3. Identify current and expected consumers, including whether they live in one
   feature, one domain, one integration, or multiple owners.
4. Classify the responsibility as domain, integration, feature, UI, adapter,
   utility, or test-only support.
5. Check the import direction created by the proposed location.

## Quality Gates

- Activation evidence names an artifact, current owner candidates, consumers,
  and dependency-direction impact.
- Local edits inside a settled owner are marked out of scope unless the request
  also proposes moving, sharing, or extracting.
- The responsibility class is chosen before location advice is given.

## Hard Stops

- Do not create a shared package for convenience without stable consumers and a
  named owner.
- Do not move code across a boundary merely to shorten imports or avoid tests.
- Do not hide mixed responsibilities in a broad common library.

## Phase Output

- State the artifact being placed, matched ownership evidence, likely owner
  class, dependency-direction constraint, and repository files still needing
  inspection.
