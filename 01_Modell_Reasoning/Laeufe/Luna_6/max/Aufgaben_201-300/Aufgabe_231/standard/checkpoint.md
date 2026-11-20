# Checkpoint

Task: Resolve Vuls2 database schema-version mismatch handling in `detector/vuls2/db.go`.

Completed:
- `shouldDownload` reads metadata before honoring `SkipUpdate`, returns a path-bearing mismatch error when updates are skipped, and forces a download when updates are allowed.
- `newDBConnection` includes the database path in connection/open/metadata errors and validates non-nil metadata plus the expected schema version.
- Added mismatch and skip-update mismatch cases to the existing `shouldDownload` table test.

Verification: `go test ./detector/vuls2` passed; `git diff --check` passed.
