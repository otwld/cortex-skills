
# Output Marker

Display:
using module: skill-evolution

---

# Skill Evolution

## Overview

Evolve focused modules when repeated patterns or agent failure modes deserve reusable
guidance.

## Reference Routing

- Use `shared/skill-quality-standard.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Analyze responsibility and consumers; compare existing modules; update before creating; sync metadata, graph, catalog, references, and validation.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Skill changes respond to repeated agent failure, durable workflow need, or a concrete doctrine gap.
- Existing modules, signals, relations, resources, and generated artifacts are compared before creating new surface area.
- Metadata, instructions, templates, references, generated views, and validation stay synchronized.

## Example

Repeated mistakes around issue briefs justify issue-decomposition plus an agent-brief
reference, not scattered planning bullets.

## Hard Stops

- Do not create a new module when updating or narrowing an existing one solves the gap.
- Do not add guidance that only documents a one-off preference or current task detail.
- Do not change skill behavior without updating routing metadata and validation expectations together.

## Usage Checklist

- Recurring pattern or failure mode was identified from concrete evidence.
- Overlap with existing modules and resources was checked before editing.
- Metadata, instructions, generated artifacts, tests, and docs were updated as one change.

## Cross References

- None
