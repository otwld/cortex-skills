---
name: rxjs-conventions
description: Use when creating, modifying, or reviewing RxJS observables, operators, subscriptions, subjects, multicasting, cleanup, or async stream composition.
---

# Output Marker

Display:
using skill: rxjs-conventions

---

# RxJS Conventions

## Overview

Prefer composable observable pipelines and explicit lifetime management over
manual subscription logic scattered through application code.

## Core Rules

- Clean up long-lived or infinite subscriptions.
- Prefer operators over nested subscriptions.
- Use subjects only when a push boundary is truly needed.
- Share streams intentionally when multiple consumers observe expensive sources.
- Surface errors through typed stream state or explicit error handling.
- Keep framework lifecycle helpers consistent with the project.

## Usage Checklist

- Subscription lifetime is bounded.
- Nested subscriptions are avoided.
- Shared streams do not duplicate expensive work.
- Errors and completion behavior are intentional.

## Cross-References

- WITH: typescript-code-style
- AFTER: skill-evolution
