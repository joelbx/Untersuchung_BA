Added `metadata.check_for_updates` to the configuration loader for YAML and JSON. It defaults to `true` when omitted and accepts `false` to disable the preference. I also updated the sample config and added loading tests.

`go test ./config` passes.