Exported `DefaultConfig()` and `DecodeHooks`, and made `Load` compose the exported hooks. Storage’s Local and Git fields now use pointers with nil-safe validation. I also added the version mapstructure tag, fixed an invalid CUE type, and added a regression test for CUE validation and duration decoding.

`go test ./internal/config ./internal/cmd ./internal/telemetry -count=1` passes.