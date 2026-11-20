Implemented `DefaultConfig` and exported `DecodeHooks`, with `Load` using the same hooks. Storage `Local` and `Git` are now pointers, with nil guards; the affected test fixtures were updated.

`go test ./internal/config ./internal/cmd` and `git diff --check` pass. The checked-out repository has no CUE-specific configuration test, so that validation could not be run here.