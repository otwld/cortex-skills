# Nestjs Mongoose Conventions Review

## Overview

Find regressions in Mongoose schema correctness, ObjectId handling, repository
contracts, and query result typing.

## Workflow

- Compare schema changes against persisted data shape, required fields, defaults,
  indexes, refs, virtuals, hooks, plugins, discriminators, and local registration
  timing.
- Verify model injection uses the correct token and connection name for the
  owning repository or provider.
- Check repository methods for behavior-oriented names and explicit return
  contracts. Callers should not need Mongoose model, query, or document APIs
  unless the method is explicitly persistence-internal.
- Trace ObjectId values from input through parsing, querying, population,
  serialization, and returned contracts.
- Review lean queries for missing getters, virtuals, methods, validation, or
  save behavior that callers might rely on.
- Review aggregation pipelines for explicit result types, ObjectId conversion,
  projection shape, and mapping before public return.
- Review index synchronization changes for explicit create/drop diff evidence
  and an operational plan for expensive or destructive index work.
- Confirm touched exported schemas, repositories, tokens, persistence DTOs, and
  mappers have current JSDoc, TSDoc, tests, or consumer-facing documentation
  when behavior changed.

## Quality Gates

- Findings name the schema path, model token, repository method, query,
  aggregation stage, ObjectId path, or return contract that can regress.
- Review distinguishes persistence-only risk from public API or transport
  contract leakage.
- Missing validation is actionable: name the repository test, integration path,
  aggregation assertion, index check, or static type proof needed.

## Finding Triggers

- A repository returns hydrated documents, raw queries, models, or unconverted
  ObjectIds to callers that expect plain contracts.
- A schema class doubles as DTO or domain shape while persistence behavior
  differs.
- Aggregation output is typed as `any`, a hydrated document, or an unrelated
  schema type.
- A lean result is used where getters, virtuals, methods, or `save()` are
  expected.
- Hooks, plugins, indexes, or discriminators are registered after the model is
  compiled or outside the owning schema setup.
- Index synchronization may drop existing indexes without reviewed diff output.

## Hard Stops

- Do not approve public contracts that expose Mongoose document internals by
  accident.
- Do not accept untyped aggregation or ObjectId conversion when caller behavior
  depends on the result shape.
- Do not ignore model-token or named-connection ambiguity in multi-connection
  code.
- Do not approve index synchronization as a safe cleanup unless the diff output
  and operational impact are known.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific schema path, repository contract, ObjectId conversion, query result
type, or validation evidence needed to close it.
