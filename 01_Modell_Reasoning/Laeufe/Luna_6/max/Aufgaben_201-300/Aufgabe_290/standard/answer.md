Implemented the call sound fix. Playback now unmutes each element immediately before `play()` and leaves already-unmuted elements unchanged. The existing sound ID enum is exported, and the requested `handleEvent` listener and default-off debug setting are available.

Verification passed: 9 legacy call handler tests, TypeScript checks, ESLint on changed TypeScript files, and `git diff --check`.

- [LegacyCallHandler.tsx](/app/src/LegacyCallHandler.tsx:74)
- [handleEvent.ts](/app/src/legacy/LegacyCallHandler/handleEvent.ts:39)
- [Settings.tsx](/app/src/settings/Settings.tsx:1077)