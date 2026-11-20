# Checkpoint

Task: resolve inconsistent voice broadcast liveness feedback in `/app`.

Completed: added `VoiceBroadcastLiveness`, grey badge styling, typed header state, and liveness state/events derived from playback plus info state. Buffering is set immediately when starting playback; the hook subscribes to liveness changes; recording and playback headers now provide the unified state; last-chunk detection is used by playback progression. Updated existing affected fixtures and snapshots.

Verification: all 7 focused voice broadcast test suites passed (64 tests, 10 snapshots); playback model suite passed again after final ordering adjustment. Focused ESLint and LiveBadge stylelint passed. `yarn lint:types` reaches an existing error at `src/utils/notifications.ts:79` (TS2554: 3 arguments supplied where 1-2 are expected); no diagnostics were reported for the changes in this task.
