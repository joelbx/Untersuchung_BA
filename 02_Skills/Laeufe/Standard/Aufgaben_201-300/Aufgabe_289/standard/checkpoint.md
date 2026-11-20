# Config validation checkpoint

Implemented:
- Exported `DefaultConfig() *Config` using the existing test defaults as the canonical values.
- Exported `DecodeHooks []mapstructure.DecodeHookFunc`; `Load` composes a copy of these hooks plus its experimental field hook.
- Added the missing `version` mapstructure tag.
- Changed storage Local and Git to pointers and guarded validation for missing sub-configurations. Existing Git authentication BasicAuth remains a pointer.
- Added a direct mapstructure decode test for durations and Git storage pointers; existing default load expectations now use `DefaultConfig`.

Checks run offline (`GOPROXY=off GOSUMDB=off`):
- `go test ./internal/config ./internal/cue` — passed.
- `go test ./internal/cmd` — passed.
- `git diff --check` — passed.

No `internal/config/schema_test.go` exists in this checkout; the existing config and CUE package tests passed. `rg` is unavailable (`/bin/bash: rg: command not found`), so local filesystem tools were used.
