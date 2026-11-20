Task: Repair rollout audit segment metadata.
Located relevant constructors and types in internal/server/audit/types.go.
Completed: Added optional operator fields and segment-list handling to audit constructors, with tests for legacy, single, and multiple segments and JSON omission.
Verified: go test ./internal/server/audit/... passed. Restored incidental go.work.sum changes. git diff --check passed.
