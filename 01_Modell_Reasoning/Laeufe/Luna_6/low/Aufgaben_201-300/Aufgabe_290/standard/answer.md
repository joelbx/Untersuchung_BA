Updated [LegacyCallHandler.tsx](/app/src/LegacyCallHandler.tsx) to unmute the audio element immediately before playback, and exported `AudioID` so call sound identifiers are publicly accessible. Setting `muted` to `false` is safe for elements that are already unmuted.

The existing `LegacyCallHandler` tests passed: 9 tests across 1 suite.