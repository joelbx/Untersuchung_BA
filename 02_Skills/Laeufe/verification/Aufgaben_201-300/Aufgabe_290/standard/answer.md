Call sounds now unmute their audio element immediately before playback, including when playback was queued. I also exported the ring, ringback, busy, and call-end IDs and added the specified [media event listener](/app/src/legacy/LegacyCallHandler/handleEvent.ts).

Verification passed: 16 targeted tests, TypeScript, ESLint, and `git diff --check`.