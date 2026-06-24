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

1. Accept the request only when the user explicitly includes `$cortex` or when a directly invoked command emits a `Router handoff:` block containing a literal `$cortex` request.
2. Load always-loaded modules listed in `../../generated/module-cascade.md`.
3. Run an intent-understanding gate: state the desired outcome, task type, artifact target, known context, constraints, and whether the user is asking for questions, audit, plan, implementation, review, or explanation.
4. For command handoffs, treat only the handoff block as passed context; inspect files normally instead of inheriting command-owned resources.
5. If goal, scope, outcome, audience, or success criteria are unclear, route `design-intake` before challenge, planning, implementation, or review modules.
6. Inspect relevant files for repository evidence; do not ask questions the repository can answer.
7. Route `grill-with-docs` only after the request can be stated clearly enough to challenge; challenges clarify or stress-test known intent rather than replacing basic understanding.
8. Select additional routed modules using `../../generated/module-cascade.md`, classifying them as selected, candidate, deferred, or skipped when routing is broad or ambiguous.
9. Ask operator questions only for candidate modules where the answer changes the plan, execution path, review depth, validation, or durable artifact.
10. Expand required `before` relations from `../../generated/module-graph.md` up to the configured depth cap.
11. Add `with` modules only when they have independent evidence.
12. Defer `after` modules until the later phase is relevant.
13. Reject excluded module combinations.
14. Use local or shared resources only when a selected module declares them.

## Gates

- `$cortex` is invoked only through explicit user request.
- Command handoff invocation is accepted only through a `Router handoff:` block
  containing a literal `$cortex` request.
- Routed modules remain hidden behind this public entry point.
- Generated artifacts are derived from `skill.yaml` metadata.
- Strong, medium, and weak signals describe request or repository evidence directly.
- Routing decisions remain inspectable through generated catalog, graph, and cascade files.
- Public entry and command skills expose complete `agents/openai.yaml` UI metadata and keep implicit invocation disabled.
- Challenge and planning modules are selected only after the request intent can be stated.

## Hard Stops

- Do not use this skill through implicit invocation.
- Do not treat ordinary prose, examples, or docs that mention `$cortex` as
  command handoffs; the active boundary is the `Router handoff:` block.
- Do not inherit command-owned references, templates, assets, scripts, or other
  private context unless the handoff block includes that context.
- Do not load hidden modules unless they are always-loaded, directly evidenced, or required by relations.
- Do not treat generated catalog, graph, or cascade files as source files.
- Do not add hidden resource coupling; modules must declare resource ownership or use.

## Output Format

State the selected modules and any skipped tempting modules when routing is broad or ambiguous.
When questions are needed, ask intent questions before design tradeoffs, and design
tradeoffs before implementation details.

## Checklist

- Generated catalog was available.
- Generated graph was available.
- Generated cascade was available.
- Invocation came from explicit `$cortex` use or a valid `Router handoff:` block.
- Always-loaded modules were loaded before evidence-selected modules.
- Intent, task type, target artifact, and desired outcome were stated before challenge or planning.
- Selected modules had direct evidence or a required `before` relation.
- Candidate, deferred, and skipped modules were named when routing was broad or ambiguous.
- Relations and exclusions were respected.
- Command skills were left out of routed cascade selection unless directly invoked.

## Cross References

- Routed entry metadata: `skill.yaml`
- UI metadata: `agents/openai.yaml`
- Catalog: `../../generated/SKILL_CATALOG.md`
- Graph: `../../generated/module-graph.md`
- Cascade: `../../generated/module-cascade.md`
