# Checkpoint

Resolved the muted call sound path in `src/LegacyCallHandler.tsx` by unmuting immediately before each queued playback attempt. Exported `AudioID` for stable sound identifiers. Added the public media event listener at `src/legacy/LegacyCallHandler/handleEvent.ts` and registered its debug setting.

Verification: `test/LegacyCallHandler-test.ts` and `test/LegacyCallHandler-handleEvent-test.ts` passed (20 tests); ESLint on changed source and tests passed; `tsc --noEmit --jsx react` passed; `git diff --check` passed.
