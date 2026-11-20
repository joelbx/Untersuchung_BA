# Checkpoint

Issue: Load MIME types and lossless audio extensions from `mime_types.yaml` at application startup.

Completed:
- Added `resources/mime_types.yaml` with all previous audio/image mappings and the lossless extension list.
- Added a `mime` package that loads the resource from the embedded/overridable resource filesystem during a `conf.AddHook`, registers all configured extensions plus explicit `.js` and `.css`, and publishes `LosslessFormats` without leading periods.
- Removed `consts/mime_types.go`, updated the UI config and its existing test to use `mime.LosslessFormats`, and imported the loader where model MIME classification is used.

Verification:
- `go test ./server ./mime` passed.
- `go test ./model ./core` passed.
- `go test ./scanner ./cmd` passed (`cmd` has no test files).
- `git diff --check` passed.
