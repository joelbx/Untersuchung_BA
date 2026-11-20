Task: Handle Vuls2 schema mismatches in detector/vuls2/db.go.
Status: Complete. newDBConnection opens and validates metadata/schema with path-specific errors; shouldDownload checks schema before SkipUpdate and freshness, forcing download or returning mismatch error. Added mismatch cases to existing tests.
Verification: go test ./detector/vuls2 passed; git diff --check passed.
Delegation: None.
