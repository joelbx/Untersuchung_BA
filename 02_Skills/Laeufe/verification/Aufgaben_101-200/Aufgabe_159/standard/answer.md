Updated [CycloneDX PURL construction](/app/reporter/sbom/cyclonedx.go) to parse namespace, name, and subpath for Maven, PyPI, Golang, npm, and Cocoapods packages. Added [tests](/app/reporter/sbom/cyclonedx_test.go) for the parser and both PURL construction paths.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./reporter/...` and `git diff --check`.