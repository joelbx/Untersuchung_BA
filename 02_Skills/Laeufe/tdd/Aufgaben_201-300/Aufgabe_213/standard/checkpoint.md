# Checkpoint

Task: Make `useDefaultShare` expose an awaitable `isShareAvailable(signal, shareId)` that rejects locked or soft-deleted shares while preserving default-share behavior.

Status: Implemented and verified.

TDD: Added three availability cases before implementation. The first focused run failed in all three cases because `isShareAvailable` was absent; the existing default-share tests passed. Added a function that awaits `getShare(signal, shareId)` and checks both metadata flags.

Checks:
- Focused Jest run after implementation: 6 passed, 0 failed.
- Full Drive Jest suite (`node_modules/.bin/jest --config applications/drive/jest.config.js --rootDir applications/drive --runInBand --ci --coverage=false --detectOpenHandles`): 41 suites, 313 tests passed. Existing tests emitted console warnings for simulated offline retries, invalid extended attributes, and V8 asm.js linkage.
- `node_modules/.bin/tsc --project applications/drive/tsconfig.json --noEmit --pretty false`: passed.
- `git diff --check`: passed before final test title edit.
