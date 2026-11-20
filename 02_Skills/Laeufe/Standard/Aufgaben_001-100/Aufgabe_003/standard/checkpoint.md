# Checkpoint

Implemented `timeOffset` propagation through public and Subsonic stream handlers, MediaStreamer, transcoding cache keys, and FFmpeg command generation. Updated templates, mocks, and tests.

Verification:
- `go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./server/subsonic/responses && git diff --check` passed.
- `go test ./...` failed only in `scanner/metadata/taglib`: `taglib_test.go:34` expected 2 fixture files but found 3, `taglib_test.go:85` expected one replay gain value but found two, and `taglib_test.go:143` expected an unreadable-file error but got nil. These are unrelated fixture/permission failures; no changes were made in that package. This leaves the full suite failing in this environment.
- Initial `rg` command failed with `/bin/bash: rg: command not found`; used `grep` instead.
