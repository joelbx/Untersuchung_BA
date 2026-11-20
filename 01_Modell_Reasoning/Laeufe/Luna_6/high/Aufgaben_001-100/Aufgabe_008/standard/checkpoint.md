# Checkpoint

Task: add bounded reuse of known failed link fetches in Drive's `useLink` hook.

Implementation: `useLink.ts` caches `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` API errors per `(shareId, linkId)` for one second. Other errors and successful fetches retain the existing path. Cache expiry checks entry identity so an older timer cannot remove a newer cached error.

Validation: `yarn workspace proton-drive test --runTestsByPath src/app/store/_links/useLink.test.ts` passed (1 suite, 12 tests). `git diff --check` passed.
