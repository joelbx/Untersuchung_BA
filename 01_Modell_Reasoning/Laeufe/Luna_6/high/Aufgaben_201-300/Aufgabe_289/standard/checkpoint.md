# Checkpoint

Implemented the public `DefaultConfig` constructor and `DecodeHooks` slice in `internal/config/config.go`. `Load` composes a copy of the exported hooks with its experimental-field hook. Added the missing `version` mapstructure tag and changed storage local/git fields to pointers with nil-safe validation. Updated existing storage test expectations to use pointers.

Verification: `go test ./internal/config` passes. `go test ./internal/config ./internal/cmd` initially reported a stale test composite literal after the pointer change; the command also passed `internal/cmd`. The config package passed on rerun after correcting that literal.
