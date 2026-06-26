# TypeScript API Conventions Activate

## Overview

Use this phase to decide whether the task changes an exported TypeScript
contract. The trigger is a public type surface or consumer-facing declaration,
not the mere presence of a `.ts` file.

## Workflow

1. Inspect the request, diff, and touched paths for `export`, `export type`,
   `interface`, `type`, `class`, exported functions, declaration files, barrel
   files, package entry points, DTOs, schemas, or SDK-facing contracts.
2. Name the exported symbol or contract family at issue. If no exported surface
   is involved, say so and keep this phase inactive for the task.
3. Check the consumer side: imports of the export, generated declarations,
   public docs, compile-time examples, tests, and package export maps.
4. Identify the API risk category: state modeling, generic constraint,
   nullability, mutability, type-only boundary, runtime export boundary, or
   migration compatibility.
5. Decide which validation can prove the contract: project typecheck, API
   extraction, contract tests, declaration generation, or consumer compile
   tests.

## Quality Gates

- Activation names concrete exported symbols, files, or entry points.
- The phase distinguishes public contract design from private implementation
  style.
- The activation note states which consumer evidence was inspected or why none
  exists.
- Validation expectations are tied to the changed contract, not to a generic
  TypeScript checklist.

## Hard Stops

- Do not activate only because a TypeScript implementation file was edited.
- Do not treat a private helper type as public unless it is exported or appears
  in a public signature.
- Do not infer compatibility from local compilation alone when known consumers
  or declaration output exist.
- Do not expand ownership to HTTP, UI, or documentation policy except where the
  TypeScript contract itself is changed.

## Phase Output

Return the activation decision, the exact exported surfaces inspected, consumer
evidence found, API risks to control, and the validation commands or artifacts
required for the later phase.
