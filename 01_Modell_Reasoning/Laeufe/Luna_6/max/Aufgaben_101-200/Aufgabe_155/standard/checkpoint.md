# Checkpoint

Task: support digest-based image references consistently alongside tags.

Implemented:
- Added Digest fields to config and scan-result images, with `json:"digest"`.
- Added full-reference helpers; validation now requires exactly one of Tag or Digest and returns the specified errors.
- Propagated Digest into scan results and used full references for scanning, detection logs, and image UUID/report identifiers.
- Set per-image OS detection server names to `<iteration index>@<original server name>`.

Verification:
- `config`, `scan`, and `report` package tests passed with `GOPROXY=off` and `-vet=off`.
- `models` tests passed with `TestScan` skipped. `TestScan` failed in the full run because it found no vulnerabilities in its scanner database.
- The default `go test` run also reported existing int-to-string vet warnings in `models/library.go`; no external downloads were attempted.
- `git diff --check` passed.
