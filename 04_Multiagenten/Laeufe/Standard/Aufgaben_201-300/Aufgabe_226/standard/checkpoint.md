# Checkpoint

Task completed: MIME definitions moved from `consts/mime_types.go` to `resources/mime_types.yaml`. New `mime` package loads the resource (including data-folder resource overrides) via `conf.AddHook`, registers extension mappings and explicit JS/CSS types, and publishes sorted extension names without periods in `mime.LosslessFormats`. Model registers the hook when used independently; server UI reads the new list.

Validation: `GOPROXY=off GOTOOLCHAIN=local go test ./mime ./server ./model ./core ./cmd` passed (cmd has no tests). `git diff --check` passed.
