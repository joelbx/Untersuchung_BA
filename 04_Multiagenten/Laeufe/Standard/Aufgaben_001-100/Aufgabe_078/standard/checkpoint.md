Task: Fix voice broadcast liveness UI and playback state.
Status: Completed implementation and verification.
Changes: Added VoiceBroadcastLiveness type, grey LiveBadge style, header and call-site mapping, playback liveness state/events, hook subscription, and VoiceBroadcastChunkEvents.isLast. Added transition and UI tests; updated playback body snapshots.
Verification: 24 voice-broadcast test suites passed (217 tests, 15 snapshots). ESLint and stylelint passed for changed files; git diff --check passed. Full TypeScript check is blocked by an existing error in untouched src/utils/notifications.ts:79 (TS2554, expected 1-2 arguments but got 3).
