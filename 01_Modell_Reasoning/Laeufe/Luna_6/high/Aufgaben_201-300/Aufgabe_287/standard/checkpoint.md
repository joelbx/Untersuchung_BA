# Checkpoint

Task: resolve album image path tracking in `/app`.

Implemented:
- Added sorted, de-duplicated `MediaFiles.Dirs()`.
- Stored discovered image names in directory scan stats.
- Added `Album.ImageFiles` and album refresh path construction using `filepath.Join` and `filepath.ListSeparator`.
- Deferred changed-directory processing until traversal completes so refreshers receive the complete directory map; passed that map through changed/deleted processing.
- Added a migration for `album.image_files` that forces a full media rescan.

Verification: `go test ./model ./scanner ./persistence ./db/migration` passed; `git diff --check` passed.
