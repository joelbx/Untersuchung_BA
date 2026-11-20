# Checkpoint

Task: album image file path tracking during scans, including migration and rescan.
Status: implementation complete; focused packages pass.

## Changes
- Album stores and exposes `image_files` / `imageFiles`.
- MediaFiles.Dirs returns sorted unique parent directories.
- Folder traversal collects image names; refresher joins full paths using `filepath.ListSeparator`.
- Scanner passes the complete filesystem directory map to changed/deleted folder refreshes and processes changes after traversal.
- Migration adds `album.image_files` and calls `forceFullRescan`.

## Verification
- RED: `GOPROXY=off go test ./model ./scanner` failed because Dirs, ImageFiles, and albumImageFiles were absent.
- GREEN: `GOPROXY=off go test ./model ./scanner ./persistence ./db/migration` passed.
- Full suite: `GOPROXY=off go test ./...` failed only in `scanner/metadata/taglib`: `Extractor Parse / correctly parses metadata from all files in folder` expected 2 files but got 3, and `Extractor Error Checking / correctly handle unreadable file due to insufficient read permission` expected an error but got nil. The fixture `test_no_read_permission.ogg` is readable to this root-run environment; these failures are unrelated to the patch. The full suite therefore cannot be claimed green.
- C++ TagLib emits an existing deprecation warning for `AudioProperties::length()`.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
