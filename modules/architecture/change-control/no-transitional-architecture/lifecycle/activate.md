# No Transitional Architecture Activate

## Overview

Activate when a change creates, renames, extracts, moves, or replaces a source of
truth and could leave old and new surfaces reachable at the same time.

## Workflow

1. Read `references/replacement-contract.md` whenever the task changes a source
   of truth or proposes compatibility.
2. Inspect existing implementation, public API, callers, tests, docs, fixtures,
   generated outputs, registrations, providers, factories, routes, events,
   commands, and option names.
3. Identify old names and file paths that consumers can still reach.
4. Inspect any claimed external compatibility contract, release constraint,
   owner, removal condition, and validation.
5. Require a replacement ledger before adding the new architecture surface.

## Quality Gates

- The changed source of truth and old reachable surfaces are named.
- Ledger fields are known or explicitly blocked pending inspection.
- Compatibility is treated as an external contract, not internal caller
  convenience.

## Hard Stops

- Do not create compatibility code to avoid updating internal callers.
- Do not keep old and new implementations wired unless a named external contract
  requires it.
- Do not continue when the replacement ledger cannot identify callers, old names,
  deletion targets, or validation.

## Phase Output

- State the changed source of truth, old reachable surfaces, required ledger
  fields, compatibility exception status, and inspection still missing.
