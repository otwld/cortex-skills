
# Output Marker

Display:
using module: code-documentation

---

# Code Documentation

## Overview

Make documentation part of the code change rather than a cleanup pass.

## Reference Routing

- Use `shared/skill-quality-standard.md` when this task touches that concern.
- Use `shared/recruitment-universe.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Document touched public or reusable surfaces; move docs with code; update Storybook or MDX where that is the docs surface; avoid placeholder comments.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Code Documentation guidance names the inspected source, request evidence, or declared resource that triggered it.
- Code Documentation output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Code Documentation decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Code Documentation validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

A reusable CandidateCard documents required data, empty states, and selection behavior
instead of commenting each template line.

## Hard Stops

- Do not use Code Documentation without direct routing evidence or a required relation.
- Do not expand Code Documentation beyond its stated responsibility.
- Do not add placeholder Code Documentation guidance, examples, metadata, resources, or validation.
- Do not claim Code Documentation is satisfied without evidence for its checklist.

## Usage Checklist

- Code Documentation trigger evidence is explicit.
- Code Documentation source files, project memory, or declared resources were checked.
- Code Documentation workflow rules were applied at the relevant artifact boundary.
- Code Documentation docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Code Documentation risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: example-universe-enforcer, storybook-conventions
- AFTER: skill-evolution
