VERDICT: FIX

**Code defect:** [purlPkgType](/app/reporter/sbom/cyclonedx.go:314) omits scanner types `node-pkg`, `javascript`, `python-pkg`, and `gobinary`. The scanner passes these types through to [PURL construction](/app/reporter/sbom/cyclonedx.go:263), so affected packages bypass npm, PyPI, or Go name parsing. Map those types to their PURL ecosystems and cover the scanner path.

**Tests:** Both commands passed:

- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./reporter/sbom -run 'TestParsePkgName|TestDependencyPURLs' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./reporter/sbom -count=1`

**TEST_ENVIRONMENT_PROBLEM:** None. I made no project code changes.