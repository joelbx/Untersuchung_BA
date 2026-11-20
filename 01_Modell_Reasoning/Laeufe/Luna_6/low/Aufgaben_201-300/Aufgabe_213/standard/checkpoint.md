# Checkpoint

Task: Fix share availability handling in `useDefaultShare` while preserving default share loading/creation.

Implemented `isShareAvailable(abortSignal, shareId)` using `getShare` and checking both `isLocked` and `isVolumeSoftDeleted`. Added existing-hook test coverage for available and unavailable metadata and signal forwarding.

Verification: `yarn workspace proton-drive test --runTestsByPath src/app/store/_shares/useDefaultShare.test.tsx` passed (1 suite, 4 tests).
