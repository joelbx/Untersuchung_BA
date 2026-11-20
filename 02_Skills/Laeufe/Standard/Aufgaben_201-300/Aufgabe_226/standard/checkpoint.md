# Checkpoint

Task: load MIME mappings and lossless formats from `mime_types.yaml` during configuration initialization.

Implemented:
- Added `resources/mime_types.yaml` with the former audio/image mappings and lossless extensions. Operators can override it at `<DataFolder>/resources/mime_types.yaml` through the existing resources filesystem.
- Added `mime` package loader, registered with `conf.AddHook`. It registers all configured types, derives sorted extension names for `LosslessFormats`, and explicitly sets `.js` and `.css`.
- Removed `consts/mime_types.go`; updated the server UI configuration and ensured model file classification imports the initializer.
- Added focused loader tests and a startup assertion in the server UI test.

Checks:
- `GOPROXY=off GOTOOLCHAIN=local go test ./mime ./model ./core/... ./server/...` passed.
- `git diff --check` passed.
- `GOPROXY=off GOTOOLCHAIN=local go test ./...` failed in `scanner/metadata/taglib`: two existing AAC gain-tag tests (`Correctly parses m4a (aac) gain tags` and uppercase variant) expect one `replaygain_album_gain` value, but local TagLib returns two duplicate `0.37` values. Other packages passed. This behavior is outside the MIME loading changes.

Tooling: `rg` is unavailable; local searches used `grep` and `find`. No dependencies were downloaded.
