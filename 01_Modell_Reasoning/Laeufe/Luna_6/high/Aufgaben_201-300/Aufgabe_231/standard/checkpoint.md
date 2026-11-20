# Checkpoint

Resolved Vuls2 schema mismatch handling in `detector/vuls2/db.go`.

- `shouldDownload` reads metadata before honoring `SkipUpdate`; mismatched schemas produce a path-specific error when updates are skipped and force a download otherwise.
- `newDBConnection` includes the database path in connection errors and validates metadata presence and schema version before returning the connection.
- Added regression cases for both mismatch update modes in `detector/vuls2/db_test.go`.

Verification: `go test ./detector/vuls2` passed; `git diff --check` passed.
