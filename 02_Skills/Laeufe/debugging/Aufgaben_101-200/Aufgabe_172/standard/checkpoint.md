# Checkpoint

Task: restore legacy `listenPorts` report parsing and provide structured scanning port statistics.

Status: investigating model and scan data flow. `rg` is unavailable; using `grep` and local files. Repository initially clean.

Root cause evidence: `models.AffectedProcess.ListenPorts` is `[]ListenPort` with JSON name `listenPorts`. Legacy JSON stores an array of strings at that name, so `encoding/json` fails before reporting. `scan/base.go`, Debian/RedHat process detection, and report renderers directly consume the structured field. The existing scan destination routine already deduplicates and expands wildcard addresses; its input field must change.

Hypothesis: assigning `listenPorts` back to `[]string` and moving structured scan data to a distinct `listenPortStats` field will let legacy JSON unmarshal and keep scan behavior after all consumers move to that field.

Regression confirmed before fix: `go test ./models -run TestLegacyAffectedProcessListenPortsJSON -count=1` failed with `json: cannot unmarshal string into Go struct field AffectedProcess.AffectedProcs.listenPorts of type models.ListenPort` (exit 1).

Implemented: legacy JSON field is `[]string`; structured scan field is `[]PortStat`; scan producers, destination selection, reachability, and report display use the new field. Added `NewPortStat` and `HasReachablePort`. Focused command `go test ./models ./scan ./report -run 'TestLegacyAffectedProcessListenPortsJSON|TestNewPortStat|Test_detectScanDest|Test_updatePortStatus|Test_matchListenPorts' -count=1` passed (exit 0); C SQLite compiler emitted an existing warning.

Final verification: `go test ./models ./scan ./report -count=1 && git diff --check` exited 0. Models, scan, and report tests passed. The only output besides test results was the C compiler warning from github.com/mattn/go-sqlite3. Added coverage for JSON legacy string ports, public reachability method and parser, destination aggregation across packages, wildcard expansion, duplicates, and nil process stats. No unresolved check failure.
