# Angular TanStack Query Conventions Activate

## Overview

Decide whether Angular TanStack Query conventions apply and capture the data
contract that determines cache identity, skip behavior, and mutation effects.

## Workflow

1. Match the request or diff to TanStack Query Angular providers, query APIs,
   cache APIs, mutation APIs, or query tests.
2. Inspect installed package import path, `QueryClient` setup, and existing key
   or option helpers.
3. Enumerate every server-result input and authorization partition.
4. Decide the skip/refetch behavior and mutation cache impact.
5. Return unresolved cache identity or test isolation gaps instead of guessing.

## Trigger Evidence

Activate for requests or diffs that touch TanStack Query Angular providers,
`injectQuery`, `injectMutation`, query keys, query option helpers, mutation
option helpers, `QueryClient` cache reads or writes, invalidation, pagination,
filtering, optimistic updates, or query tests.

Do not activate for Angular services that fetch data without TanStack Query or
for state management that never reaches the query cache.

## Inspect

- Installed TanStack Query Angular package and import path, plus the application
  `QueryClient` provider and default options.
- Existing query key factories, query option helpers, mutation option helpers,
  service abstractions, and component consumption patterns.
- Every input that can change the server result: tenant, company, job offer,
  user, permissions, filters, sort, search, page, cursor, locale, and feature
  flags.
- Skippable input rules, such as missing IDs or filters, and whether manual
  `refetch()` is expected.
- Mutation side effects: affected query families, optimistic updates, rollback
  data, invalidation specificity, and user-visible pending/error states.
- Tests that create a `QueryClient`, await query completion, stub HTTP, or share
  cache across specs.

## Decisions

- Treat the query key as the cache identity for the server result, not as a
  label for the component using it.
- Use the local package API and import path. Do not mix experimental and stable
  TanStack Query Angular imports in the same change.
- Use shared query option helpers when options are consumed by components,
  prefetching, cache reads, or tests.
- Choose `skipToken` only when type-safe disabling is needed and no manual
  `refetch()` behavior is required; choose an explicit enabled condition when
  manual refetch remains part of the UI.

## Quality Gates

- Installed package and import path are known.
- Query identity inputs and authorization partitions are enumerated.
- Skip/refetch behavior, mutation cache impact, and test isolation needs are
  explicit.

## Hard Stops

- The result-changing inputs or authorization partition cannot be enumerated.
- A mutation changes server state but the affected cache keys and UI states are
  unnamed.
- The change depends on a shared `QueryClient` cache in tests without isolation
  or cleanup.

## Phase Output

Return the matched query evidence, cache identity inputs, skip/refetch decision,
mutation cache impact, and validation requirements.
