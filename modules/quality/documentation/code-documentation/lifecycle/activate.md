# Code Documentation Activate

## Overview

Identify code changes that need durable documentation or intent comments before
implementation, review, or verification work proceeds.

## Workflow

1. Match this module only to a concrete code touch, material code review, public
   contract change, documentation update, example update, or dense logic block.
2. Load `references/coverage-and-comments.md` when the task will modify or
   materially review code.
3. Name the touched documentation surfaces: exported symbols, interfaces, type
   members, properties, methods, functions, framework-bound inputs, component
   contracts, commands, routes, config, DTOs, schemas, examples, stories,
   fixtures, generated docs, long functions, or dense private logic.
4. Identify stale documentation risk from moved, split, renamed, or deleted code.

## Quality Gates

- Activation evidence names the request phrase, changed file, symbol, public
  surface, or dense function that creates documentation risk.
- Touched interfaces, type members, component contracts, schemas, config fields,
  named functions, and long implementation blocks are included in the surface
  inventory when present.
- The selected reference is relevant to the task, not loaded as generic process
  ceremony.
- Pure conceptual code discussion stays out unless the user asks for code review,
  implementation, or documentation changes.

## Hard Stops

- Do not activate from broad quality language alone.
- Do not require new public documentation for a private, self-explanatory edit
  unless the nearest public contract changes.
- Do not defer documentation impact discovery until the final response.

## Phase Output

- Return the matched evidence, reference loaded, documentation surfaces to check,
  and any reason documentation work is intentionally out of scope.
