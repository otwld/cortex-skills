# Composition Over Inheritance Verify

## Overview

Verify that final touched code prefers explicit composition and that remaining
inheritance has a concrete reason.

## Workflow

1. Re-read touched classes, functions, components, hooks, services, providers,
   adapters, strategies, modules, and tests.
2. Confirm behavior reuse is expressed through composition when practical.
3. Confirm remaining inheritance is justified by framework extension, true
   subtype polymorphism, stable abstract contract, template method, or
   compatibility.
4. Confirm collaborators, strategy functions, adapters, hooks, components, or
   configuration objects have clear names and ownership.
5. Record validation commands, tests, static inspection, or blockers that cover
   the composition or inheritance risk.

## Quality Gates

- Verification names the touched reuse boundaries checked.
- No known helper-only or state-sharing inheritance remains without a blocker or
  follow-up owner.
- Validation evidence matches the substitution, lifecycle, or collaborator
  behavior affected by the change.

## Hard Stops

- Do not claim composition verification from tests alone when inheritance
  boundaries were not inspected.
- Do not leave hidden protected-state or override-order contracts undocumented.
- Do not hide unresolved extraction, public API, SRP, framework, or deepening
  decisions inside a composition pass.

## Phase Output

- Return verified reuse boundaries, composition outcomes, inheritance
  justifications, validation evidence, unresolved risks, and required follow-up
  owner.

