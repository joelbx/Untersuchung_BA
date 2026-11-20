Added `Metadata.CheckForUpdates` to the [configuration](/app/config/config.go), enabled by default and loadable through `metadata.check_for_updates` in YAML or JSON. The [default configuration example](/app/config/default.yml) documents the setting.

Existing configuration tests pass (`go test ./config`), including the new YAML and JSON cases.