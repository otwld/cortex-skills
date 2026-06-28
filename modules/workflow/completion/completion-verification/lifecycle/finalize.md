# Completion Verification Finalize

## Overview

Shape the final completion message so it matches the evidence instead of
overstating the result. Final wording must reflect the activation intent model
and the verification evidence attached to each explicit or inferred
requirement.

## Workflow

### Response Rules

- State what was completed in terms of the user's requirements.
- State completion against the derived intent, affected surfaces, expected
  artifacts, and validation needs.
- State validation evidence by command, inspection, artifact, or blocker.
- Name skipped checks and why they were skipped when they affect confidence.
- Separate completed work from residual risk and next steps.
- Use precise status wording. "Done" is reserved for claims that have evidence
  for all mandatory requirements.

## Quality Gates

- Completion wording matches the verified evidence map.
- Final wording does not ignore inferred requirements, missing coverage, or
  excluded scope recorded in the intent model.
- Passed, blocked, skipped, and not-run checks are distinguishable.
- Residual risk remains visible when evidence is incomplete.

## Hard Stops

- Do not say the task is complete when mandatory evidence is missing.
- Do not bury validation failures or skipped checks behind a broad success
  summary.
- Do not imply a repository, branch, deployment, or release state that was not
  inspected in the current turn.

## Phase Output

- Final completion wording allowed by the evidence.
- Intent-model coverage summary.
- Validation summary that distinguishes passed, blocked, skipped, and not-run
  checks.
- Residual risk or follow-up work, if any.
