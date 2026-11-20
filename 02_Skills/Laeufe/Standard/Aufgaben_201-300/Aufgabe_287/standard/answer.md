Implemented album image file tracking. The scanner now collects image names from each directory, and album refreshes store their full paths in `Album.ImageFiles`. A database migration adds `image_files` and triggers a full media rescan.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./model ./scanner ./db ./persistence` and `git diff --check`.