
# Output Marker

Display:
using module: prototype

---

# Prototype

## Overview

Build disposable code that answers one design question and is deleted or absorbed
afterward.

## Reference Routing

- Use `shared/prototype-guidance.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. State the question; choose logic or UI branch; isolate throwaway shell; use in-memory state; provide one command; capture the answer.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- The prototype answers one named design or state-model question and stays isolated from production paths.
- UI and logic prototypes use the smallest shell that can prove the decision.
- The captured answer says whether to delete, absorb, or discard the prototype work.

## Example

An Interview scheduling state-machine prototype tests reschedule and cancellation cases
before the real module design.

## Hard Stops

- Do not let prototype code become a hidden production dependency.
- Do not prototype multiple unrelated questions in one throwaway shell.
- Do not add persistence, backend wiring, or design-system expansion unless the question requires it.

## Usage Checklist

- Prototype question, branch type, and disposal path were stated first.
- Implementation stayed isolated with in-memory or minimal state by default.
- Result, command, and delete-or-absorb recommendation were captured.

## Cross References

- WITH: design-intake, test-first-discipline, code-documentation
- AFTER: issue-decomposition
