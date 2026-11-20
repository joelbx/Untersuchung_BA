# Checkpoint

Task: support image digests across configuration, scanning, and reporting.

Changes: added digest fields to config and scan result images; added full-name helpers; enforced exclusive tag/digest validation with the required error strings; propagated digest through model conversion; used full references for scanning, logging, and report UUID names; changed per-image server names to `<index>@<originalServerName>`; added focused validation, conversion, and JSON tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./config ./models ./scan ./report`: exit 1. Config, scan, and report passed; models vet failed at `models/library.go:98,100`: `conversion from Severity (int) to string yields a string of one rune, not a string of digits`.
- `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./models ./scan ./report`: exit 1. Config, scan, and report passed; models `TestScan` failed at `models/library_test.go:45,48`: `error occurred` and `no vuln found : actual: []`. This test is outside the changed image paths; its dependency or fixture cause was not determined.
- `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./scan ./report`: exit 0.
- `GOPROXY=off GOSUMDB=off go test -vet=off ./models -run '^TestImageDigestJSON$' -count=1`: exit 0.
- `git diff --check`: exit 0.
