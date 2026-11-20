Implemented `timeOffset` propagation through `Transcode`, `NewStream`, and `DoStream`. FFmpeg templates now use `-ss %t`; templates without that placeholder get `-ss OFFSET` after the input path for nonzero offsets. Transcoding cache keys include the offset.

Subsonic and shared stream handlers parse `timeOffset`, defaulting invalid or missing values to 0. The OpenSubsonic response advertises `transcodeOffset` v1. Updated mocks and call sites.

Verification passed: `go test ./core/ffmpeg ./core ./server/subsonic/... ./server/public` and `git diff --check`. The build emitted a TagLib deprecation warning.