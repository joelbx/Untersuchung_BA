# Checkpoint

Task: externalize MIME types and lossless audio formats into `mime_types.yaml`, initialize MIME mappings at startup, and update server references.

Completed: removed the hardcoded MIME definitions from `consts/mime_types.go`; added the embedded `mime/mime_types.yaml` configuration with `types` and `lossless`; registered the configured mappings and explicit `.js`/`.css` mappings from a `conf.AddHook`; changed the server UI configuration to read `mime.LosslessFormats` and render it uppercase and comma-separated.

Verification: `go test ./server ./mime` passes.
