Implemented local artist image discovery. Each album can now return its unique media directories, and artist image lookup checks those directories for `artist.*` before falling back to existing image sources. Artwork source traces now include each attempt’s elapsed time.

Verified with `go test ./core/artwork ./model` (passed).