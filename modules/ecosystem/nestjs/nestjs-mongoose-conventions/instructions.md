
# Output Marker

Display:
using module: nestjs-mongoose-conventions

---

# NestJS Mongoose Conventions

## Overview

Keep persistence shape behind a seam so Mongoose details do not leak upward.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Separate schema, domain, and transport shapes; centralize ObjectId conversion; type aggregations; return plain contracts when callers need them.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Schema, domain model, persistence DTO, and transport contract remain separate where they differ.
- ObjectId conversion, aggregation typing, and lean/plain return shapes are explicit at persistence boundaries.
- Repositories expose behavior-oriented methods instead of leaking model internals to callers.

## Example

ApplicationRepository.findActiveForJobOffer returns ApplicationSummary records, not raw
hydrated documents.

## Hard Stops

- Do not pass raw ObjectId or document instances across transport or public API boundaries without a contract.
- Do not use Mongoose schemas as domain or DTO definitions by default.
- Do not hide aggregation result shape behind untyped any values.

## Usage Checklist

- Schema, model, repository, ObjectId, and DTO responsibilities were classified.
- Conversion, aggregation, and return contract typing were checked.
- Persistence-facing tests or validation were named for changed queries or schemas.

## Cross References

- BEFORE: nestjs-conventions
- WITH: typescript-api-conventions, public-api-design, code-documentation
- AFTER: skill-evolution
