Fixed `parsePkgName` so it returns namespace, name, and subpath for Maven, PyPI, Golang, npm, and Cocoapods. Library and GitHub manifest PURLs now use those parsed values, with scanner labels such as `pom`, `pip`, and `gomod` mapped to PURL ecosystem types.

Added [SBOM tests](/app/reporter/sbom/cyclonedx_test.go). `go test ./reporter/...` and `git diff --check` pass.