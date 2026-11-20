# Checkpoint

Task: fix package name parsing used when building CycloneDX PURLs.

Changes: added an unexported parser that returns namespace, name, and subpath for Maven, PyPI, Go, npm, and CocoaPods packages. It also handles the local manifest/library aliases (`pom`, `gradle`, `jar`, `pip`, `pipenv`, `poetry`, `uv`, `gomod`, `yarn`, and `pnpm`). Applied its results to the Trivy library and GitHub dependency PURL builders.

Verification: `go test ./reporter/sbom` passed (the package has no test files); `go test ./reporter/...` passed. `git diff --check` and `gofmt -d` reported no issues.
