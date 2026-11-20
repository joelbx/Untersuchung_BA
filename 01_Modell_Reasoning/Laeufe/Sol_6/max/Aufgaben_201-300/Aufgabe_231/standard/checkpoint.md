# Vuls2 schema version handling

Task: update `detector/vuls2/db.go` so connection errors identify the database path and schema mismatches trigger a download or an explicit error when updates are skipped.

Status: implemented schema validation in `newDBConnection` and `shouldDownload`; added local BoltDB regression cases for mismatch, skipped updates, missing metadata, and a usable returned connection.

Verification: `GOPROXY=off GOSUMDB=off go test ./detector/vuls2` passed. `git diff --check` passed.
