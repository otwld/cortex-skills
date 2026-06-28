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
6. During `activate`, run the Intent Derivation Gate before module selection.
7. Select atoms from the confirmed intent model by structured facets and declared lifecycle phase files; do not rely only on literal prompt words.
8. Add phase-specific `always` atoms from `.cortex/config.json` for the current phase.
9. When a phase is substantial, spawn one subagent to own the whole phase; the subagent returns visible phase output plus hidden trace data.
10. Write phase traces as `activate.json`, `plan.json`, `run.json`, `review.json`, `verify.json`, and `finalize.json` as phases complete.
11. Pass hidden phase trace forward so later phases know the intent model, activated atoms, matched facets, lifecycle files read, unresolved questions, and next-phase inputs.
12. Ask the operator only for decisions that change scope, behavior, validation, or the durable artifact.
13. Use local or shared resources only when an invoked atom declares them.

## Intent Derivation Gate

Before selecting atoms in `activate`, derive a generic intent model from the
request and local evidence. Inspect the explicit request, embedded plans, recent
user turns available in context, mentioned paths, repository structure,
generated artifacts, and relevant local metadata.

Record these fields in `.cortex/runs/{date-slug}/activate.json`:

- `explicit_intents`
- `inferred_intents`
- `operation_type`
- `affected_surfaces`
- `expected_artifacts`
- `risk_profile`
- `validation_needs`
- `excluded_scope`
- `confidence`
- `user_validated`
- `module_retrieval_query`
- `activated_modules`
- `missing_coverage`

Keep detailed evidence in the trace. Show only a concise user-facing activation
summary: derived intent, validation question if one is needed, activated modules,
and missing coverage.

Ask the operator before module retrieval only when confidence is low, several
plausible intents imply different modules, scope would expand materially, or the
missing decision changes validation or artifact ownership.

Retrieve modules from the confirmed intent model. Match facets and lifecycle
coverage using derived surfaces, risks, expected artifacts, operation type, and
validation needs. If the intent model expects a responsibility but no module
exists, record it in `missing_coverage` and surface that during activation. Do
not add a generic fallback module.

## Gates

- `$cortex` is invoked only through explicit user request or a valid command handoff block.
- Routed modules remain hidden behind this public entry point.
- Generated artifacts are derived from `skill.yaml` metadata.
- Modules are selected from the confirmed intent model by structured facets and lifecycle coverage, not peer-module relations.
- Commands are public atoms; `$cortex` may invoke them when orchestration requires it.
- Phase traces are local full-fidelity artifacts under `.cortex/runs/`.
- Later phases use the activation intent model when planning, executing, reviewing, verifying, and finalizing work.
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
- Intent was derived and validated before module retrieval when required.
- Activated atoms had intent-model evidence, phase config, or a lifecycle role.
- Missing module coverage was recorded when expected responsibilities had no owner.
- Phase traces were written and passed forward.
- Command atoms were invoked only when orchestration required them.

## Source Artifacts

- Routed entry metadata: `skill.yaml`
- UI metadata: `agents/openai.yaml`
- Catalog: `../../generated/SKILL_CATALOG.md`
- Graph: `../../generated/module-graph.md`
- Cascade: `../../generated/module-cascade.md`
