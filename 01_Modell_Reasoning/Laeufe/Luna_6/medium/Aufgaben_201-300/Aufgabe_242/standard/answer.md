Implemented liveness as a mapping from broadcast info state in [determineVoiceBroadcastLiveness.ts](/app/src/voice-broadcast/utils/determineVoiceBroadcastLiveness.ts). Playback controls, position changes, and chunk arrival no longer update liveness independently. Updated the existing test to expect a resumed broadcast to be live.

The focused playback test suite passes: 40 tests.