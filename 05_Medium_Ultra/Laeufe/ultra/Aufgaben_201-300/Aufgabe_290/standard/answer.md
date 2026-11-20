Fixed call sound playback in [LegacyCallHandler.tsx](/app/src/LegacyCallHandler.tsx): ring, ringback, busy, and call-end audio now unmute immediately before each `play()` attempt, including queued replays. `AudioID` is exported for consistent use elsewhere.

Added the public [handleEvent listener](/app/src/legacy/LegacyCallHandler/handleEvent.ts) with structured error logging and debug logging controlled by the new setting. I delegated the code and test audit and the listener implementation, then reviewed the combined patch.

Verification passed: 20 tests across three focused suites, TypeScript, targeted ESLint, and `git diff --check`.