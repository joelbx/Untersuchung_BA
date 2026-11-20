Implemented per-lockfile vulnerability reporting. Findings now retain their lockfile path, and report lookups match both path and library name. Lockfiles are analyzed individually in memory, and duplicate CVEs preserve fixed-version entries from each file.

Verification passed: `GOSUMDB=off GOPROXY=off go test -mod=mod ./...` and `git diff --check`.