# Checkpoint

Task: add album image file tracking across scanning, model, and database migration.

Completed:
- Added `album.image_files` migration and forced full rescan.
- Added `Album.ImageFiles` JSON/structs field and sorted, unique `MediaFiles.Dirs()`.
- Collected image names in directory stats and joined full paths with `filepath.ListSeparator` during album refresh.
- Passed complete filesystem directory map through changed/deleted directory processing, after traversal finishes.
- Removed context from `folderHasChanged`.
- Added tests for directory collection and image path construction.

Verification: `GOPROXY=off GOSUMDB=off go test ./model ./scanner ./db ./persistence` passed. TagLib emitted a C++ deprecation warning during scanner build. `git diff --check` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`. No downloads attempted.
