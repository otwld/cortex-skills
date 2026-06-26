# Nestjs Mongoose Conventions Run

## Overview

Implement Mongoose persistence changes so schemas, queries, ObjectId conversion,
and returned contracts remain explicit.

## Workflow

- Register schemas through the local `MongooseModule` pattern. Keep model tokens,
  named connections, and repository providers consistent with the surrounding
  feature.
- Define schema paths with required, default, enum, index, ref, immutable, and
  selection behavior that matches persisted data. Use raw schema definitions only
  when decorators cannot represent the shape clearly.
- Keep hooks, plugins, virtuals, indexes, and discriminators close to the schema
  and registered before the model is compiled.
- Keep repositories behavior-oriented. Return named contracts such as summaries,
  existence results, or persistence DTOs instead of raw models or queries.
- Centralize ObjectId parsing and serialization at repository or mapper
  boundaries. Do not make controllers or public DTO consumers know Mongoose
  ObjectId details.
- Use `lean()` for read-only return data that will be mapped or serialized
  without document behavior. Avoid it when getters, virtuals, document methods,
  validation, or saving are required.
- Type aggregation pipelines and result records explicitly. Map aggregation
  output before exposing it to callers.
- When synchronizing indexes, inspect the index diff first and treat dropped
  indexes as a migration decision rather than a routine schema cleanup.
- Update JSDoc or TSDoc for touched exported schemas, repositories, model
  tokens, persistence contracts, mappers, and reusable query helpers.
- When adding invented examples, use recruitment job board entities such as
  candidates, job offers, applications, recruiters, and interviews.

## Quality Gates

- Run the narrowest repository unit test, integration test, schema validation,
  query test, aggregation test, or mapper test that exercises the changed
  persistence behavior.
- When validation cannot run, provide static evidence: schema path definitions,
  model token registration, ObjectId conversion point, query or aggregation
  result type, and mapped return contract.

## Hard Stops

- Do not return hydrated documents, raw query objects, raw models, or unconverted
  ObjectIds from public repository contracts unless the contract explicitly
  requires Mongoose behavior.
- Do not use a schema class as a DTO or domain model when persistence-only fields,
  methods, virtuals, or serialization behavior differ.
- Do not hide aggregation output behind `any`, broad casts, or inferred document
  types.
- Do not add schema hooks or plugins after model compilation.
- Do not run index synchronization where existing database indexes may be
  dropped without reviewed diff output and an operational plan.

## Phase Output

Return changed Mongoose files, schema and repository decisions, ObjectId and
result-shape mapping, validation command or static proof, and any remaining
persistence risk.
