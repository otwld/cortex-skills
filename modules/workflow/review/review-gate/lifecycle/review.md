# Review Gate Review

## Overview

Assess completed work against the user's requirements and the current diff,
prioritizing defects and regression risk over preference.

## Workflow

### Inspect

- Reconstruct the required behavior from the latest user request and any stated
  constraints.
- Inspect the changed files, public interfaces, tests, docs, generated outputs,
  dependency changes, and configuration changes.
- Compare validation evidence to the changed surface area. A passing unrelated
  command does not cover a risky change.
- Look for missing negative cases, broken compatibility, unintended file churn,
  stale docs, data handling mistakes, and unclear ownership boundaries.

### Finding Rules

- Start findings ordered by severity.
- Each finding must include a concrete file, line, artifact, or command result
  that lets another agent reproduce the concern.
- Describe the failing behavior and the user-visible or maintainer-visible risk.
- Separate blocking findings from non-blocking observations and follow-up ideas.
- If no findings exist, state that directly and name any remaining test gap.

## Quality Gates

- Requirements and diff scope are inspected prior to style or preference issues.
- Findings describe a reproducible failure mode and concrete risk.
- No-findings output still names the evidence inspected and remaining test gaps.

## Hard Stops

- Do not approve major work when requirement fit or validation coverage has not
  been inspected.
- Do not report vague concerns that cannot guide a fix.
- Do not mix unrelated improvement ideas into blocking review findings.
- Do not treat style preference as a defect unless it violates an explicit
  project rule.

## Phase Output

- Severity-ordered findings, or a clear no-findings statement.
- Evidence inspected: requirements, diff scope, tests, docs, contracts, and
  relevant artifacts.
- Required fixes, accepted residual risks, and validation needed following fixes.
