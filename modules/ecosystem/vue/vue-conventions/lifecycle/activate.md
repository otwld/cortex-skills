# Vue Conventions Activate

## Overview

Use this phase when the task creates, modifies, or reviews Vue 3 component
behavior, Single-File Component structure, Composition API code, typed component
contracts, or composables.

## Workflow

1. Inspect touched paths for `.vue` files, imports from `vue`, composable files,
   component tests, stories, fixtures, and docs that describe component
   behavior.
2. Identify the local component pattern: `<script setup>`, explicit
   `setup()`, Options API, TypeScript usage, naming style, and SFC section
   order.
3. Name the public component surface being changed: props, emits, slots,
   `v-model`, exposed instance methods, component name, or documented states.
4. Identify reactive ownership: props from parents, local refs or reactive
   objects, computed derivations, watchers, provided/injected values, and
   composable-owned state.
5. Check the project Vue version and compiler macro support when the task uses
   `defineProps`, `defineEmits`, `defineSlots`, `defineExpose`, or
   `defineModel`.
6. Identify validation that covers the public behavior: component tests,
   typecheck, lint, stories, visual snapshots, or documented usage examples.

## Quality Gates

- Activation names the Vue files or composables and the public component
  surface involved.
- Local SFC and Composition API style is identified from neighboring code.
- Version-sensitive macro or `v-model` usage is checked instead of assumed.
- Validation expectations are tied to props, emits, slots, reactive state, or
  component behavior.

## Hard Stops

- Do not activate for a TypeScript utility merely because a Vue app imports it.
- Do not assume `<script setup>` is the local style when nearby components use a
  different pattern.
- Do not treat private local state as public component API unless it is exposed,
  emitted, slotted, documented, or consumed by templates.
- Do not recommend a compiler macro without checking project support.

## Phase Output

Return the activation decision, Vue surfaces inspected, local SFC pattern,
public component contract at risk, version-sensitive features, and validation
required.
