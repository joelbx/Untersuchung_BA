Implemented opt-out anonymous telemetry. It stores a per-host UUID in `telemetry.json`, sends a `flipt.ping` event when due and every four hours, and records successful reports. Telemetry errors are logged without stopping Flipt. The advanced config example disables it, and `Flipt` now has an HTTP JSON handler.

Validation: `GOPROXY=off go test ./...` passed.