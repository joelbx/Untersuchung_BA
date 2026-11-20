Updated call sound playback to clear `muted` before `play()` for ring, ringback, busy, and call-end sounds, including queued replays. Exported `AudioID` and added the requested public `handleEvent` listener.

Verification passed: 15 relevant Jest tests, TypeScript, ESLint on changed files, and `git diff --check`.