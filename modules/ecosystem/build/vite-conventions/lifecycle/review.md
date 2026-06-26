# Vite Conventions Review

## Overview

Find regressions in Vite config loading, plugin behavior, dev-server behavior,
and published build output.

## Workflow

- Compare changed Vite config against package scripts, installed Vite version,
  framework plugins, TypeScript paths, package exports, and peer dependencies.
- Verify aliases do not bypass public entry points or create a second import
  contract that only works in Vite.
- Check library builds for explicit entries, output formats, file names,
  externals, source maps, and generated package artifacts.
- Review plugin order for transform dependencies and mode differences between
  dev, build, preview, tests, and Storybook.
- Inspect env and define changes for accidental browser exposure of server-only
  values or replacement of consumer-supplied runtime values.
- Check dev server, HMR, host, proxy, watch, and preview changes against the
  environment they are meant to support.
- Inspect websocket proxy origin rewriting as a security decision, not only a
  connectivity fix.

## Quality Gates

- Findings name the affected mode and the concrete config option, plugin,
  package entry point, dependency, or output file that can regress.
- Review distinguishes app bundling, library publishing, test reuse, and
  Storybook builder effects.
- Missing validation is actionable: name the build, dev-server observation,
  preview check, source-map inspection, or static output proof needed.

## Finding Triggers

- A library build includes a framework peer or dependency already expected from
  the consuming app.
- A Vite alias points at private source in a way exported consumers can copy.
- Plugin reordering changes transform ownership without a test or build result.
- Source maps, env replacement, proxying, or HMR settings changed without an
  observation in the affected mode.
- Websocket origin rewriting is enabled without naming the target origin and
  cross-site request risk.
- Config uses options unsupported by the installed Vite major version.

## Hard Stops

- Do not approve published-library output when public entries, externals, and
  generated files are unknown.
- Do not accept browser-exposed env values without proof they are safe to ship.
- Do not treat a successful production build as validation for dev-server proxy,
  HMR, or preview behavior.

## Phase Output

Return findings ordered by severity, each tied to a file and line, plus the
specific Vite mode, config option, output artifact, dependency decision, or
validation evidence needed to close it.
