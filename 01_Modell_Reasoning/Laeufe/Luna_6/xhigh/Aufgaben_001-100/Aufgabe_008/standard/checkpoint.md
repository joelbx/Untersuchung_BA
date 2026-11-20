# Checkpoint

Task: Reuse known client-visible `fetchLink` failures for the same `(shareId, linkId)` during a bounded backoff in Drive's `useLink` hook.

Implemented: Added a hook-local ref cache keyed by the serialized `(shareId, linkId)` pair. `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` failures are reused and removed after 5 seconds; other errors and successful results continue through their existing paths.

Verification: Existing `useLink.test.ts` passed (12 tests). ESLint passed for `useLink.ts`; `git diff --check` passed. The workspace Yarn launcher initially produced no output, so the existing Jest test was run directly using the repository's installed binary.
