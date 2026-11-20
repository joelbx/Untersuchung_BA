Call sounds now unmute their audio element before playback, including queued replays. The four sound IDs are exported as `AudioID`, and the requested [handleEvent listener](/app/src/legacy/LegacyCallHandler/handleEvent.ts) is available for media events.

Verification passed: 15 focused Jest tests, TypeScript, ESLint, and `git diff --check`.