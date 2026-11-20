Added `parsePkgName` and wired it into SBOM PURL construction for library and dependency graph packages. It splits Maven, Go, scoped npm, and Cocoapods names into the required fields and normalizes PyPI names. Added focused parser tests.

Verification: `go test ./reporter/sbom` passed.