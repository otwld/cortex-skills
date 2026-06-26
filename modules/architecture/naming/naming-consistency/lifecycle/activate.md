# Naming Consistency Activate

## Overview

Activate when the task creates or renames files, symbols, DTOs, contracts,
events, commands, providers, factories, public exports, or reusable
abstractions.

## Workflow

1. Read `shared/domain-glossary.md` when names include domain terms or the task
   asks for vocabulary alignment.
2. Inspect neighboring names in the same owner, package, feature, or domain.
3. Inspect public exports, docs, tests, stories, fixtures, generated references,
   and import paths that mention the name.
4. Check whether suffixes such as service, manager, helper, util, provider,
   factory, DTO, command, or event describe a real local role.
5. Treat purely mechanical local variable changes as out of scope unless they
   affect meaning or public readability.

## Quality Gates

- Activation evidence names the surface, current and proposed terms, glossary
  evidence, affected consumers, and unresolved vocabulary decisions.
- Public or reusable names are compared to neighboring vocabulary.
- Role suffixes are justified by local responsibility.

## Hard Stops

- Do not introduce vague names that force readers to inspect implementation.
- Do not add role suffixes that are conventional but false for the code's actual
  responsibility.
- Do not rename public symbols without planning consumer and documentation
  updates.

## Phase Output

- State the naming surface, current and proposed terms, glossary evidence,
  affected consumers, and unresolved vocabulary decisions.
