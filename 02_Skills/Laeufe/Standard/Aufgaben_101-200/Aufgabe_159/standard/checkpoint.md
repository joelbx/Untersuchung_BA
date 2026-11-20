# Checkpoint

- Issue: parse package names for ecosystem PURLs in CycloneDX SBOM output.
- Initial finding: `parsePkgName` does not exist in this checkout; `reporter/sbom/cyclonedx.go` constructs library and GitHub dependency PURLs with unparsed package names.
- Implemented `parsePkgName(t, n)` for Maven, PyPI, Golang, npm, and Cocoapods, including aliases emitted by library and GitHub manifest scanners. Wired its three return values into both PURL construction paths.
- Added parser and library PURL tests in `reporter/sbom/cyclonedx_test.go`.
- Verification: `GOPROXY=off GOSUMDB=off go test ./reporter/sbom` passed. `git diff --check` passed.
- Initial test run failed because the test expected `%2B` in a Cocoapods subpath; packageurl-go preserves `+`. Corrected the expectation and reran successfully.
