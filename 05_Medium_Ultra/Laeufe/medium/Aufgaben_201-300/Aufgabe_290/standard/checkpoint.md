# Checkpoint

Task: Fix muted call notification sounds and expose the public media event listener.
Status: Complete. Call playback clears `muted` before `play()` for ring, ringback, busy, and call-end. `AudioID` is exported, and `handleEvent(e: Event)` is available at the specified path.
Verification: LegacyCallHandler tests (17 passed); handleEvent tests (2 passed); TypeScript no-emit check, targeted ESLint, and git diff check passed.
Constraints observed: Local code and existing dependencies only; git history, index, and harness configuration untouched.
