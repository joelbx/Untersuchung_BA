VERDICT: FIX

**Code defect:** [VoiceBroadcastPlayback.ts](/app/src/voice-broadcast/models/VoiceBroadcastPlayback.ts:299) can play a chunk through `skipTo()` while its state remains `Paused` or `Buffering`. `getLiveness()` then stays `"grey"` and emits no `LivenessChanged` event during playback. Set the state to `Playing` when seeking starts a chunk, and cover that transition in the existing playback tests.

**Tests:** `./node_modules/.bin/jest --runInBand --watch=false test/voice-broadcast/components/atoms/LiveBadge-test.tsx test/voice-broadcast/components/atoms/VoiceBroadcastHeader-test.tsx test/voice-broadcast/components/molecules/VoiceBroadcastPlaybackBody-test.tsx test/voice-broadcast/models/VoiceBroadcastPlayback-test.ts test/voice-broadcast/utils/VoiceBroadcastChunkEvents-test.ts` — passed: 5 suites, 65 tests, 7 snapshots.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/tsc --noEmit --jsx react` failed at the unchanged [notifications.ts](/app/src/utils/notifications.ts:79): `sendReadReceipt` receives three arguments, but the installed type definition accepts at most two. Resolve that API/type mismatch and rerun the check.

I reviewed the patch without changing project code or tests.