Added `metadata.check_for_updates` to the configuration loader. It defaults to `true` when omitted and can be set to `false` in YAML or JSON. The default config example and tests now cover the setting.

Verification: `git diff --check`, `go test ./config`, and `go test ./...` passed with offline dependency settings.