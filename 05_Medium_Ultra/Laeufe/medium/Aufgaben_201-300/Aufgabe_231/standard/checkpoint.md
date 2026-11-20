# Vuls2 schema version handling

Updated `shouldDownload` to inspect metadata before honoring `SkipUpdate`, force a download for incompatible schemas, and report mismatches when updates are disabled. Updated `newDBConnection` to open the database, read metadata, validate its schema, and include the path in connection and metadata errors.

Added mismatch cases to the existing Vuls2 download test. `GOPROXY=off GOSUMDB=off go test ./detector/vuls2` passes; `git diff --check` passes.
