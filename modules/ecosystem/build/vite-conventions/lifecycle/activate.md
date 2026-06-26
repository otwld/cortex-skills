# Vite Conventions Activate

## Overview

Decide whether Vite conventions apply and capture the config, package, and mode
evidence needed before changing dev or build behavior.

## Workflow

1. Match the request or diff to Vite config, plugins, aliases, library build
   settings, dependency optimization, source maps, env handling, or dev-server
   behavior.
2. Inspect the installed Vite and plugin versions, local config file, package
   scripts, public entry points, peer dependencies, and TypeScript path aliases.
3. Identify whether the change affects app build, library build, dev server,
   preview server, tests that reuse Vite config, or Storybook builder behavior.
4. Decide which mode must be validated and whether the option is version
   sensitive in the installed Vite release.
5. Record the expected output, transformed import path, plugin order, or server
   behavior that will prove the change correct.

## Trigger Evidence

Activate for changes to `vite.config.*`, Vite plugins, aliases, env and define
values, `publicDir`, dependency optimization, build output, source maps, library
mode, preview, dev server, HMR, proxying, or package metadata that changes how
Vite bundles a project.

Do not activate for unrelated TypeScript or package metadata changes unless a
Vite config, build, dev-server, or published-output behavior changes.

## Decisions

- Classify the config as app, library, shared test, Storybook builder, or mixed
  use before editing options.
- Use local Vite version and existing config style when choosing bundler option
  names and plugin APIs.
- Align aliases with package public entry points and TypeScript paths. Avoid
  aliases that let consumers depend on private source structure.
- Externalize framework and peer dependencies for published libraries unless the
  package intentionally ships them.
- Treat plugin order, source maps, proxy/HMR settings, and env replacements as
  mode-specific behavior that needs targeted validation.

## Quality Gates

- Activation names the affected mode, config file, package entry point, and
  dependency mode.
- The phase identifies whether aliases, externals, plugin order, source maps, or
  server settings are behavior-critical.
- Validation is stated as a build, dev-server, preview, source-map, or static
  output inspection.

## Hard Stops

- Installed Vite version or local config style is unknown and the change relies
  on version-sensitive options.
- A library build changes bundled dependencies without checking
  `peerDependencies`, package exports, and consumer entry points.
- A dev-server proxy, HMR, host, or source-map change lacks a way to observe the
  affected mode.

## Phase Output

Return matched Vite evidence, affected mode, config and package files, alias or
externalization decision, plugin-order risk, and required validation evidence.
