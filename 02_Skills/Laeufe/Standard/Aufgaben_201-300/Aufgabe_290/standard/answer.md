Call sounds now clear an element’s `muted` state before each playback attempt. The four sound IDs are publicly exported, and the requested [handleEvent listener](/app/src/legacy/LegacyCallHandler/handleEvent.ts) is available for media elements.

The call handler tests passed (14 tests), as did TypeScript, ESLint, and `git diff --check`.