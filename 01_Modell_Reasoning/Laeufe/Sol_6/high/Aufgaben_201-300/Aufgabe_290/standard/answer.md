Call sounds now clear `muted` immediately before playback, including when playback has been queued. `AudioID` is exported for ring, ringback, busy, and call-end sounds. The requested public `handleEvent` listener logs media errors with the element ID and gates debug events behind `debug_legacy_call_handler`.

Validation passed: 18 focused tests, TypeScript, ESLint, and `git diff --check`.