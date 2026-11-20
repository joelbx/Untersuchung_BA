# Checkpoint

Task: add `timeOffset` support through FFmpeg transcoding and streaming, update public handlers and OpenSubsonic metadata, then run relevant existing tests.

Completed: FFmpeg and media streamer signatures now carry the integer offset; transcoding cache jobs and keys include it; command templates interpolate `%t` or add `-ss OFFSET` after the input path for nonzero offsets; public handlers default missing/invalid offsets to zero; OpenSubsonic advertises `transcodeOffset` version 1; mocks and call sites were updated.

Validation passed: `GOPROXY=off GOSUMDB=off go test ./core/ffmpeg ./core ./server/public ./server/subsonic`; `git diff --check`. The Go build emitted a TagLib deprecation warning, with all test packages passing.
