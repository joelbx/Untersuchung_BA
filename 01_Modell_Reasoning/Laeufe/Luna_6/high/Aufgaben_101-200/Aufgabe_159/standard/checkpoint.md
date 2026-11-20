# Checkpoint

Task: fix `parsePkgName` ecosystem parsing in `/app` and run relevant existing tests.

Implemented `parsePkgName(t, n)` in `reporter/sbom/cyclonedx.go` and wired its namespace, name, and subpath into library PURL construction. It covers Maven, PyPI, Golang, scoped npm, and CocoaPods while returning empty values for non-applicable components.

Validation: `gofmt` completed; `git diff --check` passed; `go test ./reporter/sbom ./reporter` passed (`reporter/sbom` has no test files; `reporter` tests passed).
