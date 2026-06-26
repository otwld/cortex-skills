# Angular TanStack Query Conventions Review

## Overview

Find cache identity, skip behavior, mutation, invalidation, pagination, and
Angular test regressions in TanStack Query integration.

## Workflow

- Trace every variable read by each query function and confirm it appears in the
  key when it changes the server result or cache partition.
- Check keys for authorization, tenant, company, job offer, user, permission,
  search, filter, sort, page, cursor, and locale dimensions where relevant.
- Confirm skipped queries have an explicit disabled condition. If `skipToken` is
  used, verify the UI does not depend on `refetch()` while skipped.
- Verify query option helpers preserve type inference and that cache reads use
  the same key factory or options source as the query.
- Check mutations for variable typing, pending/error/success UI, affected query
  keys, invalidation specificity, optimistic update rollback, and cache writes.
- Confirm broad invalidation is intentional and does not refresh unrelated
  lists, users, tenants, or authorization partitions.
- Verify paginated and infinite queries put the page, cursor, page size, and
  filters in the cache identity and do not merge incompatible result windows.
- Check Angular tests create or clear `QueryClient` instances per spec, disable
  retries where failures are expected, stub HTTP deterministically, and await
  stable query work.

## Quality Gates

- Every finding names the missing key dimension, skip rule, mutation cache
  effect, pagination boundary, or test isolation failure.
- Cache findings distinguish under-keying, over-invalidation, and stale local
  component state.
- Test findings name the shared cache, retry behavior, HTTP stub, or stability
  wait that makes the spec unreliable.

## Finding Triggers

- A query key omits an input used by the query function or server request.
- A query function accepts `null` or `undefined` values instead of an explicit
  skip or enabled condition.
- A mutation updates server data but only invalidates a vague or unrelated key.
- Component state copies query data and can drift from the cache.
- Specs share cache state or assert intermediate retry behavior accidentally.

## Hard Stops

- Do not approve a query key that omits a result-changing input or authorization
  partition.
- Do not approve a mutation that changes server state without named cache
  effects.
- Do not accept query tests that share cache state across specs.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
missing key dimension, skip condition, mutation cache effect, or test isolation
evidence needed to close it.
