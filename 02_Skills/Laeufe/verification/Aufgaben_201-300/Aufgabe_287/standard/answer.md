Album scans now collect image filenames and persist their full paths in the new `image_files` column. `MediaFiles.Dirs()` returns sorted, unique directories, and the migration triggers a full media rescan.

Verification: `git diff --check` and `GOPROXY=off GOSUMDB=off go test ./model ./scanner ./db/...` passed.