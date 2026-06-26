# Skill Evolution Plan

## Overview

Plan skill artifact changes as a synchronized metadata, lifecycle, resource, and
validation update.

## Workflow

1. Read the current artifact metadata, lifecycle files, declared resources, and
  any prior content needed to preserve useful doctrine.
2. Classify the change as one of: add artifact, retire artifact, narrow
  responsibility, broaden responsibility, rewrite lifecycle behavior, update
  routing facets, or change declared resources.
3. Define the smallest durable behavior that solves the observed gap. The plan
  must name the evidence that future routing or review can inspect.
4. Decide which lifecycle phases have distinct work. Keep only phases that add
  phase-specific decisions, hard stops, or validation expectations.
5. Identify generated files or catalogs that will need rebuild by the task owner
  responsible for generated output. Do not hand-edit generated files.

## Quality Gates

- The plan keeps routing evidence in `skill.yaml` and execution guidance in
  lifecycle files.
- The plan names every file family that must change together: metadata,
  lifecycle, resources, templates, assets, tests, generated views, or docs.
- The plan removes obsolete behavior instead of layering compatibility prose on
  top of it.
- The planned lifecycle text can be falsified through concrete evidence,
  commands, review checks, or hard stops.

## Hard Stops

- Do not plan duplicate guidance when updating an existing artifact would make
  the ownership clearer.
- Do not keep a lifecycle phase that only repeats another phase.
- Do not rely on private resource sharing; every needed resource must be
  declared by the consuming artifact.

## Phase Output

Return the selected change type, the minimum file set, phases to keep or delete,
resource declarations to add or remove, generated-output responsibility, and
validation commands expected for the change.
