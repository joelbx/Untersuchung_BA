# Checkpoint

Task: simplify SQLite persistence to use one unified `*sql.DB` connection, removing the read/write database abstraction and routing complexity as requested by the issue title and expected behavior.

Initial state: repository inspection started in `/app`. The issue text also contains a contradictory later interface request for read/write separation; that conflicts with the main expected behavior and will be resolved in favor of the unified connection unless repository-local behavior provides stronger evidence.

Implementation completed:

- Added all required SQLite DSN settings while preserving existing URI query options.
- Kept persistence bound to the injected `*sql.DB`, removed fallback to the global connection, and kept nested transaction work on the active transaction.
- Updated transaction callbacks in play tracking and initial setup to use their `tx` datastore.

Verification: `go test ./db ./persistence ./core/scrobbler ./server ./server/nativeapi ./server/subsonic` passed. `git diff --check` passed, and transaction callbacks were reviewed for direct datastore access.
