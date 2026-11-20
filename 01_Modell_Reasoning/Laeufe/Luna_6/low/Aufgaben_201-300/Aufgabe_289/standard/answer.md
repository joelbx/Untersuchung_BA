Implemented the exported `DefaultConfig()` and `DecodeHooks`, and updated `Load` to compose the exported hooks. Storage now uses pointer fields for Local and Git, with nil-safe validation. I also added the `version` mapstructure tag and preserved conditional database URL defaults.

Verified with `go test ./internal/config -run 'Test(JSONSchema|Load)$' -count=1` — passed.