Implemented runtime MIME configuration using embedded [mime_types.yaml](/app/mime/mime_types.yaml). A `conf.AddHook` loads its mappings and lossless extensions at startup, with explicit `.js` and `.css` registrations. The server UI now uses `mime.LosslessFormats` for its uppercase, comma-separated value.

Removed the hardcoded definitions from `consts/mime_types.go`.

Verification passed: `go test ./server ./mime`.