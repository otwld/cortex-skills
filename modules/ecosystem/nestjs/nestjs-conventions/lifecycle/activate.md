# Nestjs Conventions Activate

## Overview

Decide whether NestJS conventions apply and capture the module, dependency, and
request-lifecycle evidence needed before framework-facing changes.

## Workflow

1. Match the request or diff to Nest modules, controllers, providers,
   decorators, guards, pipes, interceptors, filters, middleware, bootstrap code,
   microservice runtime setup, or Nest testing modules.
2. Inspect installed `@nestjs/*` versions, local module structure, global
   bootstrap configuration, and same-feature controller/provider patterns.
3. Name the affected transport boundary, provider token, validation DTO, request
   lifecycle hook, runtime adapter, or global framework behavior.
4. Decide whether the behavior belongs in a controller, provider, pipe, guard,
   interceptor, filter, middleware, or bootstrap configuration.
5. Identify the test, e2e flow, runtime command, or static dependency-injection
   evidence that can validate the decision.

## Trigger Evidence

Activate for changes to Nest decorators, module metadata, controllers,
providers, DTO validation, pipes, guards, interceptors, filters, middleware,
custom providers, injection scopes, application bootstrap, microservices, or
Nest-specific tests.

Do not activate for plain TypeScript code that has no Nest decorator, injection
token, request lifecycle hook, bootstrap effect, or Nest testing surface.

## Decisions

- Keep controllers transport-focused: parse request context, bind route
  parameters, call providers, and return response contracts.
- Put application behavior in injectable providers that can be tested without
  HTTP, WebSocket, queue, or microservice transport.
- Use pipes for validation and transformation, guards for access decisions, and
  interceptors for cross-cutting behavior around handler execution.
- Use explicit exported tokens for non-class providers, replaceable adapters,
  factories, or multiple implementations.
- Treat global pipes, guards, interceptors, filters, and provider scopes as
  application-wide behavior until proven narrower.

## Quality Gates

- Activation names the affected module, route, provider token, lifecycle hook,
  or bootstrap setting.
- The phase distinguishes transport work from application behavior and
  cross-cutting framework behavior.
- Validation is stated as a specific unit test, e2e test, runtime path, or
  static provider wiring check.

## Hard Stops

- The change alters validation, authorization, response mapping, provider scope,
  or global bootstrap behavior without naming affected routes or consumers.
- A replaceable adapter or factory provider is introduced without an explicit
  token and provider registration location.
- The task relies on Nest version-sensitive APIs while installed versions are
  unknown.

## Phase Output

Return matched NestJS evidence, affected module and transport boundary, provider
or lifecycle decision, validation requirement, and any blocked runtime or API
decision.
