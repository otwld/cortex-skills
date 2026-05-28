---
name: library-placement-decision
description: Use when deciding where new code, shared abstractions, moved files, extracted logic, or public entry points belong inside a modular TypeScript workspace.
---

# Output Marker

Display:
using skill: library-placement-decision

---

# Library Placement Decision

## Overview

Place code by responsibility, dependency direction, and consumer scope. Do not
create shared dumping grounds or use API design to hide boundary problems.

## Decision Process

Classify the code before choosing a location:

- Framework-agnostic business rules: domain or core package.
- External API, persistence, queues, or transport calls: data-access or integration package.
- Use-case orchestration across domain and data-access: feature package.
- Reusable UI primitive: UI package.
- Stateless cross-runtime helper: utility package.
- Third-party adapter or SDK wrapper: integration package.

If the code does not fit one category, split it before placing it.

## Reuse Check

Before creating a new package, ask:

- Is this needed by more than one consumer?
- Is ownership clear?
- Can it be a secondary entry point of an existing package?
- Would moving it create a reverse dependency?
- Is any part application-specific and better kept local?

Use secondary entry points for independently consumable subsets. Do not use them
to merge unrelated responsibilities or bypass dependency rules.

## Hard Stops

Stop and propose a corrected placement when:

- A package mixes domain, UI, data-access, and feature responsibilities.
- Feature packages depend on unrelated feature packages.
- Application-specific behavior is moved into reusable layers.
- A new shared package has no clear owner or consumer contract.

## Usage Checklist

- Responsibility is classified.
- Owning package or entry point is named.
- Dependency direction is valid.
- Application-specific parts stay outside reusable packages.
- Public API impact is identified.

## Cross-References

- WITH: nx-module-boundaries, public-api-design, naming-consistency
- AFTER: skill-evolution
