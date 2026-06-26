# Example Universe Enforcer Run

## Overview

Use the recruitment job board universe for invented examples while keeping
examples small enough to expose the behavior being demonstrated.

## Workflow

1. Replace generic placeholders such as Foo, Bar, User, Product, Item, Test, and
   ExampleEntity when they appear in invented sample data.
2. Use the core entities from `references/recruitment-universe.md`: JobOffer,
   Candidate, Application, Recruiter, Company, Interview, Contract, and SkillTag.
3. Keep entity relationships plausible: applications connect candidates to job
   offers, recruiters manage job offers, and interviews or contracts belong to an
   application.
4. Limit sample records to the smallest set that proves the contract, state
   transition, UI state, or validation rule.
5. Preserve real project data supplied by the user or already present in the
   system under test.

## Quality Gates

- Every invented entity belongs to the recruitment universe or has a task-specific
  reason to exist.
- Sample data uses coherent names, fields, and links instead of mixing unrelated
  domains.
- Fixtures and snippets remain focused on the behavior, not broad world-building.

## Hard Stops

- Do not introduce unrelated invented domains for convenience.
- Do not convert real user-provided data into recruitment examples.
- Do not add large fixtures when one or two records would prove the behavior.

## Phase Output

- Return the example artifacts changed, placeholder replacements made, preserved
  real data, and any exception to the recruitment universe.
