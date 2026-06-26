# Vue Conventions Run

## Overview

Implement Vue changes so component public surfaces are small and typed, reactive
ownership is explicit, and Composition API structure follows local project
convention.

## Workflow

1. Preserve the local SFC pattern unless the task explicitly migrates it. Keep
   section order, naming, imports, and component organization consistent with
   nearby files.
2. Type props and emits at the component boundary. In `<script setup>`, use
   `defineProps` and `defineEmits` consistently as either runtime declarations
   or type-based declarations, and avoid mixing both forms for the same
   boundary.
3. Keep macro arguments module-scope safe. Do not reference setup-local values
   from `defineProps` or `defineEmits` options because those options are
   hoisted by the compiler.
4. Treat props as parent-owned. Derive display state through `computed`, use
   local refs for local edits, and emit changes rather than mutating props.
5. Use watchers for effects that must react to change, not for derived values
   that can be expressed as `computed`.
6. Extract a composable only when behavior is reused, needs an independent
   lifecycle, or becomes clearer as a named reactive unit. Call composables
   synchronously from `<script setup>` or `setup()` unless a documented Vue
   lifecycle hook pattern applies.
7. Document slots, exposed instance methods, unusual `v-model` behavior, and
   component states that are not clear from names and types.
8. Use `defineModel` only when the project Vue version and local style support
   that macro; otherwise declare the model prop and `update:` event explicitly.
9. Run component typecheck, lint, focused tests, stories, or visual checks that
   cover changed public behavior.

## Quality Gates

- Props, emits, slots, model bindings, and exposed instance APIs are typed and
  intentionally limited.
- Reactive state has a clear owner, and derived state is not duplicated through
  watchers or ad hoc refs.
- Composable extraction has a reuse, lifecycle, or naming reason beyond making a
  component file shorter.
- Public component behavior changed by the task is covered by tests, stories,
  docs, or a stated validation gap.

## Hard Stops

- Do not mutate props or rely on casts to satisfy prop or emit types.
- Do not expose internal refs, methods, or component instance state unless a
  consumer contract requires it.
- Do not use watchers as computed values.
- Do not extract a one-off composable that hides rather than clarifies reactive
  ownership.
- Do not introduce `defineModel` or other macros unsupported by the project
  version.

## Phase Output

Return the component contract changes, reactive ownership decisions, macro and
version assumptions, composable boundaries, documentation updates, validation
run, and remaining behavior gaps.
