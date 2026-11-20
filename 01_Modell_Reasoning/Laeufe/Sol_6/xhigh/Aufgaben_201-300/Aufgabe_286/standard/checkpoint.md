# Checkpoint

Task: fix startup release detection, update reporting, and telemetry gating in /app.
Status: complete. Added internal/release Info, Is, and Check; startup uses release results for status and metadata and disables telemetry for non-release builds. Added release classification, comparison, and warning tests.
Verification: go test ./internal/release ./internal/info ./cmd/flipt ./internal/telemetry; go test ./internal/server/metadata; git diff --check. All passed.
