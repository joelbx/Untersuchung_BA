# Rollout audit log repair checkpoint

- Added JSON optional `Rule.SegmentOperator` and `RolloutSegment.Operator` fields.
- `NewRule` and `NewRollout` use `SegmentKeys` when present: one key is copied, multiple keys are comma joined and include the operator name. Deprecated single-key fields remain the fallback when the list is empty.
- Added local tests for legacy, single, and multiple segments, rollout value, and optional JSON operator fields.
- Verification: `GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` exited 0; audit, kafka, log, template, and webhook packages passed.
- Initial `rg --files -g '!vendor' -g '!node_modules'` was unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` fallback.
