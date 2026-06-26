# Grill With Docs Plan

## Overview

Build a short challenge sequence from evidence, not from generic interview
templates. Each question must name the assumption it tests and the decision it
can change.

## Workflow

1. Ask one blocking question at a time when the answer can redirect the work.
2. Include the evidence that prompted the question: memory note, glossary term,
   ADR guidance, source behavior, doc statement, or test expectation.
3. Prefer contrastive choices over open-ended prompts when the tradeoff is known.
4. Capture the user's answer as a decision, rejected alternative, or glossary
   candidate.
5. Identify any proposed memory target and exact change; do not overwrite
   existing memory without approval.

## Quality Gates

- A glossary update is only for canonical domain language, not implementation
  slang.
- An ADR candidate is only for a choice that is hard to reverse, surprising
  without context, and grounded in a real tradeoff.
- Every question has an evidence source and expected decision impact.
- Unrelated challenge threads stay separate.

## Hard Stops

- A question has no evidence source.
- A question would not change the plan, vocabulary, acceptance criteria, or
  durable decision.
- Multiple unrelated challenge threads are bundled together.
- A memory update is proposed for a one-off implementation detail.

## Phase Output

Return:

- Prioritized challenge questions, each tied to evidence and expected impact.
- Decisions already locked by evidence.
- User answers captured as assumptions, glossary candidates, ADR candidates, or
  rejected alternatives.
- Exact durable-memory follow-up, if any.
