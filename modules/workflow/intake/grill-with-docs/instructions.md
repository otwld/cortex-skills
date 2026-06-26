
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
3. Confirm the intent, plan, artifact, vocabulary, or decision being challenged before asking challenge questions.
4. Read memory first; explore facts instead of asking; ask one decision-changing question at a time; update glossary terms inline; offer ADRs sparingly.
5. Prefer durable artifacts, public seams, and validation evidence over local convenience.
6. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Questions are grounded in existing memory, glossary terms, ADRs, docs, or source facts.
- Each question changes the decision, locks an assumption, or exposes a meaningful tradeoff.
- Durable vocabulary or decision changes are routed to glossary, ADR, or memory artifacts.

## Example

If “active candidate” is fuzzy, ask whether it means submitted, interviewing, or not
rejected, then record the chosen term.

## Hard Stops

- Do not grill the user on facts that source files or project memory can answer.
- Do not challenge an undefined request; route design-intake first when intent is unclear.
- Do not ask broad interview-style question lists when one decision blocks progress.
- Do not create ADR or glossary churn for routine implementation choices.

## Usage Checklist

- Project memory and relevant docs were checked before questioning.
- The thing being challenged was stated before questions began.
- Questions were limited to decision-changing gaps.
- New durable terms or decisions were assigned to the correct memory artifact.

## Cross References

- WITH: design-intake, implementation-plan
- AFTER: issue-decomposition
