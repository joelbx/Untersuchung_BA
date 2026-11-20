Added `metadata.check_for_updates` to the configuration loader, with a default of `true` when metadata is absent. YAML and JSON files can both set it to `false`; the setting uses the existing validation and loading path. The [default configuration example](/app/config/default.yml) now documents it.

Tests passed: `GOPROXY=off go test ./...` and the config package tests after the final test update.