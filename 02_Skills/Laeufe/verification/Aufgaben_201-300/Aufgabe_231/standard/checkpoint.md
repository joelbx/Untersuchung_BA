# Checkpoint

Issue: validate Vuls2 database schema versions in connection and download decisions.

Initial inspection: `newDBConnection` does not open or read metadata after constructing a connection. `shouldDownload` returns early for `SkipUpdate` before reading metadata. `rg` is unavailable (`/bin/bash: rg: command not found`); use grep/find locally.

Pending: inspect DB API and tests, implement checks, run relevant tests.

Implemented schema validation after opening the selected database in `newDBConnection`, with path-bearing errors. `shouldDownload` now reads metadata before honoring `SkipUpdate`, errors for a mismatch when updates are disabled, and forces download otherwise. Added mismatch regression cases.

Verification so far: `GOPROXY=off GOSUMDB=off go test ./detector/vuls2 -run '^Test_shouldDownload$' -count=1` exited 0. `git diff --check` exited 0.

Final verification: `GOPROXY=off GOSUMDB=off go test ./detector/vuls2 -count=1` exited 0 (`ok ... 0.315s`). `git diff --check` exited 0. The package tests include mismatch forcing download, mismatch with SkipUpdate reporting an error and path, matching schema with SkipUpdate returning false, and missing metadata reporting an error and path.

Requirement review: `newDBConnection` reports path for connection construction/open, metadata retrieval, and nil metadata errors, and checks expected schema after opening the selected database. `shouldDownload` checks schema before SkipUpdate and freshness, returning an error for SkipUpdate and true otherwise on mismatch; nil metadata still reports path.
