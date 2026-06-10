---
name: review-feedback-triage
description: Use when receiving code review, CI review, agent review, or external technical feedback before implementing suggested changes.
---

# Output Marker

Display:
using skill: review-feedback-triage

---

# Review Feedback Triage

## Overview

Review feedback is input to evaluate, not an order to apply blindly. Verify the
claim, understand the intent, and implement one coherent fix at a time.

## Workflow

1. Read all feedback before changing files.
2. Group related findings.
3. Clarify anything that affects scope or correctness.
4. Verify each claim against current code and requirements.
5. Decide: fix, defer, reject with technical reason, or ask the user.
6. Implement accepted fixes in risk order.
7. Test each meaningful fix and re-run relevant verification.

## Rules

- Treat user feedback as authoritative on intent, but still clarify scope.
- Treat external or agent feedback as a hypothesis to verify.
- Push back when feedback breaks requirements, violates architecture, or adds
  unused scope.
- Do not batch unrelated fixes if that hides which change resolved the issue.

## Hard Stops

- Feedback is unclear and implementation would guess intent.
- A suggestion conflicts with prior user or architecture decisions.
- A reviewer requests broad "proper" implementation for unused behavior.

## Usage Checklist

- Feedback was read and grouped.
- Unclear items were clarified before implementation.
- Accepted and rejected findings have technical reasons.
- Fixes were validated individually or by coherent batch.

## Cross-References

- WITH: systematic-debugging, test-first-discipline, completion-verification, review-gate
