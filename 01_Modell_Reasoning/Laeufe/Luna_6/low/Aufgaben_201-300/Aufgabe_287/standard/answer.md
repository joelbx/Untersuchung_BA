Implemented album image path tracking across the model, database, and scanner.

- Added `Album.ImageFiles` and the `album.image_files` migration, which triggers a full media rescan.
- Added `MediaFiles.Dirs()` to return sorted, unique containing directories.
- Directory scan stats now retain image file names. Album refresh combines them with directory paths and joins the full paths using `filepath.ListSeparator`.
- The scanner passes the complete directory map to refreshes and `folderHasChanged` no longer takes a context.

Verified with `go test ./model ./scanner ./db/migration ./persistence` and `git diff --check`.