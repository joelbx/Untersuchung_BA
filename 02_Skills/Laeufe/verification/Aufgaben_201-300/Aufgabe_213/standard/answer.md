Added `isShareAvailable(signal, shareId)` to `useDefaultShare`. It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. The existing default-share path remains unchanged.

Verification: all 6 targeted Jest tests passed, the Drive TypeScript check passed, and `git diff --check` passed.