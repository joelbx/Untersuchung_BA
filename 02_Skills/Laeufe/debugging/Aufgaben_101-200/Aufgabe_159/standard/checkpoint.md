# Debugging checkpoint

Issue: CycloneDX library and dependency PURLs do not parse ecosystem package names.

Initial evidence: `reporter/sbom/cyclonedx.go` constructs PURLs with empty namespace and subpath at library and dependency call sites. No `parsePkgName` exists in checked-out Go code. `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find.

Next: inspect call sites and local tests, add failing focused tests, implement parser and integrate it, run offline tests.

Root cause confirmed: both `libpkgToCdxComponents` and `ghpkgToCdxComponents` supplied unsplit package names with empty namespace/subpath; Trivy ecosystem identifiers such as `pom`, `pip`, and `gomod` also differ from PURL identifiers. Regression test first failed at compile time with `undefined: parsePkgName`. Implemented ecosystem mapping plus parser at both call sites. Initial post-fix test found incorrect expected qualifier and subpath encoding in the test itself; adjusting expectations to actual existing package-url behavior.

Verification: `GOPROXY=off go test ./reporter/sbom -count=1` passed. `GOPROXY=off go test ./reporter/... -count=1` passed (reporter and reporter/sbom). `git diff --check` passed. Focused tests cover parser values and generated library/dependency graph PURLs. No downloads used.
