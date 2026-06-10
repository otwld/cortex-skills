---
name: typescript-api-conventions
description: Use when designing or reviewing TypeScript public APIs, exported types, DTOs, contracts, generics, strict typing, entry points, or reusable type surfaces.
---

# Output Marker

Display:
using skill: typescript-api-conventions

---

# TypeScript API Conventions

## Overview

Public TypeScript types are contracts. Keep them explicit, stable, reusable, and
free of private implementation details.

## Core Rules

- Avoid `any` in public APIs; use generics or `unknown` with narrowing.
- Public exported types must not expose private or internal types.
- Prefer discriminated unions for distinct states.
- Prefer interfaces for exported object shapes.
- Avoid return-type-only generics.
- Keep DTO and contract ownership clear.
- Do not widen types to hide design problems.

## Usage Checklist

- Exported types are named and owned clearly.
- No public `any` is introduced.
- Internal types do not leak into public surfaces.
- Generics represent real caller-provided relationships.
- Contract changes are compatible or migration notes exist.

## Cross-References

- WITH: public-api-design, naming-consistency, typescript-code-style, code-documentation
