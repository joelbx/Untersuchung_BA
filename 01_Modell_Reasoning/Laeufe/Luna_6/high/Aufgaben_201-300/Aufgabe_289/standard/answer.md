Implemented the exported `DefaultConfig` and `DecodeHooks`, wired `Load` to compose the exported hooks, added the `version` mapstructure tag, and changed storage Local/Git fields to pointers with nil-safe validation.

`go test ./internal/config ./internal/cmd` passes. Updated the existing storage test fixtures for the pointer fields.