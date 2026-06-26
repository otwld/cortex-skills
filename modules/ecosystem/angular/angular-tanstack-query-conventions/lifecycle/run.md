# Angular TanStack Query Conventions Run

## Overview

Implement Angular TanStack Query changes so cache identity, disabled-query
behavior, mutations, and Angular consumption remain predictable.

## Workflow

- Build query keys as arrays that include every variable used by the query
  function that can change the server result or cache partition. Include
  authorization and tenant boundaries when they affect returned data.
- Put pagination cursors, page numbers, page size, search text, sort, filters,
  and feature flags in the key when they change results.
- Keep query key segments stable and serializable. Prefer a shared key factory
  or query option helper for reused keys, prefetching, cache reads, and tests.
- Use `queryOptions` or the local equivalent when extracting query options so
  type inference stays attached to the key and query function.
- Make skippable inputs explicit. Use `skipToken` only when the query should not
  support manual `refetch()` while skipped; otherwise use an enabled condition
  and guard the query function.
- Convert Angular `HttpClient` observables to the promise shape expected by the
  query function intentionally, and preserve cancellation behavior when the
  local HTTP abstraction supports it.
- Define mutations through `injectMutation` or local mutation option helpers.
  Name mutation variables, success/error/pending states, affected query keys,
  invalidation specificity, and rollback behavior for optimistic updates.
- Prefer targeted invalidation or precise cache writes over broad cache clearing.
  Prefix invalidation must be intentional and should name the full query family
  it refreshes.
- Keep components consuming query state through the returned query object or
  stable derived Angular state. Do not duplicate query cache data into ad hoc
  component fields without a synchronization reason.
- In tests, create a fresh `QueryClient` per spec or clear it between specs, turn
  off retries for deterministic failure tests, and wait for Angular stability or
  the local test helper that settles query work.

## Quality Gates

- Exercise cache identity by changing at least one filter, page, tenant, or ID
  that should produce a distinct query result.
- Exercise skip behavior for missing inputs and, when supported, manual refetch.
- Exercise mutation success and error paths enough to prove invalidation,
  optimistic rollback, and user-visible state.

## Hard Stops

- Do not reuse a key across different server results, users, tenants, filters,
  pagination windows, or authorization-sensitive data.
- Do not pass nullable values into a query function as the only disabled-query
  guard.
- Do not mutate cache state without naming the exact query keys or key prefixes
  affected.

## Phase Output

Return the files changed, final key shapes, skip/refetch behavior, mutation
cache impact, and targeted validation evidence.
