# Checkpoint

Task: Add registration-token support to the interactive authentication flow in `/app`.

Discovery: `rg` is unavailable and no `AGENTS.md` guidance was found. The installed matrix-js-sdk declares both stable and unstable registration-token auth types. The interactive auth component already reports successful results with `clientSecret` and `emailSid` metadata.

Implemented: added `RegistrationTokenAuthEntry`, wired stable and unstable stage identifiers to it, and submits `{ type: loginType, token }` so the server-advertised type is preserved. The view has a labeled autofocus field, Enter/click submission, disabled empty action, spinner while busy/submitting, duplicate-submit guard, and accessible error alert.

Validation: Prettier, ESLint, and `git diff --check` pass. Existing interactive-auth and registration suites pass (2 suites, 5 tests). Full TypeScript check remains blocked by pre-existing Sliding Sync type mismatches in unrelated files; it reports no errors in the changed auth component.
