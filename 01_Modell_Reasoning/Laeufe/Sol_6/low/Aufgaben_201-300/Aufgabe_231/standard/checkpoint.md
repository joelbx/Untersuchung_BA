Task: Handle Vuls2 database schema mismatches in detector/vuls2/db.go.
Status: Complete. Added connection and metadata validation with path-aware errors; shouldDownload checks schema before SkipUpdate and freshness checks. Added mismatch regression cases. go test ./detector/vuls2 passed; git diff --check passed.
