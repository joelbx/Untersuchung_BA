Call sound playback now unmutes a muted audio element immediately before `play()`, and the sound ID enum is publicly exported from [LegacyCallHandler.tsx](/app/src/LegacyCallHandler.tsx:75).

Added the requested `handleEvent` listener in [handleEvent.ts](/app/src/legacy/LegacyCallHandler/handleEvent.ts), with structured error logs and debug logs gated by `debug_legacy_call_handler`.

Verification passed: the existing legacy call handler suite (9 tests), targeted ESLint, and `git diff --check`.