Implemented album image tracking. Directory scans now collect image names, `MediaFiles.Dirs()` returns sorted unique directories, and album refresh stores the full image paths in `Album.ImageFiles`. A database migration adds `album.image_files` and triggers a full media rescan.

`GOPROXY=off go test ./model ./scanner ./db ./persistence` and `git diff --check` passed.