MIME types and lossless formats now load at startup from [mime_types.yaml](/app/resources/mime_types.yaml). The server uses the loaded lossless list for its uppercase, comma-separated UI setting. Operators can override the file in the data folder’s `resources` directory.

Verified with `go test ./mime ./model ./server ./core` and `git diff --check`.