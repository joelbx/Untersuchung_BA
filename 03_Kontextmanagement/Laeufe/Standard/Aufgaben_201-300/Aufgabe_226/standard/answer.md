MIME types and lossless formats now load from [mime_types.yaml](/app/resources/mime_types.yaml) during startup. The file can be overridden in the configured data folder’s `resources` directory. The UI uses the loaded lossless formats, and the hardcoded definitions in `consts/mime_types.go` are removed.

Verified with `go test ./mime ./server ./model ./core ./cmd` and `git diff --check`.