# Checkpoint

Issue: vulnerability reports must identify each affected library's lockfile path.

Changes:
- Analyze each lockfile separately from in-memory content using `AnalyzeFile` and `DummyFileInfo`; append per-file scanners.
- Use `(path, name)` for library lookup and reporting; carry `Path` in `LibraryFixedIn`, including Trivy imports.
- Preserve fixed-library entries when a CVE occurs more than once.
- Update locally cached Fanal, Trivy, and Trivy DB dependencies for the required `AnalyzeFile` and error-returning driver APIs.
- Add multi-lockfile and unknown-file tests; update parser expectations.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod -count=1 ./...` exited 0. The C compiler emitted a warning in the existing go-sqlite3 dependency. `git diff --check` exited 0. No downloads were requested.
