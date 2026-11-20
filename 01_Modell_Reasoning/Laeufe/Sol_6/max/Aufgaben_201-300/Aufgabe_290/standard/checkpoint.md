# Checkpoint

Completed: `LegacyCallHandler.play` now clears `audio.muted` immediately before playback, including queued replays. `AudioID` is exported from the handler and a dedicated module. Added the requested `handleEvent` listener and registered `debug_legacy_call_handler` with a disabled default. Existing and new focused Jest tests pass (20 tests); TypeScript, ESLint, and `git diff --check` pass.
