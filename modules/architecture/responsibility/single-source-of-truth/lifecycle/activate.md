# Single Source Of Truth Activate

## Overview

Activate for code work that may create, preserve, or blur the authoritative
owner of a fact, rule, state value, configuration value, generated value, or
derived value.

## Workflow

1. Load `references/source-of-truth-boundaries.md` for code creation, edit,
   refactor, split, move, or material review tasks involving information
   ownership or duplicated facts.
2. Inventory touched facts and rules: state, configuration, constants, enums,
   feature flags, schemas, DTOs, validation, permissions, policies,
   calculations, generated values, fixtures, examples, and documentation facts.
3. Identify the current authoritative owner for each touched fact and every
   consumer that reads, imports, derives, caches, projects, validates, or
   serializes it.
4. Mark competing owners, copied values, parallel validators, duplicate field
   lists, stored derivations, manually edited generated output, and writable
   caches as drift risks.
5. Name overlap with SRP, extraction, public API, composition,
   no-transitional architecture, documentation, or framework conventions when
   the durable decision belongs to those modules.

## Quality Gates

- Activation evidence names a concrete touched fact, rule, data shape, or code
  surface.
- A duplication concern names the authoritative owner and the copied or
  competing consumer.
- Broad code requests activate this module, while non-code workspace work stays
  out unless the user asks for source-of-truth guidance.

## Hard Stops

- Do not reject every cache, projection, fixture, snapshot, migration bridge, or
  generated file as a violation.
- Do not choose package ownership, public API shape, reusable extraction, or
  responsibility splits when another routed module owns that decision.
- Do not recommend deleting duplication until the owner, consumers, and sync or
  migration path are understood.

## Phase Output

- Return touched facts, candidate authoritative owners, consumers, duplication
  risks, accepted exceptions, overlap risks, loaded reference, and next-phase
  source-of-truth decisions needed.
