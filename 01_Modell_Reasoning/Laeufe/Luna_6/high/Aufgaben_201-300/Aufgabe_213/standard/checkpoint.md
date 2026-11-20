# Checkpoint

Implemented `isShareAvailable(abortSignal, shareId)` in `useDefaultShare`. It awaits `getShare` with the same signal and identifier, then reports false for locked or soft-deleted shares. The existing default-share loading and volume creation path is unchanged.

Validation: Prettier check and `git diff --check` pass. The focused existing Jest test was attempted twice (with and without `--detectOpenHandles`) but remained CPU-bound without output, so both runs were stopped; no test result was available.
