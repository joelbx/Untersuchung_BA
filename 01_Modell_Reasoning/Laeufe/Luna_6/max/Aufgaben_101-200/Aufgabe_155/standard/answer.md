Implemented digest support across image configuration, scanning, and reporting.

- Added `Digest` fields and `GetFullName()` helpers; validation now requires exactly one of Tag or Digest.
- Propagated digests into scan results and used full image references for scan domains, detection logs, and report identifiers.
- Changed per-image OS detection names to `<index>@<serverName>`.

Verification: config, scan, and report tests passed. Model tests passed with `TestScan` skipped; that existing test failed because its scanner database found no vulnerabilities. The default test run also reported existing vet warnings in `models/library.go`.

Updated [checkpoint.md](/app/.codex-role-output/checkpoint.md).