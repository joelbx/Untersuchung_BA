# Checkpoint

Task: Fix `parsePkgName` ecosystem parsing in CycloneDX PURLs.
Status: Complete. Added parser and connected it to library and GitHub dependency PURL construction. Added regression coverage for Maven, PyPI, Golang, npm, Cocoapods, and fallback names.
Verification: `go test ./reporter/sbom` passed; `git diff --check` passed.
