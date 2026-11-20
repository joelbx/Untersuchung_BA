Implemented anonymous telemetry with a default-on config option, environment opt-out, persistent UUID state, and a four-hour reporting loop. Telemetry errors are logged without interrupting startup. Added the `internal/info.Flipt` HTTP handler and disabled telemetry in the advanced config example.

Verification passed: `go test ./...` and `git diff --check`.

The reporter posts to Segment’s tracking endpoint by default. This repository contains no Segment write key; set `FLIPT_META_TELEMETRY_WRITE_KEY` for an authenticated Segment source. The endpoint can be overridden with `FLIPT_META_TELEMETRY_ENDPOINT`.