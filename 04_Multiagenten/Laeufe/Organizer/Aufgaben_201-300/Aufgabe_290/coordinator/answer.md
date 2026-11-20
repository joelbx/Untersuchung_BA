Call sounds now unmute their audio element immediately before playback, including queued playback after a reload. The four sound IDs are exported as `AudioID`, and the requested `handleEvent` listener is available at [handleEvent.ts](/app/src/legacy/LegacyCallHandler/handleEvent.ts).

Verification passed: 17 focused tests, TypeScript, ESLint, and `git diff --check`. No delegation was used.