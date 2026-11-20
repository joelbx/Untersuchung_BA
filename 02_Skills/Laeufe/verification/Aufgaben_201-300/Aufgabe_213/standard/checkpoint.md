# Checkpoint

Task: Make `useDefaultShare` expose an awaitable `isShareAvailable(signal, shareId)` that checks locked and soft-deleted metadata, while preserving default-share behavior.

Status: Added `isShareAvailable` to `useDefaultShare`. It calls `getShare(signal, shareId)` and returns false for locked or soft-deleted metadata. Added targeted tests for signal forwarding and each availability state. Existing default-share code remains intact.

Verification:
- Red run: targeted Jest suite exited 1 because `isShareAvailable` was missing; 3 new cases failed and 3 existing cases passed.
- Green run: `./node_modules/.bin/jest --config applications/drive/jest.config.js --runInBand --ci --coverage=false applications/drive/src/app/store/_shares/useDefaultShare.test.tsx` exited 0; 6 tests passed.
- `./node_modules/.bin/tsc --project applications/drive/tsconfig.json --noEmit` exited 0.
- `git diff --check` exited 0.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.
