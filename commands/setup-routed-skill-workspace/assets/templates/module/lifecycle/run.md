# {{module_display_name}} Run

## Overview

Describe the implementation behavior this atom owns during execution.

## Workflow

1. Apply the atom's rules to the files or artifacts being changed.
2. Keep edits inside the responsibility selected during activation.
3. Record any validation or documentation work this atom requires.

## Quality Gates

- Implementation guidance is tied to the current artifact.
- Required validation or documentation is named before completion.

## Hard Stops

- Do not broaden this atom into unrelated implementation guidance.
- Do not add compatibility shims, relation language, or hidden resource coupling.

## Phase Output

- Return implementation requirements, changed surfaces, and validation needs for this atom.
