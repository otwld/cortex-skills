# Vite Conventions Run

## Overview

Implement Vite changes so dev behavior, production output, and published package
contracts stay explicit and verifiable.

## Workflow

- Keep config mode-aware. Use the existing `defineConfig` style, env loading,
  and project script conventions instead of introducing a second config pattern.
- Keep aliases consistent with TypeScript paths and package exports. Internal
  source aliases are acceptable only for build-time implementation code, not for
  published consumer contracts.
- For library builds, define entry points, formats, file names, source maps, and
  external dependencies from the package's public API. Framework peers should
  stay external unless the package intentionally owns that runtime.
- Preserve local bundler option names for the installed Vite version. Do not mix
  old and new option names in the same config without a compatibility reason.
- Order plugins by observable transform dependency: framework/compiler plugins,
  path or asset transforms, analysis or inspection plugins, then reporting
  plugins. Add a short comment only when the ordering is non-obvious.
- Keep `define`, `envDir`, and env prefix changes narrow. Do not expose server
  secrets to browser code or replace runtime values that consumers are expected
  to provide.
- Validate dev-server changes in the mode they affect: proxy target, allowed
  host, HMR websocket behavior, file watching, middleware mode, or preview
  output.
- Treat websocket proxy origin rewriting as security-sensitive. Name the local
  need, target origin, and CSRF exposure before enabling origin rewrites.
- When adding invented examples, use recruitment job board fixtures such as
  candidates, job offers, applications, recruiters, and interviews.

## Quality Gates

- Run the narrowest build, dev, preview, Storybook, or static output inspection
  that exercises the changed Vite behavior.
- For library output, inspect generated formats, externals, source maps, and
  package entry points when a full consumer test is not available.
- When validation cannot run, provide static evidence: installed Vite version,
  affected mode, package exports, peer dependency decision, plugin order, and
  expected output path.

## Hard Stops

- Do not add aliases that let package consumers import private source files.
- Do not bundle peer dependencies into a library without naming the consumer and
  duplication impact.
- Do not change plugin order, env replacement, source-map generation, or
  dev-server networking without targeted validation.
- Do not enable websocket origin rewriting for convenience or to bypass a local
  integration failure without naming the security impact.
- Do not copy options from another Vite major version without confirming support
  in the installed project.

## Phase Output

Return changed Vite files, affected mode, alias and externalization choices,
plugin-order or server behavior decisions, validation command or static proof,
and any remaining build-output risk.
