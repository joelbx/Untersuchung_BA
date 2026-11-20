# Checkpoint

Task: resolve unreliable retrieval of the last persisted session on public pages.

Implemented:
- Added `getLastActivePersistedUserSession` in the Drive app and mirrored Docs store. It uses shared persisted-session storage, selects the greatest `persistedAt`, and returns the complete session including UID and localID.
- Added shared storage parse-error callbacks. Malformed session JSON is now reported and causes the lookup to return `null`; storage access failures are also reported and return `null`.
- Updated Drive and Docs public-session SRP and resume flows, telemetry UID headers, and Drive's public user hook.
- Removed the old selectors and `LAST_ACTIVE_PING` identifier/key. The separate active API ping throttle uses its own storage prefix.
- Updated existing helper and active-ping tests.

Verification:
- Drive focused tests: 2 suites, 11 tests passed.
- Docs-store focused tests: 2 suites, 11 tests passed.
- Prettier check and `git diff --check` passed.
- Drive and Docs-store type checks each report only the existing OpenPGP type incompatibility in `packages/crypto/lib/worker/api.ts:579`.
- ESLint invocation ran out of Node heap before returning results.
