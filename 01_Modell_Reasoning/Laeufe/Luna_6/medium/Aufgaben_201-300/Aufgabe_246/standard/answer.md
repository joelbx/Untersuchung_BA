Implemented path tracking for library vulnerabilities. `LibraryFixedIn` now carries the lockfile path, reporting looks up libraries by both path and name, and scanning analyzes each lockfile separately so results retain their source path. Duplicate CVEs now keep fixed library entries from each file.

Added `DummyFileInfo` and updated the existing `Find` test for its path-aware signature. The pinned `fanal` version does not provide `AnalyzeFile`, so per-file analysis uses its available `GetLibraries(FileMap)` API.

Relevant tests passed: `go test ./models ./scan ./report ./libmanager`.