# Routed Workspace Operations

Use this reference for the operations supported by
`$setup-routed-skill-workspace`.

## Initialize Workspace

1. Require the target root and entry slug.
2. Create `routed-skills.yaml` with `entry.path: entry/<entry-slug>`.
3. Create the public entry skill from templates.
4. Add or update the checkout-root `.gitignore` with the entry runtime path:
   use `.<entry-slug>/` for repository-root routed workspaces and
   `<target-root>/.<entry-slug>/` for nested `skills/` or `.skills/` roots.
5. Create empty `modules/`, `shared/`, and `generated/` folders.
6. Copy rebuild, validate, and validator fixture-test scripts into `scripts/`.
7. Create `commands/setup-routed-skill-workspace/` from the current command
   package so the target workspace can author future atoms.
8. Create `commands/setup-<entry-slug>-config/`.
9. Copy generated placeholders, then rebuild generated artifacts.
10. Run validation.

Do not create starter routed modules unless the user explicitly asks for them.
Do not create `.<entry>/config.json`; the config command owns that operator
local file.
Do not create `skills/.gitignore` or `.skills/.gitignore` to satisfy runtime
ignore policy for nested layouts.

## Create Routed Module

1. Inspect existing module names, descriptions, facets, lifecycle files, and
   declared resources.
2. If overlap is material, report create, merge, narrow, split, or reject.
3. Choose the requested module path; prefer
   `modules/<area>/<cluster>/<module-name>/` when taxonomy is available.
4. Create `skill.yaml` with `status: draft`, empty facets, and all lifecycle
   phases declared.
5. Create lifecycle placeholders for activate, plan, run, review, verify, and
   finalize.
6. Rebuild generated artifacts.
7. Validate.

## Create Command Atom

1. Create `commands/<command-name>/`.
2. Add `SKILL.md`, `agents/openai.yaml`, and `skill.yaml`.
3. Use `activation: explicit`, `visibility: public`, and `status: active`.
4. Do not add lifecycle files.
5. Rebuild generated artifacts.
6. Validate.

## Rebuild Workspace

Run:

```bash
python3 scripts/rebuild-routed-skills.py routed-skills.yaml
```

## Validate Workspace

Run:

```bash
python3 scripts/rebuild-routed-skills.py --check routed-skills.yaml
python3 scripts/validate-routed-skills.py routed-skills.yaml
```

When validation or rebuild scripts change, also run:

```bash
python3 scripts/test-validate-routed-skills.py
```
