# Checkpoint

Implemented album image path tracking across scanning and persistence.

- Directory stats now retain image file names; scans pass the complete directory map into changed/deleted directory refreshes.
- `MediaFiles.Dirs()` returns sorted unique containing directories, and album refresh joins full image paths with the platform list separator.
- Added `album.image_files` and a migration that forces a full media rescan.
- Verification: `go test ./model ./scanner ./persistence ./db/migration` passed; `git diff --check` passed.
