# Progress checkpoint

- Found CycloneDX PURLs constructed from raw library and dependency names in `reporter/sbom/cyclonedx.go`; `parsePkgName` did not exist.
- Added package type mapping and `parsePkgName`, and wired namespace, name, and subpath into both PURL call sites.
- Added focused parser and PURL checks in `reporter/sbom/cyclonedx_test.go`.
- Verified `GOPROXY=off GOSUMDB=off go test ./reporter/sbom` and `GOPROXY=off GOSUMDB=off go test ./reporter/...` pass.
- `git diff --check` passes. Implementation is complete.
