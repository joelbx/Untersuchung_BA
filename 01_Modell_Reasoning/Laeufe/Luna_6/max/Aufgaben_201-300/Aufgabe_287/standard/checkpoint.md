# Checkpoint

Task: add album image path tracking from directory scans through persistence, expose media-file directory paths, and update scan refresh/change handling per the issue requirements.

Implementation complete:
- Added `Album.ImageFiles` mapped to `album.image_files`, plus a migration that calls `forceFullRescan`.
- Added sorted, duplicate-free `MediaFiles.Dirs()`.
- Directory statistics now retain image filenames while preserving the existing image/playlist/audio indicators.
- Album refresh assembles full artwork paths with `filepath.Join`, separated by `filepath.ListSeparator`.
- Changed folders are processed after the full filesystem directory map is collected; the map flows through changed/deleted folder handling and album refresh.
- Removed context from the folder change predicate.

Verification: `go test ./model ./scanner ./persistence` passed. `git diff --check` and `gofmt -d` reported no issues.
