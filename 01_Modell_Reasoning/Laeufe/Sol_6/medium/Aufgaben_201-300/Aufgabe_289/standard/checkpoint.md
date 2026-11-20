# Config default validation checkpoint

Task: expose canonical default config and decode hooks, align Load decoding, and verify defaults against the existing config tests and CUE schema.

Status: complete. Exported DefaultConfig and DecodeHooks; Load composes exported hooks; added version tag and pointer storage sub-configurations with nil-safe validation. Existing tests use the exported default and pointer fixtures. Verified with `go test ./internal/config ./internal/cmd` and focused config tests; `git diff --check` passes.
