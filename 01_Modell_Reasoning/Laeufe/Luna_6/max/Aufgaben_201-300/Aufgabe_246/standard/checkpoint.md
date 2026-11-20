# Checkpoint

Task: resolve missing lockfile paths in vulnerability reports, including per-file lockfile analysis, path-aware library lookup, and duplicate CVE merge behavior.

Implemented:
- Added `DummyFileInfo` and an in-memory, one-lockfile `AnalyzeFile` adapter for this repository's Fanal API; `scanLibraries` now analyzes each lockfile separately and appends its converted scanners.
- Made library lookup require path and name, preserved path in `LibraryFixedIn` (including parsed Trivy results), updated TUI/util lookups, and merged fixed-in entries for repeated CVEs.
- Added an error-returning library-driver initializer for unknown file types.
- Updated existing model and Trivy parser fixtures for path-aware behavior.

Validation: `GOPROXY=off go test ./scan ./models ./libmanager ./report ./contrib/trivy/parser` passes. `git diff --check` passes. The Go build emitted an existing C warning from `go-sqlite3`; tests passed.
