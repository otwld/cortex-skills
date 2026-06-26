# Naming Consistency Review

## Overview

Review naming changes for stable meaning, glossary alignment, complete consumer
updates, and absence of stale public names.

## Workflow

1. Inspect diffs for renamed files, exports, imports, DTO fields, events,
   commands, providers, factories, tests, docs, stories, fixtures, and generated
   references.
2. Search for old names and near-duplicate vocabulary.
3. Inspect glossary or project memory updates when a domain term changed.

## Quality Gates

- Names encode stable meaning without implementation spelunking.
- Public vocabulary aligns with the glossary and neighboring owners.
- Consumers, docs, tests, fixtures, and generated references are updated or
  explicitly unaffected.
- Old public names are absent unless a named compatibility contract keeps them.

## Hard Stops

- Reject generic names that hide domain role, lifecycle, ownership, or artifact
  kind.
- Reject suffixes that imply a false pattern or broad responsibility.
- Reject public renames that leave old imports, docs, examples, fixtures,
  generated references, or tests behind.
- Reject two names for the same domain concept or one name for two different
  concepts.

## Phase Output

- Return naming findings with affected symbols, vocabulary conflicts, stale
  references, required renames, and validation evidence.
