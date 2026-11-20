# Checkpoint

Task: simplify SQLite database access to one `*sql.DB` throughout the repository.

The issue text contains conflicting legacy requirements for a read/write split. I am following the title, problem statement, and unified-connection requirements while checking repository code and tests.

Status: implemented and verified. The existing checkout already passed one `*sql.DB` to persistence and migrations. SQLite now builds a DSN with the required options; persistence no longer falls back to the global database; transaction callbacks in scrobbling and initial setup use the transaction store. Added DSN and isolated-connection tests.

Verification: `go test ./db ./persistence ./core/scrobbler ./server` and `git diff --check` passed after final edits. Final diff review complete.
