Added `metadata.check_for_updates` to Flipt’s configuration. It defaults to `true` when omitted and accepts `false` in YAML or JSON. The setting is also shown in the sample configuration.

Tests cover the default and both file formats. `go test ./...` passed; the sqlite3 dependency emitted a compiler warning.