# Checkpoint

- Task: ensure legacy call notification sounds unmute before playback and expose stable sound identifiers.
- Status: complete. Playback clears `muted` immediately before `play()`; sound IDs are exported. Added the media event listener and its debug setting, plus focused tests.
- Verification: targeted Jest suites passed (17 tests); ESLint, TypeScript, and `git diff --check` passed.
