# Changelog

All notable changes to this project will be documented here.

## Unreleased

### Fixed

- Read `LINEAR_AGENT_*` settings through Hermes' profile secret scope. A multiplexed gateway keeps a secondary profile's `.env` out of `os.environ`, so that profile never saw its webhook secret and rejected every delivery with `Webhook secret not configured`.
- Acknowledge (200 ignored) `created`/`prompted` deliveries from other webhook categories, such as `OAuthAuthorization` when a user authorizes the app, instead of failing with 400 `Missing agentSession.id`.
- Attribute Agent Session webhooks to `agentSession.creator` (and a prompt's activity author). Linear sends no top-level `actor`, so the sender fell back to the app's own user and the gateway rejected every session as `Unauthorized user`; a user-ID allowlist could never match.

### Changed

- OAuth scopes are fixed to `read,write,app:assignable,app:mentionable,customer:read,customer:write,initiative:read,initiative:write`. `LINEAR_AGENT_OAUTH_SCOPES`, the `oauth_scopes` config key and the helper's `--scope` flag are removed, and the helper deletes a leftover `LINEAR_AGENT_OAUTH_SCOPES` from `.env`. The gateway previously fell back to `read,write`, and Linear revokes all app tokens and replaces the installed scopes when a token is requested with a different set, which stripped the agent's assign/mention scopes. A cached token with other scopes is now discarded and minted again.

## 0.4.2 — 2026-07-29

### Fixed

- Resolve a child `AgentSession.sourceCommentId` to its root comment before replying; Linear rejects child comments as `commentCreate.parentId` with `incorrect parent`.
- Mirror final Agent Session responses to the resolved source thread in adapter-controlled delivery instead of relying on the model to invoke a comment tool.

## 0.4.1 — 2026-07-29

### Fixed

- Preserve Linear's current `agentSession.sourceCommentId` webhook field so replies triggered from an existing issue-comment thread can be routed back to that original thread.
- Accept `agentActivity.sourceCommentId` as a compatible fallback for prompted activity payloads.

## 0.4.0 — 2026-07-29

### Added

- Standalone Hermes platform-plugin distribution for Linear Agent Sessions.
- Git-directory plugin manifest and pip entry point.
- 58 attributed `linear_agent_*` tools with fail-closed mutation policies.
- Linear client-credentials and authorization-code OAuth support.
- Signed webhook handling, replay protection, Agent Activities, plans, session links, clarification, stop signals, and standalone cron delivery.
- Plugin-owned, process-locked, atomic OAuth state storage with POSIX mode `0600`.
- Read-only migration fallback for earlier `providers.linear_agent` state in Hermes `auth.json`.
- Compatibility tests for current Hermes upstream and Python 3.11–3.13.
