# Checkpoint

Resolved: lockfile findings retain their source path, reports resolve versions by `(path, name)`, and repeated CVEs accumulate library findings. Each lockfile is analyzed separately and appended to `LibraryScanners`; `DummyFileInfo` supplies in-memory file metadata. Findings without a fixed version also retain the source path.

The pinned offline dependencies expose `analyzer.GetLibraries` rather than `analyzer.AnalyzeFile`, and Trivy `DriverFactory.NewDriver` returns a nullable driver rather than `(driver, error)`. Local adapters provide one-file analysis and error-returning driver initialization without changing dependencies.

Test-first evidence:
- `GOPROXY=off go test ./models -run TestLibraryScanners_Find -count=1`: failed on missing path argument.
- `GOPROXY=off go test ./libmanager -run TestAddLibraryVulnPreservesBothLockfiles -count=1`: failed on missing merge helper.
- `GOPROXY=off go test ./scan -run TestAnalyzeFileSeparatesSameLibraryAcrossLockfiles -count=1`: failed on missing AnalyzeFile and DummyFileInfo after fixing test fixture type.
- `GOPROXY=off go test ./models -run TestLibraryFindingWithoutFixedVersionKeepsPath -count=1`: failed on missing finding construction.

Verification: `GOPROXY=off go test ./...` passed all packages. `git diff --check` passed. The Go build prints an upstream `go-sqlite3` C compiler warning (`sqlite3-binding.c:125322:10: warning: function may return address of local variable`); it does not fail tests.
