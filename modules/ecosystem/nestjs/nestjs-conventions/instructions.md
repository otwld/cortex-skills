
# Output Marker

Display:
using module: nestjs-conventions

---

# NestJS Conventions

## Overview

Keep NestJS modules explicit without letting framework structure swallow domain
ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Controllers handle transport; providers hold application behavior; pipes validate boundaries; tokens are explicit when adapters vary.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- NestJS controllers stay transport-focused while providers own application behavior.
- Validation pipes, guards, interceptors, and tokens sit at explicit framework boundaries.
- Runtime and bootstrap changes preserve module ownership and testable provider seams.

## Example

ApplicationsController validates Candidate application requests and delegates decision
logic to an Application intake provider.

## Hard Stops

- Do not place business behavior in controllers to avoid provider or service design.
- Do not make implicit provider tokens when adapters or implementations can vary.
- Do not bypass NestJS validation or lifecycle boundaries with ad hoc runtime wiring.

## Usage Checklist

- Module, controller, provider, bootstrap, and boundary responsibilities were inspected.
- Transport, validation, guard, interceptor, and provider roles are separated.
- NestJS tests, docs, or runtime validation were named for changed behavior.

## Cross References

- WITH: rxjs-conventions, typescript-code-style, code-documentation
- AFTER: skill-evolution
