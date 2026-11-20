# Checkpoint

- Task: fix package name parsing for Maven, PyPI, Golang, npm, and Cocoapods PURLs.
- Initial state: working tree clean; `parsePkgName` is not present by name in the current checkout.
- Implemented `parsePkgName` in the CycloneDX reporter and wired it into library and GitHub dependency PURL creation.
- Added a table-driven regression test covering all five requested ecosystems and fallback cases.
- Verified: `GOTOOLCHAIN=local GOPROXY=off go test ./reporter/sbom` passed.
- Verified: `GOTOOLCHAIN=local GOPROXY=off go test ./reporter/...` passed.
- `git diff --check` passed.
