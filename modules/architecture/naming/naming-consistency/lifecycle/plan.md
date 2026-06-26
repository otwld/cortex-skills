# Naming Consistency Plan

## Overview

Plan names that encode domain role, lifecycle state, ownership, and artifact kind
while preserving project vocabulary and consumer readability.

## Workflow

1. Name the owner, domain role, lifecycle state, and artifact kind.
2. Compare proposed names to neighboring files, exported symbols, DTOs, events,
   commands, tests, and docs.
3. Prefer complete public names over abbreviations that require local context.
4. Use a role suffix only when it communicates a real responsibility.
5. Plan exact rename updates for imports, exports, tests, docs, stories, fixtures,
   generated references, and build metadata.

## Quality Gates

- Names distinguish domain concepts that are different in the product model.
- Public names are stable enough for consumers and documentation.
- Glossary changes are recorded or the unresolved decision is called out.
- Validation includes searches for old public names and affected generated
  references.

## Hard Stops

- Do not use shared, common, helper, util, base, new, old, temp, or generic
  manager names unless the project vocabulary explicitly defines them.
- Do not invent a second vocabulary when a glossary term already exists.
- Do not hand-edit generated references; use the owning workflow.

## Phase Output

- Return chosen names, rejected alternatives, glossary impact, files and symbols
  to rename, consumer updates, and validation plan.
