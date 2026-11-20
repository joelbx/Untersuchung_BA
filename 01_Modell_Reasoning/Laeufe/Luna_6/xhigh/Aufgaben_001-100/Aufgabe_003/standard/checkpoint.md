# Checkpoint: streaming timeOffset support

- Task: thread an integer time offset (seconds) through FFmpeg transcoding and media streaming, including public handlers and extension support.
- Initial state: working tree was clean; no `AGENTS.md` files found in the repository tree.
- Implemented: FFmpeg `%t` interpolation and nonzero fallback insertion immediately after the input path; built in transcoding templates include `-ss %t`; `Transcode`, `NewStream`, and `DoStream` carry the offset; stream cache keys include it; HTTP stream and single media download handlers parse `timeOffset` with a zero default; OpenSubsonic reports `transcodeOffset` v1; mocks and existing call sites updated.
- Verification: `go test ./core/ffmpeg ./core ./server/subsonic/... ./server/public` passed. `git diff --check` passed. The test build emitted a preexisting TagLib deprecation warning.
