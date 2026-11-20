Implemented the persisted-session fix.

- Added [getLastActivePersistedUserSession.ts](/app/applications/drive/src/app/utils/lastActivePersistedUserSession.ts), selecting the newest valid session through shared storage and reporting malformed data or storage errors.
- Updated public session resume, auth state, SRP headers, the public user hook, and telemetry to use the full session or current auth state.
- Removed the old helper APIs and `LAST_ACTIVE_PING` references. The active ping key prefix was renamed.
- Added an optional parse-error callback in [persistedSessionStorage.ts](/app/packages/shared/lib/authentication/persistedSessionStorage.ts); existing callers retain their behavior.

**Verification:** Three focused Jest suites passed (17 tests); the helper suite passed again after its final assertion. ESLint found no errors and one existing React hook dependency warning. `git diff --check` passed. TypeScript checking remains blocked by an unrelated OpenPGP type error in [api.ts](/app/packages/crypto/lib/worker/api.ts).