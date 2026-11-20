Added `parsePkgName` in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go:21) with the requested handling for Maven, PyPI, Golang, npm, and Cocoapods, returning three strings in every case.

`git diff --check` passed. I attempted `go test ./reporter/sbom`, but it did not finish and had to be interrupted, so test results are unavailable.