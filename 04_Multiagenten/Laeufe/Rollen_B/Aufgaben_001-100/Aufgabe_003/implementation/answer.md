Implemented `timeOffset` through the streaming and transcoding call chain. FFmpeg now replaces `%t` in command templates or inserts `-ss OFFSET` after the input path when needed. Transcoding cache keys distinguish offsets, both streaming endpoints parse the parameter with a default of `0`, and OpenSubsonic advertises support.

The relevant local tests pass: `go test ./core/ffmpeg ./core ./server/subsonic ./server/public`.

**Limitation:** streams served directly from the original file still open at byte zero; the offset takes effect on FFmpeg transcoded streams.