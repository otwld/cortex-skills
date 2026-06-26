
# Output Marker

Display:
using module: naming-consistency

---

# Naming Consistency

## Overview

Treat names as part of the interface and align them with project vocabulary and real
responsibilities.

## Reference Routing

- Use `shared/domain-glossary.md` when this task touches that concern.

## Workflow

1. Inspect the current repository context and existing project memory before changing behavior or guidance.
2. State the concrete responsibility, interface, artifact, or user-visible behavior this module governs.
3. Read project memory; prefer complete public names; use role suffixes only when true; rename vague shared/common/helper names.
4. Prefer durable artifacts, public seams, and validation evidence over local convenience.
5. Stop when the task needs a decision outside this module's scope and route to the appropriate governance module.

## Quality Gates

- Names describe domain role, lifecycle, and ownership without vague shared/common/helper language.
- Public names align with project glossary, existing suffixes, DTO contracts, and file naming conventions.
- Renames include affected exports, imports, docs, stories, fixtures, and generated references.

## Example

CandidateStageTransition is better than StatusChange when the transition is specific to
recruiting pipeline movement.

## Hard Stops

- Do not introduce generic names that force consumers to inspect implementation for meaning.
- Do not add role suffixes such as service, manager, helper, or util unless the role is real locally.
- Do not rename public symbols without updating consumers and documentation in the same change.

## Usage Checklist

- Project vocabulary and neighboring names were inspected.
- New or changed names encode role, owner, and stable meaning.
- Consumers, docs, examples, and generated references were updated or listed as unaffected.

## Cross References

- WITH: public-api-design, typescript-api-conventions, code-documentation
