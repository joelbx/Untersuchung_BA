# Checkpoint
Implemented complete persisted-session selection via getPersistedSessions and updated public session, user, and telemetry callers. Removed LAST_ACTIVE_PING identifier and old helpers. Relevant tests: 2 suites, 11 tests passed. Type check fails in pre-existing packages/crypto/lib/worker/api.ts OpenPGP type mismatch, outside edited files. git diff --check passed.
