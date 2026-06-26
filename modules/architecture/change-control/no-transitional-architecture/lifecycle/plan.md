# No Transitional Architecture Plan

## Overview

Plan direct replacement so the final tree has one reachable implementation and
one source of truth for the changed behavior.

## Workflow

1. Complete the ledger from `references/replacement-contract.md`.
2. Edit the existing owner first; add new files or names only when the ledger
   names what they replace and what will be deleted.
3. Update callers, exports, tests, docs, fixtures, registrations, and examples in
   the same change.
4. Delete obsolete aliases, wrappers, stubs, fallback paths, fake
   implementations, dead branches, and commented-out old code.
5. Search exact old file names, symbols, route names, event names, option names,
   DTO fields, schema keys, fixture keys, and docs examples.

## Quality Gates

- The ledger names existing source, replacement source, callers, public names to
  remove, deletion targets, compatibility status, and validation.
- Expected remaining old-name matches are zero or listed in a compatibility
  exception.
- Narrow tests or type checks cover callers moved to the replacement.

## Hard Stops

- Do not edit when any required ledger line is unknown after inspection.
- Do not keep compatibility for internal churn, test updates, broad refactor
  cost, or uncertainty.
- Do not claim completion without deletion searches for obsolete surfaces.

## Phase Output

- Return the completed ledger, edit order, deletion list, compatibility exception
  or `none`, and validation commands or searches.
