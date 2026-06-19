
# Output Marker

Display:
using module: systematic-debugging

---

# Systematic Debugging

## Overview

Build a reliable feedback loop before fixing, then test falsifiable hypotheses instead
of guessing.

## Reference Routing

- Use `references/root-cause-tracing.md` when this task touches that concern.
- Use `references/defense-in-depth.md` when this task touches that concern.
- Use `references/condition-based-waiting.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read complete evidence; reproduce; rank hypotheses; probe one variable; fix root cause; add regression; remove instrumentation.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Systematic Debugging guidance names the inspected source, request evidence, or declared resource that triggered it.
- Systematic Debugging output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Systematic Debugging decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Systematic Debugging validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

If Candidate search drops results intermittently, replay one filter fixture until the
failure rate is debuggable before changing query code.

## Hard Stops

- Do not use Systematic Debugging without direct routing evidence or a required relation.
- Do not expand Systematic Debugging beyond its stated responsibility.
- Do not add placeholder Systematic Debugging guidance, examples, metadata, resources, or validation.
- Do not claim Systematic Debugging is satisfied without evidence for its checklist.

## Usage Checklist

- Systematic Debugging trigger evidence is explicit.
- Systematic Debugging source files, project memory, or declared resources were checked.
- Systematic Debugging workflow rules were applied at the relevant artifact boundary.
- Systematic Debugging docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Systematic Debugging risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: test-first-discipline, completion-verification, architecture-drift-detector
- AFTER: skill-evolution
