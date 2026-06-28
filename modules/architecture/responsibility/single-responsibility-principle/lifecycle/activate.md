# Single Responsibility Principle Activate

## Overview

Activate for code work that may create, preserve, or blur one clear reason to
change inside a touched code unit.

## Workflow

1. Load `references/responsibility-boundaries.md` for code creation, edit,
   refactor, split, move, or material review tasks.
2. Inventory touched files, functions, methods, classes, components, hooks,
   services, controllers, commands, providers, schemas, and modules.
3. Identify responsibilities present in each touched unit: UI, validation,
   business behavior, orchestration, mapping, persistence, networking,
   configuration, side effects, or lifecycle management.
4. Name any independent reason to change, actor, workflow, integration, or
   policy that may make the unit non-cohesive.
5. Note overlap with extraction, placement, public API, or architecture
   deepening when a split would create a reusable owner, package boundary, public
   surface, or deeper interface.

## Quality Gates

- Activation evidence names a concrete touched code unit or code-review target.
- A mixed-responsibility concern names independent change drivers, not size
  alone.
- Broad code requests activate this module, while non-code workspace work stays
  out unless the user asks for SRP guidance.

## Hard Stops

- Do not activate from general quality language when no code is being touched or
  reviewed.
- Do not treat every long function or large file as an SRP violation without
  naming distinct reasons to change.
- Do not resolve package ownership, public API design, or reusable extraction in
  this module when another routed module owns that decision.

## Phase Output

- Return touched units, suspected responsibilities, independent change drivers,
  loaded reference, overlap risks, and next-phase SRP decisions needed.

