Implemented per lockfile library analysis and path-aware vulnerability reporting.

- [scan/base.go](/app/scan/base.go) analyzes each lockfile’s in-memory content separately and keeps its path.
- [models/library.go](/app/models/library.go) stores the source path on findings, filters lookups by path and name, and reports unknown lockfile types as errors.
- [libmanager/libManager.go](/app/libmanager/libManager.go) preserves library fix entries when CVEs repeat.
- Updated TUI/util lookups and the existing path-aware lookup test.

Verification passed: `GOPROXY=off go test ./models ./scan ./libmanager ./report`. The build emitted a SQLite C compiler warning, but all tests passed.