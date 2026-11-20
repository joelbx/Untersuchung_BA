Implemented call sound recovery: muted audio elements are unmuted immediately before playback, and the four sound IDs are now publicly exported in [LegacyCallHandler.tsx](/app/src/LegacyCallHandler.tsx:74).

Added the exported media event listener in [handleEvent.ts](/app/src/legacy/LegacyCallHandler/handleEvent.ts:46). It logs media errors with the element ID, and logs recognized media events only when the device-only debug setting is enabled. That setting is registered in [Settings.tsx](/app/src/settings/Settings.tsx:1066).

Validation passed: the existing legacy call handler tests (9 tests), ESLint on changed source files, TypeScript compilation, and `git diff --check`.