# Checkpoint

Issue: restore backward compatibility for legacy `listenPorts` JSON while moving scanning and reachability logic to structured port stats.

Initial investigation: repository contains the Go code under `models`, `scan`, and `report`; `rg` is unavailable in this environment, so use `find`/`grep` for discovery.

Plan: inspect the package/process types and all listener-port consumers; implement the legacy string field, structured `PortStat` APIs and nil-safe selection/reachability helpers; adapt scanning call sites; run relevant existing Go tests.

Implementation complete:
- `AffectedProcess.ListenPorts` is now the legacy `[]string` JSON field, with structured `ListenPortStats []PortStat` serialized separately.
- Added `PortStat`, IP/port parsing, reachable-port detection, and legacy string conversion for reports.
- Scan destination detection, wildcard expansion, and reachability updates use structured stats; nil stats are skipped safely.
- Updated Debian/Red Hat process collection and report renderers; retained the old `ListenPort` helper type for source compatibility.
- Updated scan test fixtures to the new structured field.

Verification: `go test ./models ./scan ./report` passes; `git diff --check` passes.
