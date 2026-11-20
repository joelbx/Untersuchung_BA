# Checkpoint

Task: resolve voice broadcast liveness feedback inconsistency.

Completed: unified liveness type and header prop; grey badge styling; playback liveness state and change event tied to playback/info transitions; hook exposure; recording and playback callsite updates; last chunk detection; relevant snapshots updated.

Verification: all 24 voice-broadcast test suites pass (209 tests); changed TypeScript files pass ESLint; LiveBadge stylesheet passes Stylelint. `yarn lint:types` is blocked by an existing error in unmodified `src/utils/notifications.ts:79` (TS2554).
