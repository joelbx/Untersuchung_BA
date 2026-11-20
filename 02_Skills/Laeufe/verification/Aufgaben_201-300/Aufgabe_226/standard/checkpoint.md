# Checkpoint

Task: externalize MIME types and lossless formats into `resources/mime_types.yaml`.

Changes: removed `consts/mime_types.go`; added a MIME loader registered through `conf.AddHook`, using the embedded resource with the DataFolder/resources overlay; updated UI and model MIME references; added loader and UI tests.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./mime ./model ./server ./core ./conf` passed after the loader test's text MIME expectation was corrected.
- `GOTOOLCHAIN=local GOPROXY=off go test ./...` failed in two existing `scanner/metadata/taglib` m4a gain tag assertions. Both expected `replaygain_album_gain: ["0.37"]` and received `["0.37", "0.37"]`; the TagLib package has no MIME registration references.
- `git diff --check` passed.

Remaining: run final targeted tests after the UI test update, then report the full-suite limitation.
- Final `GOTOOLCHAIN=local GOPROXY=off go test -count=1 ./mime ./model ./server ./core ./conf` passed (mime, model, server, core; conf has no tests).
- Final `git diff --check` passed.

Status: implementation and targeted verification complete. Full-suite TagLib failures remain as recorded above.
