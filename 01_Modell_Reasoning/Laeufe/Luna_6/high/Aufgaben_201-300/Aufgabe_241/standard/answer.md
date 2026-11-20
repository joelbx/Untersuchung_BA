Updated [VoiceBroadcastPreRecordingPip.tsx](/app/src/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip.tsx) to disable Go live immediately, ignore repeat activations until `start()` completes, and guard duplicate device menu openings. Selecting a non-null device closes the menu and updates the header through the audio device selection hook.

Added a regression test for repeated Go live activation in [VoiceBroadcastPreRecordingPip-test.tsx](/app/test/voice-broadcast/components/molecules/VoiceBroadcastPreRecordingPip-test.tsx).

The component test suite passed (7 tests), and ESLint passed for both files.