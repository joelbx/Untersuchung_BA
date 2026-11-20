# Image digest issue checkpoint

Status: investigating root cause and existing test coverage.

Plan: trace configuration validation, image reference construction, scan conversion, OS detection, and report naming; reproduce with a failing test; make the smallest supported fix; run relevant existing tests.

Root cause: config.Image has only Name/Tag, IsValidImage requires Tag, scanImage constructs Name:Tag, conversion drops digest, report UUID naming constructs Name:Tag, and image OS detection embeds Tag in the generated server name. A working tag reference follows the same path; digest input has no field to survive it. Hypothesis: adding Digest to both image types and selecting one full reference at each construction point resolves the data loss and ambiguity.

Initial check: `go test ./config ./scan ./models ./report` found an incorrect expectation in the new test (empty image GetFullName is ":" by the required fallback) and an existing vet diagnostic in models/library.go:98,100 (Severity-to-string rune conversion). Corrected the test expectation. Rerunning tests with `-vet=off` to assess runtime behavior separately. Full command was still running when those results appeared.

Implementation: added Digest with json:"digest" to config and scan model, config.Image.GetFullName, exclusive tag/digest validation, scan conversion and scanner reference, digest-aware detection log and report UUID key, and tag/digest-free per-image server name. Regression tests cover validation/reference, conversion, and report UUID naming.

Verification:
- Before fix, `go test ./config -run TestImageDigestReference -count=1` failed to compile: unknown Digest field and missing GetFullName, as expected.
- `go test -vet=off ./config ./scan ./report -count=1` passed.
- `go test -vet=off ./config ./scan ./report ./models -run 'TestImageDigest|TestEnsureUUIDsImageReference|TestIsImage' -count=1` passed, with no matching models tests.
- `go test ./config ./scan ./models ./report` failed due to vet diagnostics at models/library.go:98,100 (conversion from Severity int to string yields one rune).
- `go test -vet=off ./config ./scan ./models ./report` failed at models.TestScan in models/library_test.go:45,48: `error occurred` and `no vuln found : actual: []`. This test uses the local Trivy vulnerability DB; its failure is unrelated to image reference formatting. Uncertainty: exact DB cause was not investigated because that check is outside this patch.
- `git diff --check` passed.
