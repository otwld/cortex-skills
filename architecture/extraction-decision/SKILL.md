---
name: extraction-decision
description: Use when repeated logic, DTOs, contracts, data-access patterns, UI composition, or orchestration suggest extracting a reusable abstraction.
---

# Output Marker

Display:
using skill: extraction-decision

---

# Extraction Decision

## Overview

Duplication can be a useful signal, but extraction is only valuable when
ownership, consumers, and dependency direction are clear.

## Decision Process

1. Identify the repeated pattern and all current consumers.
2. Decide whether the repetition is accidental, intentional, or premature.
3. Classify the abstraction by responsibility.
4. Choose the owning package or entry point.
5. Define the smallest public API that supports real consumers.
6. Plan migration without breaking current behavior.

## Extraction Rules

- Extract stable behavior, not coincidental similarity.
- Keep application-specific behavior local.
- Preserve tree-shaking and avoid broad barrels.
- Prefer small composable functions or types over large shared services.
- Do not mix UI, domain, data-access, and integration concerns in one abstraction.

## Hard Stops

Stop and redesign when:

- The extraction introduces circular dependencies.
- The abstraction has no clear owner.
- Consumers would import through internals.
- The extracted API is weaker or less typed than the repeated code.

## Usage Checklist

- Repetition and consumers are named.
- Responsibility and owner are clear.
- Public API is narrow.
- Migration steps are explicit.
- Bundle and dependency impact are considered.

## Cross-References

- BEFORE: library-placement-decision, nx-module-boundaries
- WITH: public-api-design, naming-consistency, bundle-performance, code-documentation
- AFTER: skill-evolution
