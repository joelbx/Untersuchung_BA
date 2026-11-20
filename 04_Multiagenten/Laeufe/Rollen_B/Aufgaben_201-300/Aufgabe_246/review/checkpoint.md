VERDICT: FIX

CODE_DEFECTS
- scan/base.go:580-586 and scan/library.go:12-18 analyze each lockfile via GetLibraries(FileMap{path: content}); the required AnalyzeFile in-memory path is absent. DummyFileInfo at scan/base.go:42-49 is never used, and convertLibWithScanner still accepts GetLibraries applications rather than per-file AnalyzeFile results. Implement the required per-file analyzer API and adapt conversion.
- scan/base.go:536-538,582-586 now appends results before all lockfiles succeed. If a later file fails, retrying on the same base skips analysis because LibraryScanners is nonempty, leaving a partial scan. Accumulate locally and assign only after all files succeed, or otherwise clear partial state on error.

TEST_ENVIRONMENT_PROBLEM
- None. Existing relevant tests executed offline with command: GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./models ./scan ./libmanager ./report ./contrib/trivy/parser. Result: exit 0; all five packages passed. The C sqlite3 compiler emitted a warning, but compilation and tests succeeded.
- git diff --check: exit 0.

Review only; no project code changed.
