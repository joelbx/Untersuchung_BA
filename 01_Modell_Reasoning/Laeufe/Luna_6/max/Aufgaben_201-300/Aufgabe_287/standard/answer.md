Implemented album image path tracking across scans and persistence.

- Added `Album.ImageFiles` and an `image_files` migration that forces a full rescan.
- Added [MediaFiles.Dirs()](</app/model/mediafile.go>) and collected image filenames during directory scans.
- Album refresh now builds full image paths and joins them with the system list separator. Changed and deleted folder handling receives the complete directory map.
- Updated the required checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

Verification passed: `go test ./model ./scanner ./persistence`; formatting and diff checks were clean.