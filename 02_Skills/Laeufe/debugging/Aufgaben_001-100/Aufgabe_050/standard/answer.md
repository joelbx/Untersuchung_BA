Fixed the NULL scan failures for `image_files` and the affected album, artist, and share timestamps. The model fields now represent absent values with pointers; reads use `gg.V`, and timestamp assignments use `gg.P`. Added regression tests for NULL scans and the new helpers.

The affected package tests passed, and `go test ./... -run '^$'` passed as a repository-wide compile check.