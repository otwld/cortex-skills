# Skill Evolution Review

## Overview

Review skill changes for durable ownership, metadata/lifecycle consistency, and
validation coverage.

## Workflow

1. Inspect `skill.yaml` for precise facets rather than prose copied from old
  keyword lists.
2. Confirm lifecycle files are phase-specific. Activation decides applicability,
  planning decides scope, execution governs edits, review or verification checks
  evidence.
3. Confirm every declared lifecycle file exists, and every kept lifecycle file is
  declared.
4. Check declared references, scripts, templates, and assets are used by the artifact;
  unused private resources are removed or the declaration is corrected.
5. Confirm the change avoids private coupling between artifacts. Shared material is used
  only through declared shared resources.
6. Confirm validation expectations are named. Generated outputs are rebuilt only by the
  task owner responsible for generated files.

## Quality Gates

- A lifecycle file could be moved to another artifact unchanged.
- Metadata says the artifact handles a surface that lifecycle files never
  govern.
- A new artifact exists mainly to document a current task preference.
- A resource is linked from prose but missing from `skill.yaml`.
- Review cannot identify the command or evidence that proves the change is
  fresh.

## Hard Stops

- Do not approve a change that leaves obsolete relation-style routing language
  in metadata.
- Do not approve undeclared resource use.
- Do not approve a lifecycle set where active artifacts have zero declared
  phases.

## Phase Output

Return findings ordered by severity, files requiring correction, validation run
or intentionally deferred, and any unresolved ownership risk.
