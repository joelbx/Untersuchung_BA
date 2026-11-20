Implemented path-aware library vulnerability reporting. Each finding now carries its lockfile path, and TUI and util reports use both path and package name to look up the matching library. `FillLibrary` also appends fixed library details when the same CVE appears across files.

Lockfiles are analyzed one at a time and their results appended separately. I added `DummyFileInfo`, but the repository’s pinned `fanal` version does not provide `AnalyzeFile`, and its Trivy version’s `NewDriver` returns a nil driver rather than an error. The implementation uses the available per-file `GetLibraries` API and preserves the unknown-driver error check.

Relevant tests passed: `go test ./models ./scan ./report ./libmanager`.