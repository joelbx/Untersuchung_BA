# Checkpoint

Task: add timeOffset support through streaming and FFmpeg command creation.
Status: implementation complete; focused tests pass.

TDD red: `GOPROXY=off go test ./core/ffmpeg ./core -run 'TestFFmpeg|TestMediaStreamer' -count=1` failed as expected because `createFFmpegCommand` lacked a fourth argument and `streamJob` lacked `timeOffset`.

Verification: `GOPROXY=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests -run 'TestFFmpeg|TestMediaStreamer' -count=1` passed. `git diff --check` passed.

Full suite: `GOPROXY=off go test ./...` failed only in `scanner/metadata/taglib` (`TestTagLib`): `correctly parses metadata from all files in folder` (got 3 files, expected 2), `Correctly parses m4a (aac) gain tags` (duplicate gain value), and `correctly handle unreadable file due to insufficient read permission` (got nil error). This leaves the full suite red; the TagLib tests are unrelated to the streaming patch and appear sensitive to this environment's fixtures, library behavior, and root file access. The C++ TagLib deprecation warning also appeared.

Tooling: `rg` unavailable; used `grep` and `find`. No dependencies downloaded.
