Task: Fix rollout audit segment data in Rule and RolloutSegment constructors.
Status: Implemented and verified.
Changes: Added optional operator JSON fields; constructors map one segment key or join multiple keys and record the operator, preserving legacy key fallback. Added focused constructor and JSON tests.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/server/audit/... passed. git diff --check passed.
Delegation: None.
