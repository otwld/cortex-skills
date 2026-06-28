# Single Source Of Truth Review

## Overview

Review code for competing authoritative owners and drift-prone duplication in
touched facts, rules, and generated outputs.

## Workflow

1. Inspect touched state, config, constants, schemas, validators, DTOs,
   permissions, policies, calculations, mappings, docs, examples, fixtures,
   generated artifacts, and tests.
2. Flag duplicated facts when two places can change independently or when a
   consumer restates a rule instead of referencing the owner.
3. For each finding, name the fact, the authoritative owner, the competing copy,
   the drift risk, and the smallest correction.
4. Accept caches, projections, generated artifacts, snapshots, compatibility
   layers, and migrations only when owner, sync, invalidation, regeneration, or
   removal rules are clear.
5. Defer non-source-of-truth findings to the owning module when the issue is
   primarily SRP, extraction, public API, composition, documentation, or
   transitional architecture.

## Quality Gates

- Findings are actionable and tied to a concrete duplicate or competing owner.
- Review does not require centralizing unrelated concepts under a vague common
  utility.
- Accepted duplication explains why it is safe from drift.

## Hard Stops

- Do not cite SSOT as a preference without naming the duplicated fact and owner.
- Do not demand a shared abstraction when a direct import, schema reference,
  generated output, or derivation is sufficient.
- Do not treat tests and snapshots as runtime sources of truth unless they are
  driving generated behavior or duplicated rules.

## Phase Output

- Return SSOT findings, accepted exceptions, owner decisions, recommended
  corrections, and any overlap handoffs.
