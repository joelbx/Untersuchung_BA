# Checkpoint

Task: Add digest-aware image configuration, scanning, and reporting.
Status: implemented and verified.

Changes:
- Added `Digest` to config and scan result image structs and `config.Image.GetFullName()`.
- Validation requires a name and exactly one of tag or digest, with the requested error text.
- Scanning uses the full image reference; scan models retain digest.
- Image detection uses `<image key>@<server name>` for per-image server names and logs full references.
- Report UUID keys use `<full image reference>@<server name>`.
- Added coverage for validation, conversion, and report UUID names.

Verification: `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./models ./scan ./report -skip '^TestScan$'` passed. The unmodified `models.TestScan` requires a local Trivy vulnerability DB and fails with no findings. Default `go test` also stops on existing `go vet` warnings in `models/library.go`.
