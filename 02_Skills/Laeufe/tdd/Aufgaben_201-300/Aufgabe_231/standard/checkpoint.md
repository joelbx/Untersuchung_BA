# Checkpoint

Task: handle Vuls2 database schema mismatches explicitly.

Implemented in detector/vuls2/db.go: validate metadata and schema when constructing a connection; inspect schema before honoring SkipUpdate, forcing download or returning a mismatch error. Connection and metadata errors include the database path.

TDD: added regression tests for mismatched schema, missing metadata, and invalid database path. Saw them fail before changing production code.

Verification passed:
- `GOTOOLCHAIN=local GOPROXY=off go test ./detector/vuls2 -run 'Test_shouldDownload|Test_newDBConnection' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off go test ./detector/vuls2 -count=1`
- `GOTOOLCHAIN=local GOPROXY=off go test ./...`
- `git diff --check`
