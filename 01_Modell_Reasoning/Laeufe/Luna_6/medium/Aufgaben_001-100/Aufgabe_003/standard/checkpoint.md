# Checkpoint

Task: add integer-second `timeOffset` support through FFmpeg transcoding and HTTP streaming endpoints.

Initial state: repository at `/app`; no `rg` executable is available, so repository searches use `find`/`grep`.

Plan: inspect FFmpeg templates and stream call sites, update signatures/call sites/cache key/request parsing/OpenSubsonic extension metadata, then run relevant existing tests.

Implementation completed:
- Added integer-second offsets to FFmpeg transcoding, media streamer APIs, cache keys, and HTTP streaming entry points.
- Added `%t` to default FFmpeg transcoding templates and fallback `-ss OFFSET` insertion for custom templates.
- Public and Subsonic stream handlers parse `timeOffset` as an integer and default invalid/missing values to 0; downloads and archive streams pass 0.
- Advertised the `timeOffset` OpenSubsonic extension (version 1).

Verification: `go test ./core/ffmpeg ./core ./server/public ./server/subsonic` passed. `go test ./...` exercised the repository but failed in existing `scanner/metadata/taglib` tests (fixture enumeration, duplicate replaygain tags, and unreadable-file permission behavior); changed packages passed. `git diff --check` passed.
