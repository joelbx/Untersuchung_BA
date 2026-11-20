# Checkpoint

Task: Add digest-aware image configuration, validation, scanning, and reporting.
Status: Inspecting local code. `rg` is unavailable; using `grep` and `find`.

Initial check: `GOPROXY=off GOSUMDB=off go test ./config ./models ./scan ./report` encountered preexisting go vet errors in `models/library.go:98` and `:100`: conversion from Severity (int) to string yields a string of one rune, not digits. Rerunning with `-vet=off` to test changed packages without altering unrelated code.

Implemented digest field and full-reference formatting in config and scan models; validation enforces exactly one tag or digest; scan and report paths now use full references; image scan server names use `<image-key>@<serverName>`. Added focused config, scan conversion, and reporting tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./scan ./report` passed.
- `GOPROXY=off GOSUMDB=off go test -vet=off ./models -run 'Test(Except|SourceLinks|VendorLink|MergeNewVersion|Merge|AddBinaryName|FindByBinName|Filter|IsDisplay|Titles|Summaries|Count|ToSorted|Cvss|MaxCvss|FormatMax|Sort|Store|Append|Distro|Vuln)'` passed.
- `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./models ./scan ./report` failed only in existing `models.TestScan`: `library_test.go:45: error occurred`, `library_test.go:48: no vuln found : actual: []`. This test requires vulnerability database data unavailable locally. The changed packages passed in that run.
- The initial `go test` without `-vet=off` failed in existing `models/library.go:98` and `:100` on Severity int-to-string conversion vet errors.
