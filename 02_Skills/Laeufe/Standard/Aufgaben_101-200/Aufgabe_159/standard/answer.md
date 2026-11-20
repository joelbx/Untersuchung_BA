Added `parsePkgName(t, n)` and used its namespace, name, and subpath values when building CycloneDX library and GitHub dependency PURLs. It handles the five requested ecosystems and the package type aliases used by the scanners. Added focused tests.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./reporter/sbom` and `git diff --check`.