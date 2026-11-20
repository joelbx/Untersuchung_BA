# Checkpoint

Implemented explicit Vuls2 database metadata validation in `detector/vuls2/db.go`.

- `newDBConnection` now includes the database path in connection/open/metadata errors, rejects nil metadata, and reports schema mismatches after downloading or when reusing a database.
- `shouldDownload` checks metadata before honoring `SkipUpdate`; it returns an error for a schema mismatch when updates are skipped and forces a download otherwise.
- Existing matching-schema skip-update and nil-metadata path errors are preserved.

Verification: `go test ./detector/vuls2` passed.
