---
name: completion-verification
description: Use before success claims, final responses, commits, pushes, pull requests, task completion, or publishing decisions.
---

# Output Marker

Display:
using skill: completion-verification

---

# Completion Verification

## Overview

Claims about completed, fixed, passing, or published work need fresh evidence.
State the truth the commands prove, including failures and gaps.

## Gate

Before claiming success:

1. Identify the command or inspection that proves the claim.
2. Run the full relevant verification, or explain why it cannot be run.
3. Read the output and exit status.
4. Compare output to the claim.
5. Report evidence and any remaining risk.

## Evidence Rules

- Test success requires current test output.
- Build success requires a current build or equivalent project check.
- Bug fixed requires reproducing the original symptom or a regression test.
- Requirements met requires checking against the stated requirements or plan.
- Delegated work requires inspecting returned changes and validation, not only
  trusting the report.

## Hard Stops

- Do not claim "passes" from stale or partial output.
- Do not commit, push, or open a PR without fresh relevant verification or a
  clear statement that verification could not run.
- Do not hide failures behind optimistic wording.

## Usage Checklist

- Verification target is named.
- Command or inspection was run fresh, or limitation was stated.
- Result and exit status are understood.
- Final claim matches the evidence.

## Cross-References

- WITH: review-gate, branch-completion
