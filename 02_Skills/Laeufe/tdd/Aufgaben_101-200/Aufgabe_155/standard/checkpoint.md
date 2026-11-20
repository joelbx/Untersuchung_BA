# Checkpoint

Implemented digest support in image config, validation, scan model conversion, image scanning, server image naming, and report UUID naming.

Verification:
- Red: `GOTOOLCHAIN=local GOPROXY=off go test ./config ./scan ./report -run 'TestImageGetFullName|TestIsValidImageIdentifier|TestConvertToModelPreservesImageDigest|TestEnsureUUIDsReusesDigestImageIdentifier' -count=1` failed as expected: missing GetFullName, incorrect validation, dropped digest, and missing report UUID lookup.
- Green: same targeted command passed in config, scan, report after implementation and test refactor.
- `GOTOOLCHAIN=local GOPROXY=off go test ./...` failed in models vet on pre-existing `models/library.go:98,100`: conversion from Severity (int) to string yields one rune, not digits. Other packages including config, scan, report passed.
- `GOTOOLCHAIN=local GOPROXY=off go test -vet=off ./...` failed in pre-existing `models.TestScan` (`models/library_test.go:45,48`): scan error and no vulnerabilities found. Other packages including config, scan, report passed. The scan test depends on a local Trivy database; its state was not changed.
- A C compiler warning from the existing go-sqlite3 dependency appeared during test runs.
- `git diff --check` passed.
