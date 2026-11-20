Album image paths are now collected during directory scans, combined into full paths, and saved in the new `image_files` album field. The migration adds the column and triggers a full media rescan. `MediaFiles.Dirs()` returns sorted, unique directory paths.

The relevant tests passed: `go test ./scanner ./model ./db/migration`.