# Architecture Deepening Review Review

## Overview

Review deepening changes for a meaningful behavior boundary, explicit dependency
classification, public-interface tests, and bounded scope.

## Workflow

1. Inspect public interface diff, implementation movement, caller updates, and
   test changes.
2. Inspect dependency classifications and any new adapters or substitute
   collaborators.
3. Inspect project memory or ADR updates when the recommendation records durable
   architecture intent.

## Quality Gates

- The interface hides more behavior than it exposes.
- Dependency classifications are explicit and match current code.
- Tests cross the supported interface and cover the behavior moved behind it.
- Scope remains limited to the named candidate and its callers.

## Hard Stops

- Reject abstractions whose interface mostly forwards to existing helpers.
- Reject tests that still reach private helpers after the public interface
  changed.
- Reject seams introduced for one hypothetical collaborator.
- Reject recommendations that name architecture depth but not hidden behavior.

## Phase Output

- Return deepening findings with the affected interface, hidden behavior,
  dependency risks, test-surface gaps, and validation evidence.
