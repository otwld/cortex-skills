
# Output Marker

Display:
using module: architecture-drift-detector

---

# Architecture Drift Detector

## Overview

Detect early structural risk from churn, repeated fixes, and ownership drift before it
becomes a rewrite.

## Reference Routing

- Use `shared/architecture-deepening.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Use concrete signals; escalate only when risk is tied to a module, seam, package, or project area; recommend focused review instead of broad rewrites.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Drift claims are tied to concrete churn, ownership spread, dependency direction, or responsibility movement.
- Risk is scoped to a named module, seam, package, workflow, or project area.
- The recommendation is a focused review or constraint, not an unbounded rewrite.

## Example

Three changes touch Candidate search, Application persistence, and query helpers;
recommend reviewing the search seam before adding another filter.

## Hard Stops

- Do not infer architecture drift from file count or personal preference alone.
- Do not escalate drift without naming the area where ownership or dependency direction is eroding.
- Do not propose new architecture layers before checking existing owners and boundaries.

## Usage Checklist

- Recent changes, current files, or request evidence were inspected for drift signals.
- Ownership, dependency direction, and repeated-change risk were localized.
- The next action is a bounded review, constraint, or module-specific fix.

## Cross References

- WITH: architecture-deepening-review, library-placement-decision, nx-module-boundaries
