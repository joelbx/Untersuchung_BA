# Checkpoint

Task: simplify SQLite access to a single unified `*sql.DB` connection and remove the read/write database abstraction, resolving conflicting issue text in favor of the title and expected behavior.

Changes made:
- Applied the required SQLite connection options to the default DSN, in-memory DSNs, and configured database paths.
- Kept `persistence.New` on the supplied `*sql.DB`; the store now retains it and uses it to start transactions instead of falling back to the package-global database.
- Changed database operations inside initial setup and scrobble play-count transaction callbacks to use the callback transaction datastore.

Validation: `go test ./db ./persistence ./core/scrobbler ./server ./server/nativeapi ./server/subsonic` passed; `git diff --check` passed.
