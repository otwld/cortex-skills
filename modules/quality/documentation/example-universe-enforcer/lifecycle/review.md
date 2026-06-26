# Example Universe Enforcer Review

## Overview

Review examples for placeholder leakage, mixed domains, and fixtures that obscure
the behavior they are meant to demonstrate.

## Workflow

1. Inspect changed examples, stories, fixtures, tests, docs snippets, DTO samples,
   and payload samples.
2. Flag generic placeholders and unrelated invented domains when the task did not
   require them.
3. Check that recruitment examples use coherent entity links and field names.
4. Check that real user-provided data was preserved when it was material.
5. Separate correctness issues from optional naming polish.

## Quality Gates

- Findings name the exact sample artifact and the placeholder, domain mismatch,
  incoherent relationship, or oversize fixture.
- Recruitment examples remain minimal and aligned to the behavior under review.
- User-provided real data is not treated as a placeholder merely because it is not
  part of the recruitment universe.

## Hard Stops

- Do not approve durable examples that contain Foo, Bar, ExampleEntity, Product,
  Item, or generic User records without a task-specific reason.
- Do not request conversion of real project data into recruitment examples.
- Do not allow mixed invented domains in one artifact when one coherent sample
  universe is enough.

## Phase Output

- Return review findings with artifact path, problematic sample data, and the
  smallest correction that restores coherence.
