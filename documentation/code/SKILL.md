---
name: code-documentation
description: Use when adding or changing public, reusable, or user-facing code that needs documentation, examples, stories, MDX docs, or API usage notes.
---

# Output Marker

Display:
using skill: code-documentation

---

# Code Documentation

## Overview

Documentation should explain public responsibility, supported usage, constraints,
and examples. Match the documentation surface the target project already uses.

## Documentation Options

- Use Storybook stories or MDX for UI components when Storybook exists.
- Use colocated Markdown or project docs for reusable functions, services, and contracts.
- Use JSDoc/TSDoc for public TypeScript APIs that callers consume in editors.
- Keep generated or source-mirror docs minimal and canonical.

## Rules

- Do not add placeholder docs.
- When documentation includes examples, apply `example-universe-enforcer`.
- Document behavior and constraints, not obvious type names.
- Keep docs near the code unless the project has a centralized docs structure.

## Usage Checklist

- Public surface and responsibility are described.
- Example usage is realistic and domain-consistent.
- Docs are colocated or linked from the project-approved docs location.
- JSDoc/TSDoc and external docs do not contradict each other.

## Cross-References

- WITH: example-universe-enforcer
- AFTER: skill-evolution
