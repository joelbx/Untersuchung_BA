Task: Fix parsePkgName and CycloneDX PURL component construction for Maven, PyPI, Golang, npm, and Cocoapods.
Status: Complete. Added parsePkgName with three string returns; normalized scanner/manifest ecosystem identifiers; used parsed fields in library and dependency graph PURLs.
Verification: GOPROXY=off GOSUMDB=off go test ./reporter/sbom (pass); git diff --check (pass).
Delegation: None.
