Updated the rollout audit structures and constructors to record comma-separated keys and operator names for multiple segments, while preserving single-segment and legacy key handling. Added tests for the field values and JSON omission behavior.

`GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed. No delegation was used.