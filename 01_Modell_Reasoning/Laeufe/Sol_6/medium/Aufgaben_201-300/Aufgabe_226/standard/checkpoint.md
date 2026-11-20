# Checkpoint

Task: load MIME mappings and lossless formats from `mime_types.yaml` at startup.
Status: complete. Added the YAML to embedded resources, loaded it through the resource overlay with a `conf.AddHook` initializer, moved lossless formats to `mime.LosslessFormats`, and updated the server UI configuration. Removed `consts/mime_types.go`.
Verification: `go test ./mime ./server ./core ./server/subsonic ./conf`, `go test ./cmd`, and `git diff --check` passed.
