Implemented album artwork path tracking. Directory scans now collect image names; album refresh combines them with sorted, unique media directories and stores the full paths in the new `image_files` field. The migration adds the column and triggers a full media rescan.

Verified with `go test ./scanner ./model ./persistence` and `git diff --check`.