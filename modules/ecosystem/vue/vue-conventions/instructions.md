
# Output Marker

Display:
using module: vue-conventions

---

# Vue Conventions

## Overview

Keep Vue component public surfaces small, typed, and aligned with reactive ownership.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use local Vue style; type props and emits; prefer computed derived state; extract composables only for real reuse; document slots.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Vue components follow local SFC, Composition API, script setup, prop, emit, slot, and naming style.
- Derived state uses computed values or composables only when reuse or locality justifies extraction.
- Public props, emits, slots, and component states are typed and documented for consumers.

## Example

CandidateStagePicker emits stageSelected with a typed stage payload and documents
disabled-stage behavior.

## Hard Stops

- Do not extract a composable for one component just to make the file look smaller.
- Do not make template-facing state untyped or rely on casts to satisfy props and emits.
- Do not mix Vue style patterns when the local component tree already establishes one.

## Usage Checklist

- Neighboring Vue components and local SFC conventions were inspected.
- Props, emits, slots, computed state, and composable boundaries were checked.
- Vue tests, stories, or docs were named for public behavior changes.

## Cross References

- WITH: typescript-code-style, rxjs-conventions, code-documentation
- AFTER: skill-evolution
