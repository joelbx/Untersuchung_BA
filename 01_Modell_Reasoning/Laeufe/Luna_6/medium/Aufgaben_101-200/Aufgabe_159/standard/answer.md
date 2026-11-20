Implemented `parsePkgName` in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go:308) for Maven, PyPI, Golang, npm, and Cocoapods. Both lockfile and dependency graph PURLs now use its namespace, name, and subpath values.

Verification: `go test ./reporter/sbom` passed; `git diff --check` passed.