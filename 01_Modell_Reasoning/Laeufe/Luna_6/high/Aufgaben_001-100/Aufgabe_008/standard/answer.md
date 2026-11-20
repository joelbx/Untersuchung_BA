Updated [useLink.ts](/app/applications/drive/src/app/store/_links/useLink.ts:23) to reuse `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` errors for the same share and link for one second. Other links and successful fetches keep their existing behavior.

The focused test passed: 1 suite, 12 tests. `git diff --check` passed.