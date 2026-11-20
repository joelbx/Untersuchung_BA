# Checkpoint

- Task: Add `isShareAvailable` to `useDefaultShare` while preserving default share behavior.
- Added `isShareAvailable(abortSignal, shareId)` using `getShare` and both share availability flags.
- Added tests for all flag combinations and forwarding the `AbortController` signal and share ID. Existing default share tests remain intact.
- `yarn test useDefaultShare.test.tsx --runInBand` (from `applications/drive`): passed, 7 tests.
- `./node_modules/.bin/prettier --check applications/drive/src/app/store/_shares/useDefaultShare.ts applications/drive/src/app/store/_shares/useDefaultShare.test.tsx`: passed.
- `git diff --check`: passed.
