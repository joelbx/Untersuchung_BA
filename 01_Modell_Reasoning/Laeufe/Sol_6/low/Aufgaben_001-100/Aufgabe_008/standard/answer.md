Updated [useLink.ts](/app/applications/drive/src/app/store/_links/useLink.ts) to reuse `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` fetch errors for the same `(shareId, linkId)` for 30 seconds. Other links and successful fetches continue through the existing path.

Verification: all 12 existing `useLink` tests passed, and `git diff --check` passed.