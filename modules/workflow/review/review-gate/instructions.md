
# Output Marker

Display:
using module: review-gate

---

# Review Gate

## Overview

Review major work before publishing, starting with requirement fit before code quality.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Identify requirements and diff; review coverage; inspect correctness, tests, APIs, docs, and boundaries; classify findings; verify fixes.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Review starts from requirements and diff scope before style or preference issues.
- Findings identify correctness, test, API, docs, boundary, or regression risk with file evidence.
- Resolved findings are rechecked after fixes rather than assumed closed.

## Example

A module catalog review checks discoverability, routing, metadata, graph, and validation,
not just Markdown formatting.

## Hard Stops

- Do not approve major work without checking requirement fit and validation coverage.
- Do not report vague concerns that cannot guide a fix.
- Do not mix unrelated improvement ideas into blocking review findings.

## Usage Checklist

- Requirements, diff, tests, docs, APIs, and boundaries were reviewed in that order.
- Findings are severity-ranked and tied to concrete evidence.
- Fixes or accepted residual risks were revalidated before final review output.

## Cross References

- WITH: agent-delegation, completion-verification, review-feedback-triage, public-api-design, architecture-drift-detector
