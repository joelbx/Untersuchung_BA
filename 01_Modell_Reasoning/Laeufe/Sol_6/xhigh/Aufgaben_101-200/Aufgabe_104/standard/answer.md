Added `metadata.check_for_updates` to the configuration loader, with version checking enabled by default. Users can set it to `false` in YAML or JSON. The default config documents the setting, and tests cover both file formats and the default.

`go test ./...` passes.

The repository has no startup version-check routine to consume this preference yet; this change makes the setting available in configuration.