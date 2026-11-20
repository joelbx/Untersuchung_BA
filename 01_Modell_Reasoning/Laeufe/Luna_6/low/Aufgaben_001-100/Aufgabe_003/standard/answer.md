Implemented `timeOffset` propagation through FFmpeg transcoding, streaming, and the public and Subsonic stream endpoints. Transcoding cache keys now include the offset, and OpenSubsonic advertises the `timeOffset` extension.

Verified with `go test ./core/ffmpeg ./core ./server/public ./server/subsonic` and `git diff --check`; all passed.