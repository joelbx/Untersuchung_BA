Added `metadata.check_for_updates` to Flipt’s configuration, with a default of `true`. YAML and JSON files can set it to `false`; the default config now documents the option.

Tests cover both file formats and the default after an explicit override. `go test ./...` passed.