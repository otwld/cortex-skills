# Vue Conventions Review

## Overview

Review Vue changes for component API drift, untyped template-facing state,
reactive ownership mistakes, unnecessary composables, and unsupported macro
usage.

## Workflow

1. Compare changed components and composables against neighboring SFC patterns:
   section order, script style, naming, prop declarations, emits declarations,
   and test structure.
2. Check props, emits, slots, `v-model`, `defineExpose`, and documented states
   for type safety and unnecessary public surface area.
3. Inspect template-facing values for casts, implicit `any`, missing null
   handling, and values that can become undefined during render.
4. Check reactive ownership: props should remain parent-owned, local refs should
   represent local state, computed values should represent derivations, and
   watchers should perform effects.
5. Review composables for synchronous setup usage, cleanup, returned API size,
   and real reuse or lifecycle ownership.
6. Check compiler macros against the project Vue version and local style,
   especially `defineModel` and type-based prop or emit declarations.
7. Review validation evidence from typecheck, lint, component tests, stories,
   visual checks, or usage docs.

## Quality Gates

- Findings cite the exact component, prop, emit, slot, macro, composable, or
  template value that creates risk.
- Review separates public component contract issues from private organization
  preferences.
- Version-sensitive feedback names the project feature support that needs
  proof.
- Test gaps describe the missing user-visible component state or interaction.

## Hard Stops

- Do not approve untyped or cast-around props, emits, slots, or template-facing
  state when TypeScript can model the contract.
- Do not approve prop mutation or exposed internal state without a documented
  consumer reason.
- Do not approve watcher-based derived state when `computed` expresses the same
  behavior.
- Do not approve a macro pattern that the project Vue version does not support.
- Do not approve component API changes without tests, stories, docs, or an
  explicit validation gap.

## Phase Output

Return findings ordered by user-facing risk, component contract corrections,
reactive ownership issues, macro/version evidence, validation reviewed, and
remaining Vue behavior gaps.
