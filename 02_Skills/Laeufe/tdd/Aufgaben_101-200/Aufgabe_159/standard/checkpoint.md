# Checkpoint

- Task: fix package name parsing for PURLs in the SBOM reporter.
- Assigned workflow: test-driven development; inspect current code, add a failing regression test, then implement and run relevant and full tests.
- Initial search: `parsePkgName` is absent from checked-out Go files; locating its call site and existing PURL construction.
- Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`), so using local `grep` and `find`.
- Regression test `TestLibraryPackagePURLNameParts` failed as expected for Maven, Go, npm, Cocoapods, and the real scanner aliases `pom`, `pip`, `gomod`; `TestGitHubPackagePURLNameParts` failed for scoped npm. Exact command: `GOTOOLCHAIN=local GOPROXY=off go test ./reporter/sbom -run 'TestLibraryPackagePURLNameParts|TestGitHubPackagePURLNameParts' -count=1`.
- Added `parsePkgName` and used it in library and GitHub dependency PURL construction. `GOTOOLCHAIN=local GOPROXY=off go test ./reporter/sbom -count=1` passed.
- Full repository test command passed: `GOTOOLCHAIN=local GOPROXY=off go test ./...` (all packages green).
- `git diff --check` passed.
