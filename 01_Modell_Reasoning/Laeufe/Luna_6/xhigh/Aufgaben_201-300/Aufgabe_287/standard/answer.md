Implemented album image file tracking.

- Added `Album.ImageFiles` and a migration that adds `album.image_files` and forces a full rescan.
- Added sorted, de-duplicated `MediaFiles.Dirs()` and collected image filenames during directory scans.
- Album refresh now joins image paths from all relevant directories using the system list separator. Changed folders are processed after traversal so refreshes see the complete directory map.

Validation passed: `go test ./model ./scanner ./persistence` and `git diff --check`. The scanner build emitted a TagLib deprecation warning.