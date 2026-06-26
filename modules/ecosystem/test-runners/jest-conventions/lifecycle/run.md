# Jest Conventions Run

## Overview

Implement Jest tests and runner changes that prove behavior through stable
interfaces, use deterministic fixtures, and keep global runner state small.

## Workflow

- Write assertions against outcomes a caller can observe: returned values,
  thrown errors, emitted events, persisted records, rendered text, command
  output, or calls to a real boundary adapter.
- Use table data or named fixtures only when they make the behavior easier to
  audit. Avoid fixture factories that hide the important inputs.
- Use `jest.fn()` and spies for callbacks, boundary adapters, and indirect
  outputs. Do not assert call order or call counts unless those calls are the
  contract.
- Use module mocks for external boundaries. Keep user-module manual mocks in
  the appropriate `__mocks__` location, and require the test to opt into the mock
  where Jest requires that opt-in.
- Keep `jest.config.*` JSON-serializable, narrow, and consistent with existing
  project entries. Prefer extending existing defaults or project config over
  creating a parallel runner path.
- Put shared assertion setup, custom matchers, and cleanup hooks in
  `setupFilesAfterEnv` only when several tests benefit. Keep application data
  construction in tests or fixtures instead of global setup.
- Restore fake timers, system time, spies, module mocks, and mutated globals in
  local cleanup hooks. A passing test file must not depend on execution order.
- For recruitment-domain examples, express behavior through public concepts such
  as Candidates, JobOffers, Applications, Recruiters, or submitted search
  filters instead of repository internals.

## Quality Gates

- Changing `testEnvironment` must include evidence that the affected tests need
  DOM APIs or Node-only behavior.
- Changing transforms, aliases, or project matching must include the exact files
  now included or excluded and the reason the current config cannot handle them.
- Adding a custom matcher must replace repeated assertion noise with a clearer
  domain assertion. One-off expectations should stay inline.
- Adding setup files must document which repeated test concern they handle:
  matcher registration, test-library cleanup, fake boundary installation, or
  deterministic environment state.

## Hard Stops

- Do not make production code more mockable at the cost of its public contract.
- Do not add snapshots where a direct behavioral assertion would be clearer.
- Do not broaden config patterns until the current runner selection and affected
  files are known.
- Do not leave skipped or focused tests behind.

## Phase Output

- Summarize changed tests/config, public behavior covered, mock boundaries,
  global state touched, cleanup strategy, and the command needed for focused
  validation.
