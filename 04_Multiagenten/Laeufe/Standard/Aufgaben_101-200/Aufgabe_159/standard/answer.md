Added `parsePkgName` and connected it to CycloneDX PURL construction for library and GitHub dependency packages. It returns namespace, name, and subpath for the five requested ecosystems, with empty strings for fields that do not apply. Added regression tests.

`go test ./reporter/sbom` and `git diff --check` passed.