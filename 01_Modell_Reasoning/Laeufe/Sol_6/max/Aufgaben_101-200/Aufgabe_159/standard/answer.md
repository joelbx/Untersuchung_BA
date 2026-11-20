Fixed CycloneDX PURL generation in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go:247). `parsePkgName` now returns namespace, name, and subpath for Maven, PyPI, Golang, npm, and Cocoapods, and both library and dependency graph PURLs use those values.

Added [parser and PURL tests](/app/reporter/sbom/cyclonedx_test.go:12). `go test ./reporter/...` passes with network access disabled.