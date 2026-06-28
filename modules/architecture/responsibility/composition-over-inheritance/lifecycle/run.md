# Composition Over Inheritance Run

## Overview

Implement code changes with composition-first reuse while preserving justified
inheritance and local framework conventions.

## Workflow

1. Prefer explicit collaborators, strategy functions, adapters, hooks,
   composables, reusable components, or configuration over base-class reuse.
2. Keep inherited behavior only when the accepted justification still applies in
   the changed code.
3. Replace shared helper inheritance with local functions or owned collaborators
   when that improves call clarity and testability.
4. Avoid exposing protected state, override sequencing, or `super` call ordering
   as hidden contracts.
5. Update tests, docs, examples, and callers for any changed reuse or
   substitution boundary.

## Quality Gates

- New variation points are named and injected or passed explicitly.
- Composition reduces hidden coupling rather than creating shallow indirection.
- Remaining inheritance has documented hooks, stable invariants, and tests
  through the public contract.
- Framework-required inheritance follows the local framework module guidance.

## Hard Stops

- Do not create wrappers that only forward calls to satisfy the principle.
- Do not move behavior into global utilities when an owned collaborator or local
  function is clearer.
- Do not leave subclasses depending on undocumented base-class state or
  lifecycle ordering.

## Phase Output

- Return reuse boundaries changed, composition mechanisms added, inheritance kept
  with justification, caller updates, validation run or static evidence, and
  deferred risks.

