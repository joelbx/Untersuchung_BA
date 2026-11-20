# Checkpoint

Issue: pre-recording Go live and device menu interaction consistency.

Implemented: native Go live button with synchronous initiation guard and disabled state until Promise settlement or one event tick for synchronous starts; guarded device-menu opening and non-null device selection; focused interaction tests and updated snapshot.

Verification after final formatting: `./node_modules/.bin/jest test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx --runInBand --silent` passed (10 tests, 1 snapshot); changed-file ESLint passed; changed-file Prettier check passed; `git diff --check` passed.

Repository-wide `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with MatrixClient type errors in `src/components/structures/MatrixChat.tsx:371`, `src/utils/device/clientInformation.ts:80`, and `test/DeviceListener-test.ts:99,192,201`. No errors reported in changed files.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`. No downloads.
