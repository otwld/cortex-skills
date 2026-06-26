# Library Placement Decision Review

## Overview

Review placement changes for clear ownership, legal import direction, supported
entry points, and complete caller/test/doc updates.

## Workflow

1. Inspect new or moved files, package metadata, path aliases, public exports, and
   import paths.
2. Inspect tests and docs that mention the old or new location.
3. Count current consumers and owner spread for any new shared surface.
4. Review boundary validation output or the stated reason it was not run.

## Quality Gates

- Every moved or new artifact has one owner class and one supported import path.
- Dependency direction is unchanged or intentionally corrected.
- Tests exercise the owning public surface, not the old file path.
- Obsolete imports, docs, and fixtures have been updated or explicitly ruled out.

## Hard Stops

- Reject new shared libraries without a named owner and current consumers.
- Reject moves that only avoid import friction while behavior still belongs to
  the original owner.
- Reject entry points that mix domain, integration, UI, adapter, and utility
  responsibilities.

## Phase Output

- Return placement findings with file paths, required corrections, remaining
  ownership risks, and validation evidence.
