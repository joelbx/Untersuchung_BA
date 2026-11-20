Added `metadata.check_for_updates` to the configuration loader, with a default of `true`. Users can set it to `false` in YAML or JSON; the example configuration and tests now cover the option.

`go test ./config` and `go test ./...` passed. No delegation was used.