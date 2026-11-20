# Rollout audit segment fields

Status: complete. Added optional operator fields to the audit structures, mapped one or multiple segment keys in both constructors, and retained the legacy key fallback. Added coverage for legacy, single, and multiple segments plus JSON omission. `GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed. Restored the incidental `go.work.sum` change from the test run.
