# Checkpoint

Issue: Load MIME types and lossless audio formats from `mime_types.yaml` at application startup.

Completed:
- Added `resources/mime_types.yaml` with the former audio and image mappings and lossless extension list. The resource filesystem supports runtime overrides under `DataFolder/resources`.
- Added a `mime` package that registers a `conf.AddHook`, reads the YAML at config load, registers its MIME mappings plus explicit `.js` and `.css` types, and exports lossless formats without leading dots.
- Removed the hardcoded MIME definitions from `consts/mime_types.go`.
- Updated model MIME usage to register the hook when used independently, and updated server UI configuration to emit uppercase comma-separated `mime.LosslessFormats`.

Verification:
- `go test ./model ./server/... ./mime` passed.
- `go test ./server/...` passed.
- `go test ./...` built and passed other packages, but the existing `scanner/metadata/taglib` suite failed two M4A gain-tag assertions because the parsed values contain duplicates. `git diff --check` passed.
