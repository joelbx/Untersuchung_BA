Implemented `parsePkgName` in [cyclonedx.go](/app/reporter/sbom/cyclonedx.go) and wired its namespace, name, and subpath into library PURL generation for the requested ecosystems.

`go test ./reporter/sbom ./reporter` passed, and `git diff --check` passed.