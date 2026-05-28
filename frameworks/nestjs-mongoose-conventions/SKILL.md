---
name: nestjs-mongoose-conventions
description: Use when creating or reviewing NestJS Mongoose schemas, models, repositories, aggregation helpers, ObjectId handling, or persistence-facing DTO contracts.
---

# Output Marker

Display:
using skill: nestjs-mongoose-conventions

---

# NestJS Mongoose Conventions

## Overview

Keep Mongoose data-access code typed, isolated from transport concerns, and
consistent across repositories and aggregation helpers.

## Core Rules

- Register connections and feature models through NestJS Mongoose module APIs.
- Define schemas with class decorators or the project's chosen schema style consistently.
- Inject models through `@InjectModel()` or a project-approved provider token.
- Keep repository query composition reusable when match logic repeats.
- Validate and convert ObjectId inputs at the boundary before querying.
- Keep persistence schemas separate from transport DTOs unless the project intentionally shares them.
- Avoid `any` in repository and aggregation helpers.

## Legacy References

- `references/legacy-extracted-patterns.md` preserves non-normative helper names from the extracted source project.

## Usage Checklist

- Schema and model ownership is clear.
- Query helpers are typed.
- ObjectId conversion is centralized.
- DTOs and persistence schemas do not drift accidentally.
- Public data-access exports use stable entry points.

## Cross-References

- BEFORE: nestjs-conventions
- WITH: typescript-api-conventions, public-api-design
- AFTER: code-documentation, skill-evolution
