# Public API Design Activate

## Overview

Activate when a task adds, removes, renames, or reshapes a consumer-facing export,
entry point, DTO, schema, contract, SDK surface, or package import path.

## Workflow

1. Inspect current public entry points and exported symbols for the owning package
   or module.
2. Inspect known consumers, import paths, generated types, docs, examples, and
   tests.
3. Identify valid and invalid states represented by the proposed contract.
4. Inspect naming and documentation on nearby public symbols.
5. Choose the owning package or module before evaluating the export shape.

## Quality Gates

- The changed surface is importable or observable by another package, project,
  app, integration, or external caller.
- Private helpers are out of scope unless exported, documented, or used as a
  contract by tests or consumers.
- Activation evidence names owner, consumers, states, docs impact, and validation
  still needed.

## Hard Stops

- Do not export implementation details because a nearby caller wants them.
- Do not model public states as optional-field bags when a typed variant would
  exclude invalid combinations.
- Do not change import paths without naming affected consumers and validation.

## Phase Output

- State the public surface, owner, consumers, contract states, docs impact, and
  validation evidence still needed.
