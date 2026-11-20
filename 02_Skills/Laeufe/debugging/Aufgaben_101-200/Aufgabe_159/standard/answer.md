Fixed CycloneDX PURL construction in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go). `parsePkgName` now returns namespace, name, and subpath for the requested ecosystems, and both library and dependency graph components use those values. Added regression tests in [cyclonedx_test.go](/app/reporter/sbom/cyclonedx_test.go).

`GOPROXY=off go test ./reporter/... -count=1` passed.