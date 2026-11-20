# Checkpoint

Task: add timeOffset support across streaming and FFmpeg command generation.

Root cause: public and Subsonic handlers called `NewStream` without an offset; `NewStream`/`DoStream` and `streamJob` had no offset field, so transcoding and cache lookup could only use the start of the file. FFmpeg command construction replaced `%s` and `%b` but not `%t`.

Reproduction: added offset command tests, then ran `go test ./core/ffmpeg -run TestFFmpeg -count=1`; compilation failed because `createFFmpegCommand` accepted only three arguments. This was the expected pre-fix failure.

Patch: carry integer offsets through streaming, cache keys, and Transcode; interpolate `%t` or insert `-ss` after input for custom templates at nonzero offsets; add `%t` to default templates; parse HTTP offsets with invalid and negative values defaulting to zero; advertise the OpenSubsonic extension. Updated mocks and call sites.

Verification: `go test ./core/ffmpeg ./core ./server/public ./server/subsonic ./tests -count=1` passed (exit 0). `git diff --check` passed. Local TagLib compiler emitted a deprecation warning during Go tests; it did not fail the run.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local grep/find. No downloads or external research.
