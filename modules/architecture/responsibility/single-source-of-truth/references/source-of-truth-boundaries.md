# Source Of Truth Boundaries

Use this reference when code is created, edited, moved, split, refactored, or
materially reviewed and the work touches information that can drift.

## Core Rule

Every fact should have one authoritative owner. Other places may consume,
derive, cache, project, validate, serialize, or document that fact, but they
should not become independent sources that can change separately.

Single Source of Truth is about ownership and drift control. It is not a demand
to centralize every value into a global file, nor a reason to erase necessary
projections, caches, snapshots, or generated artifacts.

## Authoritative Owners

Pick the strongest owner for the kind of information being changed:

- Domain and business rules belong in domain policy, use-case logic, service
  boundaries, or rule engines that enforce runtime behavior.
- Validation and construction rules belong in schemas, validators, constructors,
  parsing boundaries, or shared contracts that callers reuse.
- Configuration belongs in environment parsing, typed config modules, feature
  flag providers, dependency wiring, or declared runtime defaults.
- State belongs to the server, database, store, reducer, cache, form controller,
  component, or provider that is responsible for mutation.
- Identifiers, constants, enums, and field lists belong in the contract,
  schema, generated type, protocol definition, or module that owns their
  lifecycle.
- Generated facts belong to the input metadata, schema, template, script, or
  source artifact that regenerates them.
- Documentation and examples should describe or consume the owner; they should
  not enforce a different rule.

Prefer the owner that already controls mutation, validation, persistence,
deployment, or compatibility. A generic constants file is rarely the strongest
owner when a domain contract, schema, or config loader already exists.

## Consumers

Consumers should depend on the owner through the narrowest clear mechanism:

- Import the owning constant, enum, schema, validator, type, or config accessor.
- Derive view data, labels, totals, and eligibility from the owner rather than
  storing a second value.
- Use selectors, hooks, service methods, or adapters to read owned state without
  exposing mutation internals.
- Generate docs, fixtures, clients, payload examples, and route tables from the
  owning schema or metadata when generation exists.
- Map between models at boundaries, but keep the rule that decides valid values
  in one owner.

When consumers need local data, make it read-only, derived, or explicitly
synchronized from the owner.

## Allowed Duplication

Duplication can be correct when it has a bounded purpose and a drift control:

- Cache: names the owner and has invalidation, refresh, or expiry behavior.
- Denormalized projection: names the owner and has a rebuild or synchronization
  path.
- Generated artifact: declares the source and regeneration command or build
  step.
- Migration bridge: keeps old and new sources only for a bounded compatibility
  window with a removal condition.
- Test fixture or snapshot: represents an expected result, not an active runtime
  rule.
- Local form or draft state: represents uncommitted user input and reconciles
  through the owning validation or submit path.
- External protocol copy: mirrors a third-party or wire contract and documents
  the upstream owner or generated client source.

If the exception has no owner, no sync path, and no removal or invalidation
rule, treat it as a competing source of truth.

## Warning Signs

Look for drift risk when:

- Frontend and backend validators define the same rule separately.
- A component, service, test, fixture, or documentation snippet copies a field
  list, enum, default, permission, or calculation.
- Form state, component state, store state, and server state can all mutate the
  same value.
- A cached or denormalized value has no invalidation or rebuild path.
- Generated files are manually edited after generation.
- Example payloads and DTO definitions disagree.
- Business policy lives in UI conditionals and server checks with no shared
  owner.
- Magic numbers or strings are repeated because importing the owner feels
  inconvenient.

Fix the owner relationship first. Only extract a new abstraction when the
existing owner is unclear or the duplicated rule needs a reusable public
surface.

## Boundaries With Neighboring Concerns

Single Source of Truth owns duplicated information and authoritative ownership.
It does not own every adjacent design decision:

- SRP owns whether a unit has one reason to change.
- Extraction owns whether duplicated code should become a reusable abstraction.
- Public API design owns exported contracts and compatibility semantics.
- Composition over Inheritance owns collaborator and inheritance structure.
- No-transitional architecture owns bounded old/new architecture states.
- Documentation policy owns documentation completeness and style.

Use this module to name the fact, the owner, the consumers, and the drift path.
Use neighboring modules for the structural decision when the fix changes those
boundaries.

## Review Language

A strong finding names:

- The duplicated fact or rule.
- The authoritative owner.
- The competing copy or second writable source.
- The concrete drift scenario.
- The smallest correction: import, derive, generate, synchronize, invalidate, or
  remove the duplicate.

Avoid vague advice such as "centralize this." Prefer precise language:

> This repeats the `employmentType` options already owned by the job posting
> schema. Import or generate the options from that schema so the form and API
> cannot drift when a new employment type is added.

If the owner cannot be identified, record that as the problem before proposing a
new shared location.
