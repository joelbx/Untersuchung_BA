Task: fix rollout audit segment fields and constructor mappings.
Updated internal/server/audit/types.go to expose optional operator fields and map legacy, single, and multiple segment keys. Added focused JSON and mapping tests in types_test.go. Offline `go test ./internal/server/audit/...` passed across all audit packages. Restored incidental go.work.sum change; git diff --check passed.
