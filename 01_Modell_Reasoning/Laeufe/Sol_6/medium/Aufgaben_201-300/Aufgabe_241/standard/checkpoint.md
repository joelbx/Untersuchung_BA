Task: Resolve pre-recording Go live and device selection interaction consistency.
Status: Complete. Updated VoiceBroadcastPreRecordingPip to render a native Go live button, disable it immediately, guard repeated initiation, and restore it after promise settlement or one tick for synchronous starts. Device selection remains anchored to the root and uses the selected MediaDeviceInfo; repeated microphone activation keeps one menu open.
Verification: Focused Jest suite passed (12 tests, 1 snapshot). ESLint and Prettier checks passed on edited files. Repository-wide tsc reports existing unrelated MatrixClient type errors in MatrixChat.tsx, clientInformation.ts, and DeviceListener-test.ts.
Constraints observed: local code/tests only; git history, index, and harness configuration untouched.
