VERDICT: FIX

**Code defect:** [report/report.go](/app/report/report.go:523) splits an image server name at the first `@`. Image keys are unrestricted strings, so an image key `team@prod` on `host` produces `team@prod@host`; reporting then looks up `prod@host` and can write a spurious server entry. Resolve the original server without assuming image keys lack `@`.

**TEST_ENVIRONMENT_PROBLEM:** Relevant tests were attempted:

- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config ./models ./scan ./report` — failed: Go vet flagged unchanged conversions in `models/library.go:98,100`; the other three packages passed.
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test -vet=off ./config ./models ./scan ./report` — failed: existing `models.TestScan` reported a scan error and no vulnerabilities; the other three packages passed.
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test -vet=off ./config ./scan ./report -run 'TestIsValidImage|TestImageGetFullName|TestConvertToModelImageDigest|TestEnsureUUIDsImageDigest' -count=1` — passed.

The review note is in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code was changed during this independent review.