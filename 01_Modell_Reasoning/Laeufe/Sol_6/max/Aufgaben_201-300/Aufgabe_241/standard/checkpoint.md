# Voice broadcast pre-recording interaction fix

Status: implementation and focused verification complete.

Changes: Go live uses a native disabled button and a synchronous single-flight guard, resetting after Promise settlement or one event tick for a synchronous start. The microphone line opens one menu at a time; selection closes it and updates the header through the audio-device selection hook. The close control has an accessible label.

Verification: 4 relevant Jest suites pass (34 tests, 5 snapshots); ESLint, Prettier, and `git diff --check` pass. Full `tsc --noEmit --jsx react` reports existing unrelated MatrixClient type errors in MatrixChat, clientInformation, and DeviceListener tests, with no errors in changed files.
