# Checkpoint

Implemented `timeOffset` support across FFmpeg command generation, transcoding, stream job caching, public shared streams, and Subsonic `/stream`. Built-in transcoding templates use `-ss %t`; commands without the placeholder insert `-ss OFFSET` after the input path only for nonzero offsets. Other stream callers pass zero, and OpenSubsonic advertises `transcodeOffset` version 1.

Updated streamer and FFmpeg test mocks/call sites to the new signatures.

Verification: `go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests` passed. `git diff --check` passed.
