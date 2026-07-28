# Contributor Notes

## Scope
This repository is the standalone Hermes plugin for Linear Agent Sessions. It must remain installable without modifying the Hermes core repository.

## Rules
- Register platforms and tools only through the public `PluginContext` API.
- Do not import underscore-prefixed Hermes APIs.
- Keep credentials profile-scoped, redacted, and stored only in plugin-owned state.
- Keep product-specific behavior here; propose only generic reusable API gaps upstream.
- Run the full test suite, Ruff, package build, and both plugin installation contract tests before release.
