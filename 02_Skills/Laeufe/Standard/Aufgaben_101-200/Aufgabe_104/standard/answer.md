Added `metadata.check_for_updates` to the configuration loader. It defaults to `true` when omitted and accepts `false` in YAML or JSON. I updated the default config example and added loading tests.

`GOPROXY=off go test ./...` passed.