---
name: nestjs-conventions
description: Use when creating, modifying, or reviewing NestJS modules, providers, controllers, interceptors, guards, pipes, application bootstrap, or microservice runtimes.
---

# Output Marker

Display:
using skill: nestjs-conventions

---

# NestJS Conventions

## Overview

Keep NestJS code modular, strongly typed, and framework-idiomatic. Project
patterns can be stricter, but reusable guidance should not assume a specific
package naming scheme.

## Core Rules

- Providers with injectable dependencies should use `@Injectable()` and be registered through modules or project-approved provider factories.
- Controllers should stay thin and delegate behavior to services or use-case providers.
- Use constructor injection for providers and controllers unless the project documents another pattern.
- Prefer composition over large inheritance hierarchies or monolithic services.
- Search existing project packages before adding reusable helpers.
- Use strong typing and document any unavoidable unsafe boundary.
- Add JSDoc for public providers, guards, interceptors, pipes, and reusable runtime helpers when intent is not obvious.

## Microservices

- Use NestJS microservice APIs that match the runtime shape: microservice-only or hybrid HTTP plus transport.
- For manual message acknowledgements, configure transport options explicitly and acknowledge through the context object.
- Enable graceful shutdown hooks when the runtime owns long-lived connections.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative naming conventions from the extracted source project.

## Usage Checklist

- Module/provider ownership is clear.
- Controllers delegate business logic.
- Reusable helpers were checked before adding new ones.
- Public runtime APIs are typed and documented.

## Cross-References

- WITH: rxjs-conventions, typescript-code-style
- AFTER: code-documentation, skill-evolution
