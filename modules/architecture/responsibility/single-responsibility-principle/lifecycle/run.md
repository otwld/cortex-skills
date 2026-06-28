# Single Responsibility Principle Run

## Overview

Implement code changes while keeping each touched unit focused on one reason to
change.

## Workflow

1. Keep responsibility boundaries visible while editing each file, function,
   method, class, component, hook, service, controller, command, provider,
   schema, or module.
2. Move validation, mapping, persistence, networking, UI, configuration, or
   business behavior apart only when they have independent change drivers.
3. Preserve cohesive orchestration when multiple steps serve one use case and
   one owner should control the sequence.
4. Name new units after their responsibility, not their pattern or convenience.
5. Update callers, tests, docs, and examples affected by any split or
   keep-together decision.

## Quality Gates

- New or changed units have a clear responsibility sentence.
- Split units remove a real independent reason to change from the original unit.
- Remaining mixed concerns are justified as one cohesive use case or lifecycle.
- Tests or static review evidence cover the behavior through the responsible
  owner.

## Hard Stops

- Do not create pass-through wrappers, shallow files, or generic helpers to claim
  SRP compliance.
- Do not move code across ownership boundaries without the relevant architecture
  module decision.
- Do not make callers coordinate sequencing that a single owner should keep.

## Phase Output

- Return units changed, responsibility boundaries kept or split, caller updates,
  validation run or static evidence, and any deferred SRP risk.

