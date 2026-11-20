I traced the issue, but did not edit project source or tests: the assigned fault-localization role explicitly restricts this turn to inspection. I recorded the findings in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

The likely fix spans:

- [ffmpeg.go](/app/core/ffmpeg/ffmpeg.go:18): add the offset to `Transcode` and `createFFmpegCommand`; replace `%t`, or insert `-ss OFFSET` after the input path when the template lacks it. Preserve current output at offset `0` for templates without `%t`.
- [consts.go](/app/consts/consts.go:92): add `-ss %t` to all three default transcoding commands.
- [media_streamer.go](/app/core/media_streamer.go:21): carry the offset through `NewStream`, `DoStream`, `streamJob`, its cache key, and the FFmpeg call. Without the key change, different offsets can return the same cached audio.
- [stream.go](/app/server/subsonic/stream.go:58) and [handle_streams.go](/app/server/public/handle_streams.go:16): parse `timeOffset` as an integer, default missing or invalid values to `0`, and pass it to `NewStream`. [opensubsonic.go](/app/server/subsonic/opensubsonic.go:9) must advertise the extension.

The download and archive call sites, FFmpeg mock, streamer mock, and existing tests also need the new argument, using `0` where no offset is requested. One scope uncertainty remains: [raw streaming](/app/core/media_streamer.go:71) opens the original file at byte zero; passing an offset through that branch alone would not make raw playback start at the requested time.