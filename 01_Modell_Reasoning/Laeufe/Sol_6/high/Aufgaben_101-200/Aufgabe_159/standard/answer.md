Fixed CycloneDX PURL name parsing in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go:311). `parsePkgName` now returns namespace, name, and subpath for Maven, PyPI, Golang, npm, and Cocoapods, and library and GitHub dependency PURLs use those values.

Added [regression cases](/app/reporter/sbom/cyclonedx_test.go:5). `go test ./reporter/...` and `git diff --check` passed.