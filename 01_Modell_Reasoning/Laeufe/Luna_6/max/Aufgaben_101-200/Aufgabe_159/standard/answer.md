Implemented `parsePkgName` for Maven, PyPI, Go, npm, and CocoaPods names, including aliases used by local manifests. Both library and GitHub dependency PURLs now use its namespace, name, and subpath results.

Verification passed: `go test ./reporter/...`. The `reporter/sbom` package has no test files. Formatting and `git diff --check` were clean.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)