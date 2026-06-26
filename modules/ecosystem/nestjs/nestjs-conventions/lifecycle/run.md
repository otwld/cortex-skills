# Nestjs Conventions Run

## Overview

Implement NestJS changes with explicit module ownership, dependency wiring, and
request-lifecycle behavior.

## Workflow

- Keep module metadata minimal and intentional. Import only modules whose
  exported providers are used, provide only local dependencies, and export only
  providers that other modules should consume.
- Keep controllers thin. They may bind route parameters, request bodies, headers,
  and response codes, but business branching and persistence orchestration belong
  in providers.
- Keep DTOs and validation classes aligned with runtime validation. If a
  validation pipe depends on runtime class metadata, use imports that remain
  present at runtime.
- Use custom providers for replaceable adapters, factories, external clients,
  and configuration-derived values. Export tokens from a stable location when
  multiple files need them.
- Keep provider scope singleton unless request or transient scope is required by
  state lifetime. Document and test scope changes because request scope can
  propagate through dependent providers.
- Apply guards, pipes, interceptors, filters, and middleware at the narrowest
  scope that matches the behavior. Global registration requires route-wide
  evidence.
- Keep bootstrap code focused on framework setup: platform adapter, global
  validation, global filters, global interceptors, CORS, versioning, prefixes,
  and microservice startup.
- Update JSDoc or TSDoc for touched exported providers, controllers, DTOs,
  tokens, guards, pipes, interceptors, filters, and reusable helpers.
- When adding invented examples, use recruitment job board entities such as
  candidates, job offers, applications, recruiters, and interviews.

## Quality Gates

- Run the narrowest provider unit test, controller test, e2e route, or bootstrap
  smoke check that exercises the changed Nest behavior.
- When validation cannot run, provide static evidence: module imports and
  exports, provider token registration, request lifecycle placement, DTO
  validation path, and affected route or runtime.

## Hard Stops

- Do not put business rules in controllers to avoid creating or testing a
  provider.
- Do not use stringly or implicit tokens for replaceable adapters when a stable
  exported token is needed.
- Do not bypass validation, guards, or interceptors with manual controller code
  that changes the same request lifecycle responsibility.
- Do not widen provider scope or register global framework behavior without
  naming the route and runtime impact.

## Phase Output

Return changed NestJS files, module and provider wiring decisions, request
lifecycle placement, validation command or static proof, and any remaining
runtime risk.
