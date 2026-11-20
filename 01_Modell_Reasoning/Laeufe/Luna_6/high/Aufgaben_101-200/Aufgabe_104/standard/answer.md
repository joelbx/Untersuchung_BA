Added `Metadata.CheckForUpdates` with a default of `true`. The loader supports the YAML key `metadata.check_for_updates` and the JSON field `metadata.checkForUpdates`; the sample config and tests cover defaults and explicitly disabling checks.

Verified with `go test ./config` (pass).