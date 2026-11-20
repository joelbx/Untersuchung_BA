Exported `DefaultConfig()` and `DecodeHooks`, and made `Load` compose the exported hooks. Added the version mapstructure tag and changed storage’s Local and Git fields to pointers, with validation for missing values.

Updated the existing config fixtures and added a duration decoding test. `go test ./internal/config ./internal/cmd` and `git diff --check` pass.