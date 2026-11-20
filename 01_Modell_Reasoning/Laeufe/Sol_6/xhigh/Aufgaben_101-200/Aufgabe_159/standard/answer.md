Updated [CycloneDX PURL construction](/app/reporter/sbom/cyclonedx.go:262) to parse namespace, name, and subpath for Maven, PyPI, Golang, npm, and Cocoapods. Added [regression tests](/app/reporter/sbom/cyclonedx_test.go:12) for the parser and generated PURLs.

`GOPROXY=off GOSUMDB=off go test ./reporter/...` passes.