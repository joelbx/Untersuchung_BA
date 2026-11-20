Task: Fix parsePkgName and SBOM PURLs for Maven, PyPI, Golang, npm, and Cocoapods.
Status: Complete.
Changes: Added parsePkgName, normalized scanner ecosystem labels to PURL types, and applied parsing in library and GitHub manifest PURL construction. Added parser and PURL integration tests.
Verification: GOPROXY=off GOSUMDB=off go test ./reporter/... passed; git diff --check passed.
