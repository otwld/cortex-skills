# Grill With Docs Activate

## Overview

Decide whether a known intent, plan, term, domain rule, or durable decision needs
a docs-grounded challenge session.

## Workflow

1. State the specific artifact or statement the user wants challenged.
2. Read project memory guidance for durable context and memory file ownership.
3. Inspect domain glossary terms that may constrain vocabulary.
4. Apply ADR guidance for decisions that are hard to reverse or surprising.
5. Check source files, docs, tests, or issue text that can answer factual
   questions.

## Quality Gates

- The user asks for grilling, challenge, deeper questions, stress testing, or
  decision-changing interrogation.
- The target being challenged can be stated in one sentence.
- Existing memory, glossary, ADRs, docs, or source facts can ground the questions.
- The likely answers would change scope, terminology, acceptance criteria, or a
  durable decision record.

## Hard Stops

- The target is undefined or the request is still only a vague goal.
- The question is factual and local evidence can answer it.
- The challenge would generate broad interview questions rather than expose a
  concrete tradeoff.
- The decision is routine implementation detail that does not belong in durable
  memory.

## Phase Output

Return:

- The exact statement, term, or decision being challenged.
- Evidence consulted from memory, glossary, ADR guidance, docs, or source.
- The decision boundary: what answer would change.
- Whether durable memory, glossary, or ADR follow-up may be needed.
