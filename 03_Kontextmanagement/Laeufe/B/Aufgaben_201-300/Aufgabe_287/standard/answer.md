Implemented album image tracking. Scans now collect image names, album refreshes assemble full paths from the media directories, and the album model exposes and persists them. The new migration adds `image_files` and triggers a full rescan.

`go test ./model ./scanner ./db ./persistence` passed.