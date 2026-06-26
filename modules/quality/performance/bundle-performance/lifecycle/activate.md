# Bundle Performance Activate

## Overview

Identify changes that could add global runtime cost through shared imports,
entry points, side effects, or optional dependencies.

## Workflow

1. Match this module when a request or diff touches bundle size, tree-shaking,
   package exports, barrels, shared UI roots, runtime dependencies, lazy loading,
   side-effect declarations, global setup, or build configuration.
2. Name the broadest consumer path affected by the change.
3. Capture the dependency, entry point, import path, side effect, or chunk boundary
   that creates risk.
4. Decide whether static import inspection is enough or whether a bundle/build
   measurement is needed.

## Quality Gates

- Activation evidence names a concrete file, dependency, entry point, or shared
  import path.
- The affected consumer scope is identified: package root, app shell, shared UI,
  route-level chunk, or optional feature path.
- The phase output states what evidence will prove the bundle impact acceptable.

## Hard Stops

- Do not activate from generic performance language unless bundle, dependency, or
  import evidence exists.
- Do not treat development-only tooling changes as runtime bundle risk unless they
  affect shipped code.
- Do not ignore lockfile or package export changes when runtime imports changed.

## Phase Output

- Return matched bundle-risk evidence, affected consumers, measurement needs, and
  any static files that must be inspected.
