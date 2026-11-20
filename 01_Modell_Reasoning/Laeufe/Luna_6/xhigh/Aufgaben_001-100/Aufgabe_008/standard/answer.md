Implemented a 5 second failure cache in [useLink.ts](/app/applications/drive/src/app/store/_links/useLink.ts:26). It reuses `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` errors for the same `(shareId, linkId)` pair, then removes each cached error after the backoff.

Verification passed: `useLink.test.ts` (12 tests), ESLint for `useLink.ts`, and `git diff --check`.