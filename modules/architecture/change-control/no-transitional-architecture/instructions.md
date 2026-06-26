# Output Marker

Display:
using module: no-transitional-architecture

---

# No Transitional Architecture

## Overview

Force a direct replacement when code, APIs, files, events, types, commands, or
module boundaries change. Treat compatibility layers, aliases, shims, fallback
paths, stubs, and old/new side-by-side implementations as defects unless a named
external contract requires them.

## Workflow

1. Inspect the existing implementation, public API, callers, tests, docs, generated outputs, and runtime registrations before adding or renaming architecture surface.
2. If the work creates, renames, extracts, or replaces a source of truth, load `references/replacement-contract.md` and complete the replacement ledger before editing.
3. Edit the existing owner first. Add a new file, type, service, adapter, executor, event, option, registry, or boundary only when the ledger names what it replaces and what will be deleted.
4. Update callers, exports, tests, docs, fixtures, generated outputs, and registrations in the same change so old names stop being reachable.
5. Delete obsolete implementations, compatibility aliases, migration leftovers, temporary wrappers, fake implementations, commented-out code, and unused feature flags before claiming completion.
6. When staged compatibility appears necessary, stop and require the compatibility exception from the reference before continuing.

## Quality Gates

- The final tree has one reachable implementation and one source of truth for the changed behavior.
- Old exports, aliases, event names, option names, routes, executor IDs, schemas, DTOs, tests, fixtures, and docs are removed or explicitly covered by a compatibility exception.
- New architecture surface is justified by current requirements, not by avoiding caller updates.
- Stubs, placeholders, fake implementations, "implement later" code, disabled branches, and dead-code parking are absent.
- Validation includes a search or test that proves obsolete names and duplicate paths are not still wired.

## Hard Stops

- Do not create compatibility aliases, legacy adapters, temporary wrappers, migration shims, fallback paths, or old-name re-exports just to avoid updating callers.
- Do not leave old/new, v1/v2, feed/post, legacy/current, temp/final, backup/live, or experimental/production implementations side by side unless versioning is the product contract.
- Do not add a renamed file beside the old file while the old file remains wired.
- Do not keep old executor IDs, event names, option names, DTO fields, public exports, route names, schemas, fixtures, or docs after a breaking replacement decision.
- Do not use "preserve current behavior" or "backward compatible" as a reason without naming the external consumer, release constraint, owner, removal condition, and validation.
- Do not broaden a focused replacement into a rewrite outside the changed owner and its callers.

## Output Format

When this module changes the recommendation, output the replacement ledger:
obsolete path, replacement path, callers to update, obsolete names/files to
delete, compatibility exception or `none`, and validation proving no side-by-side
path remains.

## Usage Checklist

- Existing implementation, public API, callers, tests, docs, generated outputs, and registrations were inspected.
- Replacement ledger was completed before new architecture surface was added.
- Callers and public exports moved to the replacement in the same change.
- Obsolete names, files, events, options, schemas, fixtures, and docs were deleted or blocked by a compatibility exception.
- Validation proves only one reachable implementation/source of truth remains.

## Cross References

- Reference: `references/replacement-contract.md`
