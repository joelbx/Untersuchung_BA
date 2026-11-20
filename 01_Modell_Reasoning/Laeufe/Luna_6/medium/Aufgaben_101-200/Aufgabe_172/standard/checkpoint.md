# Checkpoint

Implemented the legacy `listenPorts []string` field alongside structured `ListenPortStats`, added `PortStat`, `NewPortStat`, and `Package.HasReachablePort`, and migrated scanning, reachability, and report rendering to structured stats. Updated scan fixtures to the new structured field.

Validation: `go test ./models ./scan ./report` passes. `git diff --check` passes.
