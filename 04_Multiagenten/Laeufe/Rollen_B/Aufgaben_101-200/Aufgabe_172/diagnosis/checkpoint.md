# Fault localization progress

Diagnosis complete. `report/util.go:746` unmarshals scan JSON into `models.ScanResult`; `models/packages.go:179` declares `AffectedProcess.ListenPorts []ListenPort` with `json:"listenPorts,omitempty"`, so a legacy string element triggers the reported type error.

Change surface for implementation: `models/packages.go` needs legacy `[]string` plus structured `ListenPortStats []PortStat`, `NewPortStat`, and `Package.HasReachablePort`; `scan/base.go` destination selection, reachability update, matching, and current parser must use the structured field; `scan/debian.go` and `scan/redhatbase.go` populate the field; `report/tui.go` and `report/util.go` display structured ports and reachability. Existing `scan/base_test.go` covers deduplication, wildcard expansion, nil slices, multi-package updates, and matching but uses the old type and field. There is no legacy JSON decoding test or malformed port parser test in the inspected tests.

No project source or tests modified. Tests were not run because this assignment is fault localization only.
