Added `timeOffset` support through the public and Subsonic stream handlers, media streamer, transcoding cache, and FFmpeg command builder. Missing or invalid HTTP values default to `0`; archive and download calls pass `0`. Updated the mocks, tests, and OpenSubsonic extension response.

The relevant Go package tests and `git diff --check` passed.