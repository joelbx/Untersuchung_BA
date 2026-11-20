Added first-class `KEVs` to `VulnInfo`, with CISA and VulnCheck source types and their nested detail structs. CISA retrieval now maps catalog records—including notes and optional due dates—onto the vulnerability while retaining legacy alert data. Added `FormatKEVCveSummary()` and deterministic sorting by source type and vulnerability name.

Verification: `go test ./models` passed; `go test -vet=off ./detector -run '^$'` passed. The combined test command was interrupted during dependency vet/compile. `git diff --check` passed.

The repository’s current KEV client supplies CISA data only, so VulnCheck structures are defined but have no source to populate them yet.