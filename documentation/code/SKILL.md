---
name: code-documentation
description: Use whenever code is generated, edited, moved, split, refactored, or materially reviewed, and when public, reusable, or user-facing documentation, examples, stories, MDX docs, or API usage notes change.
---

# Output Marker

Display:
using skill: code-documentation

---

# Code Documentation

## Overview

Documentation is part of every code edit, not a final cleanup pass. Any code
that is generated, edited, moved, split, refactored, or materially reviewed must
have relevant JSDoc/TSDoc updated in the same change.

Documentation should explain responsibility, supported usage, constraints,
failure modes, and examples. Match the documentation surface the target project
already uses.

## Required JSDoc/TSDoc Coverage

- Add or update JSDoc/TSDoc for every touched exported symbol, public API,
  reusable helper, component, service, hook, provider, command, adapter, DTO,
  contract, or module-level behavior.
- When private code is touched, document the nearest owning function, class,
  module, or public surface when that code path would otherwise be undocumented.
- When code is moved, split, or extracted, move or update the associated
  JSDoc/TSDoc in the same change.
- Do not use inline comments as a substitute for missing JSDoc/TSDoc on touched
  symbols.

## Documentation Options

- Use Storybook stories or MDX for UI components when Storybook exists.
- Use colocated Markdown or project docs for reusable functions, services, and contracts.
- Use JSDoc/TSDoc for TypeScript and JavaScript symbols that callers,
  maintainers, or generated docs consume in editors.
- Keep generated or source-mirror docs minimal and canonical.

## Rules

- Do not add placeholder docs.
- When documentation includes examples, apply `example-universe-enforcer`.
- Document behavior, constraints, failure modes, and usage expectations, not
  obvious type names.
- Keep docs near the code unless the project has a centralized docs structure.
- Prefer clearer names and stronger types over comments that merely restate the
  implementation.

## Hard Stops

- Code is generated, edited, moved, split, or refactored without updating the
  relevant JSDoc/TSDoc.
- Public or reusable code is left undocumented because tests or types were
  updated instead.
- Placeholder comments are added to satisfy the documentation requirement.

## Usage Checklist

- Touched code has relevant JSDoc/TSDoc at the symbol or owning-surface level.
- Public surface and responsibility are described.
- Moved, split, or extracted code retained or gained associated documentation.
- Example usage is realistic and domain-consistent.
- Docs are colocated or linked from the project-approved docs location.
- JSDoc/TSDoc and external docs do not contradict each other.

## Cross-References

- WITH: example-universe-enforcer
- AFTER: skill-evolution
