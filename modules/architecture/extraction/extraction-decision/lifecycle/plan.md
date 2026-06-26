# Extraction Decision Plan

## Overview

Plan extraction only when stable shared behavior can move to a named owner
without creating a shallow or direction-breaking abstraction.

## Workflow

1. Inventory all copies and consumers.
2. Separate stable shared behavior from local variation and coincidental shape.
3. Choose one outcome: keep local, consolidate in an existing owner, extract a new
   owned surface, or split the candidate.
4. Define the public API only after ownership and dependency direction are clear.
5. Plan caller updates, deletion of replaced copies, tests, docs, and validation.

## Quality Gates

- The chosen owner can support the behavior for all current consumers.
- The extraction reduces duplication or responsibility spread.
- Tests prove the shared behavior once and preserve local variations where they
  remain.
- Import searches show consumers moved to the chosen public surface.

## Hard Stops

- Do not extract feature-specific UI, local orchestration, or one-off adapters.
- Do not create a new package when an existing owner already fits.
- Do not leave removed duplicate copies wired unless they are documented local
  variation.

## Phase Output

- Return the extraction decision, owner, public surface, consumers to update,
  code to keep local or delete, risks, and validation plan.
