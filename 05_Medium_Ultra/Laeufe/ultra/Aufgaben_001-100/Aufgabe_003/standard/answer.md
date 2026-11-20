Implemented `timeOffset` for transcoded streams. FFmpeg now handles `%t` and legacy commands, the streamer passes offsets through and uses separate cache entries, and the public and Subsonic stream handlers default missing or invalid values to 0. Call sites, mocks, tests, and the OpenSubsonic extension response were updated.

Three subagents worked on FFmpeg, core streaming, and endpoints; I integrated their changes. The relevant Go tests, `git diff --check`, and `gofmt` checks passed.

Direct raw-file streams still use HTTP byte-range seeking; `timeOffset` applies to transcoded streams.