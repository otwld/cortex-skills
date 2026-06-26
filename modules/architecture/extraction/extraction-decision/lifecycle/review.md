# Extraction Decision Review

## Overview

Review extraction changes for stable shared behavior, named ownership, valid
dependency direction, complete caller movement, and preserved local variation.

## Workflow

1. Inspect diffs for duplicated code, extracted surface, caller updates, tests,
   docs, and imports.
2. Inspect remaining copies and whether they represent local variation.
3. Inspect owner and dependency direction for the extracted surface.

## Quality Gates

- The extracted surface has a named owner and current consumers.
- Remaining local copies have intentional variation.
- Consumers use the supported import path.
- Tests cover shared behavior and relevant local variations.

## Hard Stops

- Reject extraction based on similar shape rather than shared behavior.
- Reject new common, shared, helper, or util modules without durable ownership.
- Reject callers moved to a public surface while duplicate private paths remain
  wired.
- Reject dependency direction inverted by the new abstraction.

## Phase Output

- Return extraction findings with affected copies, ownership risks, duplicate
  remnants, dependency-direction defects, and validation evidence.
