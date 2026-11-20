# Checkpoint

Task: fix vulnerability reporting for projects with multiple dependency lockfiles.

Implemented:
- Analyze every discovered lockfile separately through Fanal `AnalyzeFile`, using in-memory bytes and `DummyFileInfo`, retaining each path in `LibraryScanners`.
- Resolve libraries by both lockfile path and package name in model lookups and reports.
- Store the source path on each `LibraryFixedIn` and return an error for unknown lockfile driver types.
- Merge duplicate CVEs while preserving all library fix entries.
- Update the existing `Find` test for the path-aware signature and pin Fanal to the locally available version that provides `AnalyzeFile`.

Verification: `GOPROXY=off go test ./models ./scan ./libmanager ./report` passed. The build printed a SQLite C compiler warning; it did not affect the test results.
