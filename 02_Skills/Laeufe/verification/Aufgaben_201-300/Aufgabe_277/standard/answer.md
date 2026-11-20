Updated the rollout audit structures to include the optional JSON operator fields. `NewRule` and `NewRollout` now copy a single segment key or join multiple keys with commas and record the operator name. Legacy single-key values remain supported.

Added tests for segment handling and JSON serialization. `GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed.