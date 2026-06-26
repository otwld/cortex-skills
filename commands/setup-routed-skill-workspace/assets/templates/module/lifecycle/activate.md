# {{module_name}} Activate

## Overview

{{module_purpose}}

## Workflow

1. Match this atom only when its structured facets have direct request or repository evidence.
2. Load declared resources only when this phase needs them.
3. Return activation evidence and constraints for later phases.

## Quality Gates

- Facet evidence is explicit and local to this atom.
- This atom does not name peer modules or route other atoms.

## Hard Stops

- Do not add peer-module dependencies or relation language.
- Do not use this phase file as a generic module overview.

## Phase Output

- Return matched evidence, required local resources, and phase constraints for this atom.
