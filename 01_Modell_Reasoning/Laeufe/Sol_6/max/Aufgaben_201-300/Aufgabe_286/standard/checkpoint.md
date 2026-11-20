# Checkpoint

Task: Separate startup release/update logic into `internal/release`, correctly classify `-rc` and other prerelease versions, preserve update reporting, and gate telemetry.

Status: Complete. Added `internal/release` with release classification and update checking; startup uses its result for status output, metadata, and telemetry gating. The release tests cover prerelease classification, available/current versions, and a failed update request with warning logging.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./internal/release ./cmd/flipt ./internal/info ./internal/telemetry ./internal/server/metadata` passed. `git diff --check` passed.
