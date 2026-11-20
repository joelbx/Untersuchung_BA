# Checkpoint

Task: resolve inconsistent voice broadcast liveness feedback in `/app`.

Implemented:
- Added `VoiceBroadcastLiveness` (`live`, `grey`, `not-live`) and wired the header, recording call sites, playback hook, and playback body to use it.
- Added the grey badge styling and `LiveBadge.grey` prop.
- Added derived playback liveness and deduplicated `LivenessChanged` events on playback and info state changes.
- Added `VoiceBroadcastChunkEvents.isLast()` and used it to identify playback completion.
- Updated existing UI tests and snapshots for the new typed values and visual states.

Verification:
- Relevant voice broadcast Jest suites: 5 passed, 56 tests passed, 7 snapshots passed.
- ESLint for changed TypeScript files passed.
- Stylelint for the changed badge stylesheet passed; `git diff --check` passed.
- TypeScript check is blocked by a pre-existing error at `src/utils/notifications.ts:79` (`Expected 1-2 arguments, but got 3`); no issue-related type errors remain after updating the header test API.

No external research or downloads were used.
