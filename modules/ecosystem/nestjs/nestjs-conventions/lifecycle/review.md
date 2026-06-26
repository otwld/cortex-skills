# Nestjs Conventions Review

## Overview

Find regressions in NestJS transport separation, dependency injection, request
lifecycle behavior, and runtime bootstrap.

## Workflow

- Compare module metadata, providers, controllers, DTOs, and tests against the
  affected feature's existing structure.
- Check controllers for business branching, persistence orchestration, or
  external adapter calls that should live in providers.
- Verify provider registrations use stable tokens when implementations can vary,
  factories inject dependencies in the declared order, and exports expose only
  intended consumers.
- Review provider scopes for request or transient propagation, shared mutable
  state, and accidental per-request allocation.
- Check pipes, guards, interceptors, filters, and middleware against Nest request
  lifecycle responsibilities and the scope where they are registered.
- Inspect bootstrap changes for global effects on validation, error shape,
  CORS, prefixes, versioning, adapters, and microservice startup.
- Confirm touched exported Nest symbols and public DTOs have current JSDoc,
  TSDoc, tests, or consumer-facing documentation when behavior changed.

## Quality Gates

- Findings name the affected route, provider token, module import or export,
  lifecycle hook, or bootstrap setting.
- Review distinguishes compile-time provider wiring risk from runtime request
  behavior changes.
- Missing validation is reported only when a specific unit test, e2e path,
  runtime smoke check, or static dependency proof would close the risk.

## Finding Triggers

- Controller code contains business rules or persistence behavior beyond
  transport mapping.
- A replaceable adapter is registered by class or anonymous string token with no
  stable exported token.
- Validation or transformation relies on metadata that will not exist at
  runtime.
- A global guard, pipe, interceptor, or filter changes behavior for routes not
  covered by evidence.
- Request scope is introduced and can propagate through dependent providers.

## Hard Stops

- Do not approve controller-owned business behavior when a provider boundary is
  required for testing or transport reuse.
- Do not accept global runtime changes without affected-route evidence.
- Do not ignore failed or missing provider-resolution evidence when constructor
  dependencies, tokens, or scopes changed.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific NestJS route, provider token, module boundary, lifecycle responsibility,
or validation evidence needed to close it.
