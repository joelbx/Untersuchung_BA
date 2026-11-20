Issue: startup release and update checks; release candidates must be non-release.
Status: implemented and verified.
Changes: added internal/release Info, Is, Check; startup uses those results for console/logger status, info.Flipt, and telemetry gating. Non-release builds emit the required debug message.
Verification: go test ./internal/release ./cmd/flipt ./internal/info ./internal/telemetry (passed); git diff --check (passed).
Delegation: none.
