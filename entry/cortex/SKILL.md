---
name: cortex
description: Use only when the user explicitly includes $cortex; routes work through Cortex atoms, lifecycle phases, and local run traces.
---

# Cortex

## Overview

Route explicit `$cortex` requests through Cortex atoms selected by structured
facets and lifecycle phase coverage. The entry router is the orchestrator: it
boots local config, records a run trace, selects atoms, invokes commands or
modules when needed, and moves through lifecycle phases with human checkpoints.

Use routed workspace metadata as the source of truth:

- `../../routed-skills.yaml`
- `../../generated/SKILL_CATALOG.md`
- `../../generated/module-graph.md`
- `../../generated/module-cascade.md`

## Workflow

1. Accept the request only when the user explicitly includes `$cortex` or when a command emits a `Router handoff:` block containing a literal `$cortex` request.
2. Start `.cortex/runs/{date-slug}/` and write `request.md` before normal routing.
3. Read `.cortex/config.json`; if missing, invoke the Cortex config command atom to scaffold the default phase config and record the bootstrap in the run trace.
4. Run phases in order: `activate`, `plan`, `run`, `review`, `verify`, and `finalize`.
5. Display phase progress, for example `Starting phase: activate`, `Activated modules: ...`, and `Completed phase: plan`.
6. During `activate`, collect direct evidence from the user request and relevant files, then select atoms by structured facets and declared lifecycle phase files.
7. Add phase-specific `always` atoms from `.cortex/config.json` for the current phase.
8. When a phase is substantial, spawn one subagent to own the whole phase; the subagent returns visible phase output plus hidden trace data.
9. Write phase traces as `activate.json`, `plan.json`, `run.json`, `review.json`, `verify.json`, and `finalize.json` as phases complete.
10. Pass hidden phase trace forward so later phases know the activated atoms, matched facets, lifecycle files read, unresolved questions, and next-phase inputs.
11. Ask the operator only for decisions that change scope, behavior, validation, or the durable artifact.
12. Use local or shared resources only when an invoked atom declares them.

## Gates

- `$cortex` is invoked only through explicit user request or a valid command handoff block.
- Routed modules remain hidden behind this public entry point.
- Generated artifacts are derived from `skill.yaml` metadata.
- Modules are selected by structured facets and lifecycle coverage, not peer-module relations.
- Commands are public atoms; `$cortex` may invoke them when orchestration requires it.
- Phase traces are local full-fidelity artifacts under `.cortex/runs/`.
- Public entry and command skills expose complete `agents/openai.yaml` UI metadata and keep implicit invocation disabled.

## Hard Stops

- Do not use this skill through implicit invocation.
- Do not treat ordinary prose, examples, or docs that mention `$cortex` as command handoffs; the active boundary is the `Router handoff:` block.
- Do not inherit command-owned references, templates, assets, scripts, or private context unless the handoff block includes that context or the invoked command declares it.
- Do not load hidden modules through `before`, `with`, `after`, `excludes`, or `replaces`; those relation concepts are obsolete.
- Do not treat generated catalog, graph, or cascade files as source files.
- Do not add hidden resource coupling; modules and commands must declare resource ownership or use.

## Output Format

Show phase progress lines and concise phase results. Keep routing evidence,
matched facets, lifecycle files used, and next-phase inputs in the run trace
rather than flooding the user-facing response.

When questions are needed, ask intent questions before design tradeoffs, and
design tradeoffs before implementation details.

## Checklist

- Generated catalog was available.
- Generated graph was available and interpreted as a facet/lifecycle graph.
- Generated cascade was available.
- Invocation came from explicit `$cortex` use or a valid `Router handoff:` block.
- `.cortex/runs/{date-slug}/request.md` was written.
- `.cortex/config.json` was read or scaffolded through the config command atom.
- Phase progress was reported.
- Activated atoms had direct facet evidence, phase config, or a lifecycle role.
- Phase traces were written and passed forward.
- Command atoms were invoked only when orchestration required them.

## Source Artifacts

- Routed entry metadata: `skill.yaml`
- UI metadata: `agents/openai.yaml`
- Catalog: `../../generated/SKILL_CATALOG.md`
- Graph: `../../generated/module-graph.md`
- Cascade: `../../generated/module-cascade.md`
