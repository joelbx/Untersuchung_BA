Implemented the persisted-session retrieval updates across the public session provider, user hook, and telemetry.

The new helper uses `getPersistedSessions()`, selects the session with the highest `persistedAt`, and reports errors before returning `null` if retrieval fails. Public session initialization now uses the selected session’s `UID` and `localID`, and sets auth state and user data after a successful resume.

The focused Jest test passed, and `git diff --check` passed. The Drive TypeScript check did not finish within the available run, so typechecking remains unverified. No legacy helper or `LAST_ACTIVE_PING` references remain in the updated retrieval paths.