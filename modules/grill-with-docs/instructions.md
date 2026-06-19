
# Output Marker

Display:
using module: grill-with-docs

---

# Grill With Docs

## Overview

Run a deep alignment interview that challenges language and decisions against project
memory.

## Reference Routing

- Use `shared/project-memory.md` when this task touches that concern.
- Use `shared/domain-glossary.md` when this task touches that concern.
- Use `shared/adr-format.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read memory first; explore facts instead of asking; ask one decision-changing question at a time; update glossary terms inline; offer ADRs sparingly.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Grill With Docs guidance names the inspected source, request evidence, or declared resource that triggered it.
- Grill With Docs output uses this workspace's terms and the recruitment example universe only when examples are needed.
- Grill With Docs decisions land in metadata, instructions, resources, tests, or docs when they change future behavior.
- Grill With Docs validation names the command, artifact, review proof, or acceptance check that covers its risk.

## Example

If “active candidate” is fuzzy, ask whether it means submitted, interviewing, or not
rejected, then record the chosen term.

## Hard Stops

- Do not use Grill With Docs without direct routing evidence or a required relation.
- Do not expand Grill With Docs beyond its stated responsibility.
- Do not add placeholder Grill With Docs guidance, examples, metadata, resources, or validation.
- Do not claim Grill With Docs is satisfied without evidence for its checklist.

## Usage Checklist

- Grill With Docs trigger evidence is explicit.
- Grill With Docs source files, project memory, or declared resources were checked.
- Grill With Docs workflow rules were applied at the relevant artifact boundary.
- Grill With Docs docs, metadata, tests, or generated artifacts affected by the change were updated together.
- Grill With Docs risks, rejected paths, and validation gaps are stated.

## Cross References

- WITH: design-intake, implementation-plan
- AFTER: issue-decomposition
