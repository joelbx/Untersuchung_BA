VERDICT: FIX
Code defect: reporter/sbom/cyclonedx.go purlPkgType omits Trivy scanner aliases node-pkg, javascript, python-pkg, and gobinary; these are passed through as PURL types and bypass npm/PyPI/Go name parsing. The scanner carries app.Type directly into LibraryScanner.Type. Add alias mappings and cover these paths with existing tests in the patch.
Tests executed successfully:
GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./reporter/sbom -run 'TestParsePkgName|TestDependencyPURLs' -count=1
GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./reporter/sbom -count=1
No TEST_ENVIRONMENT_PROBLEM.
