Updated [cyclonedx.go](/app/reporter/sbom/cyclonedx.go) to parse Maven, PyPI, Golang, npm, and Cocoapods names into PURL namespace, name, and subpath. Trivy analyzer labels are mapped to canonical PURL types during SBOM generation.

`GOTOOLCHAIN=local GOPROXY=off go test ./reporter/...` passed. The SBOM package has no test files. `git diff --check` passed.