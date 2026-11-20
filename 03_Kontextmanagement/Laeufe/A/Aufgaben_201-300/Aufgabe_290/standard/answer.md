Call sounds now unmute their audio element before each playback attempt, including replay. The four sound IDs are publicly exported, and the requested `handleEvent` listener logs media errors with the element ID and gates debug events behind the setting.

Verification passed: 17 focused tests, TypeScript type checking, ESLint, and `git diff --check`.