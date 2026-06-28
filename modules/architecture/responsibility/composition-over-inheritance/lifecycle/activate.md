# Composition Over Inheritance Activate

## Overview

Activate for code work that may choose, preserve, or challenge inheritance,
composition, collaborator wiring, or behavior reuse.

## Workflow

1. Load `references/composition-boundaries.md` for code creation, edit,
   refactor, split, move, or material review tasks involving behavior reuse or
   extension.
2. Inspect touched classes, abstract classes, subclasses, mixins, functions,
   components, hooks, services, providers, adapters, strategies, and modules.
3. Identify inheritance mechanisms: `extends`, override methods, protected
   members, base-class state, template methods, mixins, or framework extension
   points.
4. Identify composition mechanisms: dependency injection, constructor
   collaborators, functions, adapters, strategy objects, hooks, composables,
   components, slots, children, render props, and configuration.
5. Name overlap with SRP, extraction, public API, framework conventions, or
   deepening modules when the design question belongs there.

## Quality Gates

- Activation evidence names a concrete touched code unit or hierarchy.
- Inheritance concerns identify the reuse or variation point, not only the
  presence of `extends`.
- Broad code requests activate this module, while non-code workspace work stays
  out unless the user asks for composition guidance.

## Hard Stops

- Do not reject inheritance solely because a hierarchy exists.
- Do not recommend composition without naming the collaborator or variation
  point it makes clearer.
- Do not decide package ownership, public API, or framework-specific lifecycle
  rules when another routed module owns that decision.

## Phase Output

- Return touched units, inheritance or composition mechanisms found, variation
  points, possible justifications, overlap risks, and the loaded reference.

