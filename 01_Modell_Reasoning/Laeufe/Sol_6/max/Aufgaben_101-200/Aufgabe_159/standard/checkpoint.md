Task: Fix package name parsing for CycloneDX PURLs in /app.

Findings: `parsePkgName` was absent. Library and dependency graph PURLs in `reporter/sbom/cyclonedx.go` passed package names directly with empty namespace and subpath. Their source labels also include aliases such as `pom`, `pip`, and `gomod`.

Changes made: added `parsePkgName`, mapped source labels to canonical PURL types at both construction paths, and added parser and PURL integration tests. Original component names and vulnerability lookup keys remain based on source package names.

Verification: `gofmt` and `git diff --check` pass. With network access disabled, `go test ./reporter/sbom` and `go test ./reporter/...` both pass.
