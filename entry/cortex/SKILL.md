---
name: cortex
description: Use only when the user explicitly includes $cortex; routes work through the Cortex routed skill workspace and its hidden modules.
---

# Output Marker

Display:
using skill: cortex

---

# Cortex

## Overview

Route explicit `$cortex` requests through the hidden modules in this routed skill workspace.

Use routed workspace metadata as the source of truth:

- `../../routed-skills.yaml`
- `../../generated/SKILL_CATALOG.md`
- `../../generated/module-graph.md`
- `../../generated/module-cascade.md`

## Workflow

1. Inspect the request and relevant files for direct routing evidence.
2. Select routed modules using `../../generated/module-cascade.md`.
3. Expand required `before` relations from `../../generated/module-graph.md` up to the configured depth cap.
4. Add `with` modules only when they have independent evidence.
5. Defer `after` modules until the later phase is relevant.
6. Reject excluded module combinations.
7. Use local or shared resources only when a selected module declares them.

## Gates

- `$cortex` is invoked only through explicit user request.
- Routed modules remain hidden behind this public entry point.
- Generated artifacts are derived from `skill.yaml` metadata.
- Routing decisions remain inspectable through generated catalog, graph, and cascade files.

## Hard Stops

- Do not use this skill through implicit invocation.
- Do not load hidden modules without direct evidence or required relations.
- Do not treat generated catalog, graph, or cascade files as source files.
- Do not add hidden resource coupling; modules must declare resource ownership or use.

## Output Format

State the selected modules and any skipped tempting modules when routing is broad or ambiguous.

## Checklist

- Generated catalog was available.
- Generated graph was available.
- Generated cascade was available.
- Relations and exclusions were respected.

## Cross References

- Routed entry metadata: `skill.yaml`
- UI metadata: `agents/openai.yaml`
- Catalog: `../../generated/SKILL_CATALOG.md`
- Graph: `../../generated/module-graph.md`
- Cascade: `../../generated/module-cascade.md`
