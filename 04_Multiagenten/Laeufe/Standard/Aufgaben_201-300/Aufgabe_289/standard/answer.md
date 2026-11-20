Exported `DefaultConfig` and `DecodeHooks`, and updated `Load` to use the exported hooks. Storage’s Local and Git fields now use pointers, with validation for missing sub-configuration. The existing default configuration tests now use the exported function.

`go test ./internal/config ./internal/cmd` and `git diff --check` passed.