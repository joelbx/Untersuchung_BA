# Checkpoint

Task: load MIME mappings and lossless formats from `mime_types.yaml` at startup.

Status: implementation complete. Added `resources/mime_types.yaml` (embedded default, operator override at `<DataFolder>/resources/mime_types.yaml`), a `conf.AddHook` loader in `mime`, and `mime.LosslessFormats`. Removed `consts/mime_types.go`; UI reads the loaded list.

TDD: observed red tests for custom runtime mapping, lossless list, UI output, JS/CSS override, and missing required YAML fields before implementing each behavior. Focused tests `GOPROXY=off GOSUMDB=off go test ./mime ./cmd ./model ./server -count=1` pass.

Full suite: `GOPROXY=off GOSUMDB=off go test ./...` exits 1. All packages pass except `scanner/metadata/taglib`: `Correctly parses m4a (aac) gain tags` and `Correctly parses m4a (aac) gain tags (uppercase)` expect one `replaygain_album_gain` value but receive `["0.37", "0.37"]`. This package's parser and test were not edited; these failures appear unrelated to the MIME change. This uncertainty remains because a baseline checkout was not run.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
