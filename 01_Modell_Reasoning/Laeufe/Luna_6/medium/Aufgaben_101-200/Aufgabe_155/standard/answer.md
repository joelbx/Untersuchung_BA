Implemented digest support across image configuration, scan results, scanning, and reporting.

- Added `Digest` fields and `config.Image.GetFullName()`.
- Updated image validation to require a name and exactly one of tag or digest.
- Propagated digests into scan results and used full references for image fetching, detection logs, and report identifiers.
- Changed per image OS detection names to `<index>@<originalServerName>`.

Verification: config, scan, and report tests pass with `go test -vet=off`. The models test fails in existing `TestScan` because vulnerability data is absent; the normal test run also reports pre existing vet diagnostics in `models/library.go`.