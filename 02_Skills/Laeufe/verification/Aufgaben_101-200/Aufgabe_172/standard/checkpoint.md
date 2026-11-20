# Checkpoint

Task: restore compatibility with legacy `listenPorts` strings and keep structured scan port statistics.

Implemented:
- `AffectedProcess.ListenPorts []string` for legacy JSON; `ListenPortStats []PortStat` for scan data.
- `NewPortStat` parsing and validation, `Package.HasReachablePort`.
- Scanner destination, reachability, and report display paths updated for the split fields.
- Model regression tests and cross-package destination test added; existing scan tests updated for the new fields.

Verification:
- `GOPROXY=off go test ./models ./scan ./report && git diff --check` exited 0 on final edits. All three package test suites passed. The compiler emitted only an existing sqlite3 C warning.
- An earlier test run failed because a TUI method reference had not yet been renamed; it was corrected before the passing final run.
- The first attempt at the final run failed at gofmt due to a missing brace in the newly added test; corrected before the passing final run.

No offline tooling checks remain blocked.
