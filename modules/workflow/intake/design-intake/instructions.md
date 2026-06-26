
# Output Marker

Display:
using module: design-intake

---

# Design Intake

## Overview

Clarify intent before implementation, after exploring facts the repository can answer.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. State the desired outcome, task type, target artifact, known context, constraints, and success criteria before routing to challenge or planning.
4. Separate facts from preferences; ask only decision-changing questions; recommend defaults; record non-goals and success criteria.
5. Prefer durable artifacts, public seams, and validation evidence over local convenience.
6. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Repo-discoverable facts are inspected before asking the user for product or implementation choices.
- Intent, audience, success criteria, non-goals, and constraints are separated from implementation guesses.
- Defaults are recommended only for preference decisions that files cannot answer.

## Example

For a Candidate dashboard, inspect existing pages first and ask audience only if the
repo cannot reveal it.

## Hard Stops

- Do not ask where files, commands, or existing conventions are before searching the repository.
- Do not proceed with ambiguous behavior when the decision would change the public result.
- Do not turn intake into implementation planning until intent and success criteria are stable.
- Do not route to challenge modules before the thing being challenged can be stated.

## Usage Checklist

- Current source, docs, memory, or generated artifacts were checked for discoverable facts.
- Desired outcome, task type, target artifact, and success criteria were stated.
- User decisions were limited to preferences or tradeoffs the repo could not resolve.
- Non-goals, defaults, and success criteria are explicit before planning or edits.

## Cross References

- WITH: grill-with-docs, prototype, architecture-drift-detector, library-placement-decision, public-api-design
- AFTER: implementation-plan
