# Design Intake Plan

## Overview

Produce a stable intake summary, not an implementation sequence. The summary must
make the user's desired result explicit enough that later work does not invent
requirements.

## Workflow

1. Capture desired outcome in user-facing language.
2. Classify task type: build, change, fix, review, investigate, design, document,
   or compare.
3. Name the target artifact or surface and primary audience or actor.
4. State success criteria, validation expectations, constraints, non-goals, and
   accepted defaults.
5. Ask only questions whose answers change scope, behavior, acceptance criteria,
   or validation.
6. Group non-blocking preference questions behind a recommended default.

## Quality Gates

- Repository facts are presented separately from guesses and preferences.
- The question set is the smallest useful set; when one answer unlocks progress,
  that question comes first.
- Success criteria are observable.
- Non-goals are explicit when adjacent enhancements are plausible.

## Hard Stops

- A question asks the user to repeat repository information that local evidence
  can answer.
- The intake summary still mixes facts, assumptions, and preferences.
- Success criteria are phrased as vague satisfaction claims rather than observable
  outcomes.
- Non-goals are omitted for work that has obvious adjacent enhancements.

## Phase Output

Return:

- Intake summary with facts, decisions, assumptions, non-goals, and success
  criteria in separate sections.
- Open questions, ordered by how much each answer changes the outcome.
- Recommended defaults and the reason each is safe.
- Readiness statement: `ready for planning`, `ready for implementation`, or
  `blocked on user decision`.
