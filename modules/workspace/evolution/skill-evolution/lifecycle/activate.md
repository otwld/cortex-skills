# Skill Evolution Activate

## Overview

Decide whether the request is truly about durable Cortex skill behavior rather
than a one-time task instruction, local implementation detail, or ordinary
documentation cleanup.

## Workflow

1. Inspect user request language that asks to create, split, retire, narrow, or rewrite a
  skill artifact.
2. Identify repeated agent failures, repeated review comments, or recurring workflow gaps
  that would predictably appear in future work.
3. Read the current `skill.yaml`, declared lifecycle files, and declared resources for
  each artifact under consideration.
4. Read `shared/skill-quality-standard.md` when the task evaluates general skill
  quality, routing evidence, or lifecycle substance.
- State the artifact responsibility in one sentence: what behavior it owns, what
  evidence selects it, and what users or agents can rely on.

## Quality Gates

- Activate only for reusable guidance, routing facets, lifecycle behavior,
  declared resources, or validation expectations.
- Treat a single project preference as insufficient unless the user explicitly
  wants it turned into reusable Cortex doctrine.
- Prefer narrowing or correcting an existing artifact when that fully covers the
  gap.

## Hard Stops

- Do not create a new skill artifact from a one-off task detail.
- Do not continue when the desired ownership is unclear enough that two artifacts
  could reasonably own the same behavior.
- Do not change lifecycle behavior unless the matching metadata and validation
  expectations can change in the same task scope.

## Phase Output

Return the activation decision, the durable evidence that justifies it, the
artifact responsibility sentence, required local resources, and any ownership
question that must be resolved.
