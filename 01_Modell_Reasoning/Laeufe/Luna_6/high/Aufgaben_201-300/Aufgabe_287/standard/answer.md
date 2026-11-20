Implemented album image path tracking and persistence.

- Added sorted, deduplicated `MediaFiles.Dirs()` and exposed `Album.ImageFiles`.
- Folder scans now retain image names; album refreshes join them to media directories using the system list separator.
- Changed folders are processed after traversal so refreshes receive the complete directory map, including during deletions.
- Added a migration for `album.image_files` that triggers a full media rescan.

Verified with `go test ./model ./scanner ./persistence ./db/migration` and `git diff --check`.