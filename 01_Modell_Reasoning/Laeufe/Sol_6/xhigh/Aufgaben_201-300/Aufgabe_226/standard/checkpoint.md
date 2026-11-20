# Checkpoint

- Task: load MIME types and lossless extensions from `mime_types.yaml` during startup.
- Initial findings: current registrations and lossless list live in `consts/mime_types.go`; server UI reads `consts.LosslessFormats`.
- Implemented: bundled `resources/mime_types.yaml` with data-folder override, `mime` startup hook, updated UI reference, and removed old constants.
- Verified: `go test ./mime ./model ./server ./core ./server/subsonic ./cmd ./scanner` with module downloads disabled; all passed.
- Final review: no remaining `consts.LosslessFormats` references; `git diff --check` passed.
