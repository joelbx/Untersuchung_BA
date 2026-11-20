Fixed PURL package name parsing for Maven, PyPI, Golang, npm, and Cocoapods. Library scans and GitHub manifests now pass the parsed namespace, name, and subpath into PURL construction. Added [tests](/app/reporter/sbom/cyclonedx_test.go) covering the parser and generated PURLs.

`go test ./reporter/sbom` and `git diff --check` passed.