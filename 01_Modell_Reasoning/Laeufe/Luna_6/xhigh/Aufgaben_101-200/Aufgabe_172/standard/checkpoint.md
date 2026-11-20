# Checkpoint

Issue: preserve compatibility with legacy Vuls scan JSON where affected process listening ports are strings, while providing structured listening-port stats for scanning and destination selection.

Completed:
- `AffectedProcess` now reads legacy string arrays and prior structured arrays, and stores new structured data in `ListenPortStats`.
- Added `PortStat`, `NewPortStat`, matching/reachability logic, and `Package.HasReachablePort`.
- Scanner destination selection, listener reachability updates, and both report renderers now use structured stats with legacy string display fallback.
- Migrated existing scan tests to the structured field.

Verification: `go test ./models ./scan ./report` passed; `git diff --check` passed.
