# Checkpoint

Task: make `useDefaultShare` expose an awaitable `isShareAvailable(signal, shareId)` that reports locked or soft-deleted shares as unavailable while preserving default-share behavior.

Status: investigating repository implementation and tests. `rg` is unavailable (`/bin/bash: rg: command not found`), so searches use local `grep`/`find`.

Root cause: `useDefaultShare` only returns `getDefaultShare`; callers have no availability function. `useShare.getShare(signal, id)` already returns the cached or fetched share, and the `Share` metadata includes `isLocked` and `isVolumeSoftDeleted`. The existing default-share selection excludes both states. A new focused test failed as expected with `TypeError: hook.current.isShareAvailable is not a function` (Jest exit 1); the three preexisting default-share tests passed.

Hypothesis: exposing an async helper that calls `getShare(signal, id)` and checks both flags will satisfy availability semantics without altering default-share creation.

Implementation: `useDefaultShare` now returns `isShareAvailable(abortSignal, shareId)`. It awaits `getShare` with the exact arguments and returns true only if neither availability flag is set. Existing `getDefaultShare` logic was untouched. Added parameterized tests for all four flag combinations and signal forwarding.

Verification: `./node_modules/.bin/jest --config applications/drive/jest.config.js --runInBand --coverage=false applications/drive/src/app/store/_shares/useDefaultShare.test.tsx` passed (7/7); `./node_modules/.bin/prettier --check applications/drive/src/app/store/_shares/useDefaultShare.ts applications/drive/src/app/store/_shares/useDefaultShare.test.tsx` passed; `./node_modules/.bin/tsc --noEmit --project applications/drive/tsconfig.json` passed; `git diff --check` passed.
