Album artwork paths are now collected during scans and saved in the new `image_files` column. The [Album model](/app/model/album.go) exposes them, and the migration triggers a full media rescan to populate existing albums. `MediaFiles.Dirs()` returns sorted, unique directories.

The model, scanner, database, and persistence tests pass.