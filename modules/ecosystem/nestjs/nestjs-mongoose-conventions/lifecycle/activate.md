# Nestjs Mongoose Conventions Activate

## Overview

Decide whether NestJS Mongoose conventions apply and capture the schema, model,
query, and contract evidence needed before persistence changes.

## Workflow

1. Match the request or diff to Mongoose module registration, schemas, model
   injection, repositories, query builders, aggregations, ObjectId conversion,
   mapping code, or persistence tests.
2. Inspect installed `@nestjs/mongoose` and `mongoose` versions, connection
   setup, model registration, schema definitions, indexes, hooks, plugins, and
   repository patterns.
3. Classify every affected shape as schema document, hydrated document, lean
   object, domain model, persistence DTO, transport DTO, or API response.
4. Identify where ObjectIds are accepted, converted, populated, serialized, or
   returned.
5. Decide which query, aggregation, index, or mapper evidence can validate the
   persistence behavior.
6. For index synchronization, require an index diff or migration plan before
   accepting any operation that may drop existing database indexes.

## Trigger Evidence

Activate for changes to `MongooseModule`, `@Schema`, `@Prop`, `SchemaFactory`,
`InjectModel`, models, repositories, schema hooks, plugins, indexes, virtuals,
discriminators, population, lean queries, aggregation pipelines, sessions,
transactions, ObjectId handling, persistence DTOs, or persistence tests.

Do not activate for NestJS code that has no Mongoose model, schema, query,
database contract, or persistence-facing type.

## Decisions

- Keep schema definitions, hydrated documents, lean objects, domain models, and
  transport contracts separate when their shapes or behavior differ.
- Use `Types.ObjectId` in TypeScript document-facing types and schema ObjectId
  declarations in schema definitions. Convert to string or a public identifier
  before returning data across transport or public API boundaries.
- Use lean/plain results only when the caller does not need document methods,
  change tracking, getters, setters, virtuals, validation, or `save()`.
- Type aggregation results explicitly. Mongoose aggregation can produce arbitrary
  document shapes and does not provide normal schema casting guarantees.
- Register hooks, plugins, indexes, and discriminators before model compilation,
  using async feature registration when schema mutation requires injected
  dependencies.
- Treat index synchronization as a migration risk. Prefer inspecting the index
  diff before running a sync operation that can remove indexes from the
  database.

## Quality Gates

- Activation names the affected schema, model token, repository method, query,
  aggregation, ObjectId path, and returned contract.
- The phase identifies whether callers receive hydrated documents, lean objects,
  mapped domain data, or transport DTOs.
- Validation is stated as a persistence unit test, integration test, index/query
  inspection, or static type proof.

## Hard Stops

- A raw Mongoose document, model, query, or ObjectId is exposed across a public
  or transport boundary without an explicit contract.
- Aggregation output shape or ObjectId conversion is unknown for behavior the
  caller depends on.
- Schema hooks, plugins, indexes, or discriminators are changed without checking
  registration timing.
- Index synchronization is proposed without evidence of indexes to create and
  drop.

## Phase Output

Return matched Mongoose evidence, affected schema and repository contract,
ObjectId and result-shape decisions, validation requirement, and any blocked
persistence decision.
