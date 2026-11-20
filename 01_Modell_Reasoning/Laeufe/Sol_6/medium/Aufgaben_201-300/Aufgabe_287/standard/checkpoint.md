# Checkpoint

Task: persist all album image paths gathered during scans, expose them on the album model, and cover incremental scans and deletions.

Status: complete. Added album `image_files` migration with forced full rescan; exposed `ImageFiles` on `Album`; added sorted, unique `MediaFiles.Dirs`; collected image filenames during traversal; propagated the complete directory map through changed/deleted directory refreshes; and populated album image paths before persistence. `folderHasChanged` now takes only folder statistics, database directories, and timestamp.

Verification: `GOPROXY=off go test ./model ./scanner ./db ./persistence` passed. `git diff --check` passed.
