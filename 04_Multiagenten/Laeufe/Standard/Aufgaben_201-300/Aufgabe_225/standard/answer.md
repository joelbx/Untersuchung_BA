Added a first-class `KEVs` field to vulnerabilities, with CISA and VulnCheck details. Both KEV retrieval paths now populate it, zero due dates become `nil`, and JSON output sorts entries by source and vulnerability name. Added `FormatKEVCveSummary()` and focused tests.

Verified with `GOPROXY=off GOSUMDB=off go test ./models ./detector`.