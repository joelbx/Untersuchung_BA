Implemented path aware vulnerability reporting. Lockfiles are now analyzed individually, and each library finding carries its source path. TUI and util reports look up libraries by path and name, and repeated CVEs retain fixed version entries from each lockfile. Trivy parsed results also preserve their target path.

Added `DummyFileInfo` and an error returning driver initializer for unknown file types.

**Validation:** `GOPROXY=off go test ./scan ./models ./libmanager ./report ./contrib/trivy/parser` passed, and `git diff --check` passed. The build emitted a C compiler warning from `go-sqlite3`.