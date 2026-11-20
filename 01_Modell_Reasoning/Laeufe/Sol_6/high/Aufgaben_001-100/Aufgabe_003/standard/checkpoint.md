# Checkpoint

Task: add `timeOffset` support across FFmpeg transcoding and media streaming.

Status: implemented and verified.

- Added offset arguments through stream and transcode interfaces, call sites, and mocks.
- Updated FFmpeg templates and command interpolation/fallback; cache keys distinguish nonzero offsets while preserving the zero-offset key.
- Parsed `timeOffset` in shared and Subsonic stream handlers, defaulting missing, invalid, and negative values to zero; advertised the `transcodeOffset` extension.
- Added command, cache, and endpoint tests. Relevant Go package tests pass with `GOTOOLCHAIN=local GOPROXY=off`.
