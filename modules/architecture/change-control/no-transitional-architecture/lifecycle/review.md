# No Transitional Architecture Review

## Overview

Review replacement work for one reachable implementation, deleted obsolete
surfaces, direct caller updates, and validated absence of side-by-side paths.

## Workflow

1. Inspect the replacement ledger and any compatibility exception.
2. Inspect diffs for old and new files, exports, routes, events, options, DTO
   fields, schemas, fixtures, docs, generated outputs, providers, factories, and
   registrations.
3. Review exact searches for obsolete names and validation output for updated
   callers.

## Quality Gates

- One reachable implementation and one source of truth remain.
- Obsolete public names and internal registrations are deleted or covered by a
  complete compatibility exception.
- Callers and tests use the replacement directly.
- Searches for old names are clean or every remaining match is justified.

## Hard Stops

- Reject old and new implementations, APIs, files, events, options, routes, or
  DTO fields that remain reachable without an external compatibility contract.
- Reject aliases, wrappers, shims, fallbacks, stubs, placeholders, or legacy
  adapters used to avoid caller updates.
- Reject ledgers that omit callers, deletion targets, or validation.

## Phase Output

- Return replacement findings with obsolete surfaces, missing deletions,
  compatibility defects, search results, and required corrections.
