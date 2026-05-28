---
name: angular-tanstack-query-conventions
description: Use when creating, modifying, or reviewing TanStack Query integration in Angular code, including query keys, query options, mutations, pagination, and skippable inputs.
---

# Output Marker

Display:
using skill: angular-tanstack-query-conventions

---

# Angular TanStack Query Conventions

## Overview

Keep Angular TanStack Query usage predictable by centralizing query keys,
options, pagination handling, and mutation metadata in reusable project
patterns.

## Core Rules

- Use TanStack Angular primitives such as `injectQuery` and `injectMutation` directly unless a shared abstraction is justified.
- Prefer typed query option factories over repeated inline option objects.
- Build query keys through a project-approved factory so invalidation remains consistent.
- Represent disabled/skippable queries explicitly instead of passing partial invalid inputs.
- Normalize paginated responses through a reusable selector when backend response shapes repeat.
- Keep mutation metadata explicit when the project relies on it for invalidation, analytics, or notifications.
- Avoid `any` in shared query helpers.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative helper names from the extracted source project.

## Usage Checklist

- Query keys are centralized and typed.
- Disabled query paths are explicit.
- Pagination logic is not duplicated across features.
- Mutations expose the metadata the project expects.
- Public helpers are typed without `any`.

## Cross-References

- BEFORE: angular-conventions
- WITH: rxjs-conventions, typescript-api-conventions, public-api-design
- AFTER: code-documentation, skill-evolution
