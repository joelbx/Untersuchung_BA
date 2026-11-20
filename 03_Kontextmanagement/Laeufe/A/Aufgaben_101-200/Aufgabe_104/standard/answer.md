Added `metadata.check_for_updates` to Flipt’s configuration. It defaults to `true` and can be set to `false` in YAML or JSON.

Verified with `go test ./config` and `go test ./cmd/flipt ./config`.