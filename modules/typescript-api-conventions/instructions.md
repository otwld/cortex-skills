
# Output Marker

Display:
using module: typescript-api-conventions

---

# TypeScript API Conventions

## Overview

Design TypeScript public APIs that make invalid states hard and supported states
obvious.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Identify consumers; use explicit exports; prefer discriminated unions; constrain generics; avoid optional-field state bags; document invariants.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Exported TypeScript types model valid states, invariants, and consumer usage explicitly.
- Generics, DTOs, contracts, and unions are constrained enough to prevent invalid combinations.
- Type-only exports, runtime exports, and public entry points remain intentional.

## Example

CandidateApplicationState as submitted, interviewing, offered, or rejected variants is
safer than one loose object.

## Hard Stops

- Do not expose broad generics or optional bags that shift invariants to consumers.
- Do not export private helper types as a workaround for local imports.
- Do not erase type errors with casts instead of fixing the API contract.

## Usage Checklist

- Consumers, exported symbols, DTOs, generics, and entry points were inspected.
- States, invariants, and naming are encoded in the type surface.
- Type checking, docs, and migration impact were validated or named as gaps.

## Cross References

- WITH: public-api-design, naming-consistency, typescript-code-style, code-documentation
