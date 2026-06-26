# Replacement Contract

Use this reference when a change creates, renames, extracts, replaces, or moves a
source of truth. The goal is to prevent partial migrations and old/new paths from
coexisting by accident.

## Replacement Ledger

Complete this before editing:

```md
Replacement Ledger
- Existing source of truth:
- Replacement source of truth:
- Callers to update in this change:
- Public names to remove:
- Files/tests/docs/fixtures to delete or rewrite:
- Compatibility exception: none
- Validation proving no side-by-side path remains:
```

If any required line is unknown, inspect the repository before continuing. If it
is still unknown after inspection, stop and ask for the missing decision.

## Compatibility Exception

Use this only when immediate deletion is blocked by a named external contract.

```md
Compatibility Exception
- External consumer or release contract:
- Owner:
- Removal condition:
- Maximum lifetime:
- Validation preventing old/new divergence:
```

Internal caller churn, test updates, broad refactor cost, or uncertainty are not
compatibility exceptions.

## Deletion Audit

Before claiming completion, search for the removed surface by exact old names:

- file names and folder names
- exported symbols and public entry points
- command names, executor IDs, route names, event names, and option names
- DTO/schema fields and fixture keys
- docs examples, README snippets, comments, and tests
- registration maps, dependency injection providers, factories, and registries

Expected remaining matches are either zero or explicitly named in the
compatibility exception.

## Examples

Bad:

- Add `CandidateSearchV2Service` while `CandidateSearchService` remains wired.
- Export `linkedInPostExecutor` while keeping `linkedInFeedExecutor` as an alias.
- Keep `candidateName` and `candidate.fullName` in the same DTO for internal
  callers.
- Add a resolver that returns placeholder `SkillTag[]` values until parsing is
  implemented later.

Good:

- Rename `CandidateSearchService` to `CandidateMatchingService`, update all
  providers and tests, and delete the old export in the same change.
- Replace `candidateName` with `candidate.fullName`, update fixtures and API
  examples, and search for `candidateName` before completion.
- Move `ApplicationStatusChanged` events to a new owner, update publishers and
  subscribers, and delete the old event registration.
