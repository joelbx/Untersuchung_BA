Implemented in [VoiceBroadcastPreRecordingPip.tsx](/app/src/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip.tsx). “Go live” now uses a native disabled button and a handler lock to prevent repeated starts until the attempt settles, or one event tick for a synchronous start. Device selection accepts a non-null device, closes the anchored menu, and updates the displayed label through the audio-device hook. The close handler remains independent of the start lock.

Updated the component snapshot.

Validation: focused suite passed (6 tests); ESLint, Prettier, and `git diff --check` passed. The repository TypeScript check reports five errors in unrelated MatrixClient API usage in `MatrixChat.tsx`, `clientInformation.ts`, and `DeviceListener-test.ts`.