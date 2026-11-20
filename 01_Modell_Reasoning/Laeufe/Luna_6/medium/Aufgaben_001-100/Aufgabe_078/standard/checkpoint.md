# Voice broadcast liveness issue

- Implemented the `VoiceBroadcastLiveness` union, grey badge styling, typed header props, and updated every header caller.
- Playback now derives liveness from broadcast info and playback states, emits `LivenessChanged` only on transitions, and the playback hook exposes it.
- Added final chunk detection and used it when handling chunk completion.
- Updated header test fixtures for the typed API.
- Verification: focused Jest run passed (4 suites, 51 tests, 3 snapshots); `git diff --check` passed.
- TypeScript check was attempted but reports an unrelated existing error at `src/utils/notifications.ts:79` (`Expected 1-2 arguments, but got 3`).
