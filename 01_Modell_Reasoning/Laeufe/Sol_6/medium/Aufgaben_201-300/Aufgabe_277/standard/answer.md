Added the optional operator fields to the audit structures. `NewRule` and `NewRollout` now use a single segment key directly, join multiple keys with commas, and record the operator for multiple segments. Legacy single keys remain supported.

Added mapping and JSON tests. All audit package tests passed with `go test ./internal/server/audit/...`.