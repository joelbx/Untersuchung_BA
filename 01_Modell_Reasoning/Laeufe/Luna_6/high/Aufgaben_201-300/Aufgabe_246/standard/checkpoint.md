# Checkpoint

Task: Resolve missing lockfile paths in vulnerability reports.

Implemented:
- Lockfiles are analyzed individually with `AnalyzeFile` and in-memory content using `DummyFileInfo`; `convertLibWithScanner` converts each analysis result, and records are appended per file.
- `LibraryScanners.Find` filters by both path and library name; TUI and utility reports pass both values.
- Fixed-version records carry the source path, and repeated CVEs retain all associated library fixed-version entries.
- Library driver initialization propagates unknown file type errors.
- Updated cached `fanal` and Trivy versions to expose the required per-file analysis and error-returning driver APIs.

Verification: `GOSUMDB=off GOPROXY=off go test -mod=mod ./...` passed. `git diff --check` passed.
