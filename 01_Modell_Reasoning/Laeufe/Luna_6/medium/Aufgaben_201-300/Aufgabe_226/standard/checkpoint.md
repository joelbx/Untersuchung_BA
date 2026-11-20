# Checkpoint

Implemented runtime MIME configuration:
- Added root `mime_types.yaml` with the prior audio/image MIME mappings and lossless extensions.
- Added `mime` package hook registered with `conf.AddHook`; it loads YAML during `conf.Load()`, registers mappings, registers the required `.js`/`.css` types, and fills sorted `LosslessFormats` without leading dots.
- Removed the old MIME and lossless definitions from `consts/mime_types.go`.
- Updated the server UI configuration and its existing test to read `mime.LosslessFormats`; imported the package from the application entry point so the hook is registered.

Verification: `go test ./mime ./server` passed; `git diff --check` checked next.
