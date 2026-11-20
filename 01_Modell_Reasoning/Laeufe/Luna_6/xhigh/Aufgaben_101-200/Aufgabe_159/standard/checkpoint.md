# Checkpoint

Task: Resolve package name parsing for Maven, PyPI, Golang, npm, and Cocoapods PURLs.

Initial status: Starting repository inspection. I will use checked-out code and existing tests only.

Implementation: Added ecosystem name parsing and canonicalized Trivy package type labels during CycloneDX library PURL construction. Formatting completed; verification is pending.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./reporter/...` passed. The `reporter/sbom` package has no test files. `git diff --check` passed.
