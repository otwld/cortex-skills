# Architecture Deepening Review Activate

## Overview

Activate when a task asks whether an existing module, interface, or abstraction
is too shallow, too broad, poorly tested, or carrying behavior in the wrong
place.

## Workflow

1. Read `shared/architecture-deepening.md` for the vocabulary and deletion test.
2. Read `shared/project-memory.md` when durable architecture context may exist.
3. Inspect the public interface, implementation files, tests, and callers of the
   candidate module.
4. Inspect behavior spread across routes, repositories, UI, data access, adapters,
   or helpers.
5. Classify dependencies as in-process, local-substitutable, remote-owned, or
   true external collaborators.

## Quality Gates

- The candidate is a named module, interface, owner, workflow, or project area.
- The deletion-test result names behavior hidden or not hidden by the interface.
- Activation identifies the interface tests should cross.

## Hard Stops

- Do not recommend a deeper module without naming the behavior it hides.
- Do not create a seam for one hypothetical adapter unless the current design
  already pays for it.
- Do not turn a focused deepening review into a broad rewrite.

## Phase Output

- State the candidate, deletion-test result, dependency classifications,
  suspected test surface, loaded resources, and unknown evidence.
