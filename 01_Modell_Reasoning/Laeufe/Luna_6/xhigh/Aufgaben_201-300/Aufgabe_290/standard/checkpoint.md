# Checkpoint

Task: Resolve muted call notification playback in `/app`.

Initial inspection: No `AGENTS.md` files were found under the parent workspace. `rg` is unavailable; using `find` and standard shell tools for repository inspection.

Findings: Call sounds are played by `LegacyCallHandler.play()` in `src/LegacyCallHandler.tsx`; its `AudioID` enum held the four DOM IDs but was private. The requested `src/legacy/LegacyCallHandler/handleEvent.ts` path was absent.

Changes made: Exported `AudioID`, unmute the sound element only when muted immediately before `play()`, added the public media event listener module with structured error and opt-in debug logging, and registered its device-only debug setting.

Validation: `yarn test --runInBand test/LegacyCallHandler-test.ts` passed (9 tests); ESLint passed on changed source files; `yarn tsc --noEmit --jsx react` passed; `git diff --check` passed.

Status: Changes are complete. The working diff contains the playback recovery, exported sound identifiers, the requested event listener, and its opt-in debug setting.
