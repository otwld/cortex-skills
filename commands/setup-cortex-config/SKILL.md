---
name: setup-cortex-config
description: Use when Cortex needs to create or repair the operator-local .cortex/config.json phase configuration.
---

# Setup Cortex Config

## Overview

Create or repair the operator-local `.cortex/config.json` file used by `$cortex`
before lifecycle routing begins.

## Workflow

1. Inspect whether `.cortex/config.json` exists.
2. If it is missing, create `.cortex/config.json` with all lifecycle phases and empty `always` lists.
3. If it exists, preserve valid configured modules and repair only invalid or missing phase keys when explicitly asked.
4. Keep the config operator-local; do not move it into tracked workspace source.

## Default Config

```json
{
  "phases": {
    "activate": { "always": [] },
    "plan": { "always": [] },
    "run": { "always": [] },
    "review": { "always": [] },
    "verify": { "always": [] },
    "finalize": { "always": [] }
  }
}
```

## Quality Gates

- The config includes every manifest lifecycle phase.
- Each `always` value is a list of module names.
- Existing operator choices are not discarded during repair.

## Hard Stops

- Do not add project-specific modules to the default scaffold.
- Do not commit `.cortex/config.json`; `.cortex/` remains operator-local.
- Do not change routed module metadata from this command.

## Completion Checklist

- Existing config state was inspected.
- Missing phase keys were scaffolded or repaired.
- The resulting JSON shape is valid for `$cortex` bootstrap.
