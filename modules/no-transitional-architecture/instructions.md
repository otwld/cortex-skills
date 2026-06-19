# Output Marker

Display:
using module: no-transitional-architecture

---

# No Transitional Architecture

## Overview

Keep the repository moving toward the architecture that should exist now. Prefer
replacing, deleting, and completing migrations over preserving old behavior with
extra layers.

## Workflow

1. Inspect existing implementation, callers, tests, docs, and public boundaries before adding a new artifact.
2. Prefer modifying existing code over adding a parallel path.
3. Replace obsolete implementations and update callers in the same change.
4. Delete dead code, temporary wrappers, migration leftovers, commented-out code, and unused feature flags.
5. Collapse duplicate sources of truth instead of synchronizing them.
6. Add abstractions only when current usage justifies them, not to avoid touching existing code.
7. If transitional code appears necessary, stop and state the concrete compatibility constraint, owner, removal condition, and validation path.

## Quality Gates

- The final design has one implementation and one source of truth for the changed behavior.
- Migrations are finished in the same change unless the user or an external contract explicitly requires staging.
- New files, services, interfaces, adapters, factories, registries, and feature flags are justified by current requirements.
- Placeholders, fake implementations, and "implement later" code are absent unless the user explicitly approves a stub.
- Compatibility is preserved only for named external consumers, release constraints, or public contracts.

## Hard Stops

- Do not create compatibility layers, legacy adapters, temporary wrappers, migration shims, or fallback paths just to avoid updating callers.
- Do not leave old/new, v1/v2, legacy, temp, backup, or experimental implementations side by side unless versioning is the actual product contract.
- Do not keep obsolete code, disabled branches, unused abstractions, or "just in case" paths.
- Do not broaden the change into an architecture rewrite when a focused replacement or deletion solves the problem.

## Output Format

When this module changes the recommendation, name the obsolete path to remove,
the replacement path, any callers that must be updated, and any explicit
compatibility constraint that prevents immediate deletion.

## Usage Checklist

- Existing implementation and callers were inspected.
- Replacement or modification was considered before addition.
- Dead code and duplicate paths were removed or explicitly blocked by a named constraint.
- Any staged compatibility path has an owner, removal condition, and validation evidence.
- The repository ends with less architectural surface area than before.

## Cross References

- None
