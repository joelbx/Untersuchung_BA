# Checkpoint

Issue: support image digests alongside tags while enforcing exactly one identifier, and carry digest references consistently through scanning and reporting.

Implemented:
- Added `Digest` to config and scan result image types, plus `config.Image.GetFullName()`.
- Updated image validation for the required missing-name, missing-identifier, and conflicting-identifier errors.
- Propagated digests into scan results and used full image references for image scanning, detection logs, and report UUID identifiers.
- Assigned static image server names as positional `<index>@<originalServerName>` values, with deterministic map ordering, and copied each configured image directly.

Validation:
- `go test ./config ./models ./scan ./report`: config, scan, and report passed; models was blocked by existing `go vet` warnings in `models/library.go`.
- `go test -vet=off ./config ./models ./scan ./report`: config, scan, and report passed; existing `models.TestScan` failed because it found no vulnerability.
- All other existing models tests passed when `TestScan` was excluded.
