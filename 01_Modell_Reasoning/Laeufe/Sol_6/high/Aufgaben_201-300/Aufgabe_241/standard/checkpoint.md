# Checkpoint

Task: Make the voice broadcast pre-recording controls robust under repeated activation and complete device selection.

Status: Complete. `VoiceBroadcastPreRecordingPip` now renders a native Go live button with a synchronous initiation guard and a disabled state until the start attempt settles (or one event tick for a synchronous result). The device menu has an open guard; selecting a device closes it and updates the header label through the existing audio-device hook.

Verification: Pre-recording and header Jest suites pass (16 tests, 5 snapshots). ESLint, Prettier, and `git diff --check` pass. The repository-wide TypeScript check still reports five errors in unrelated `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts` files.
