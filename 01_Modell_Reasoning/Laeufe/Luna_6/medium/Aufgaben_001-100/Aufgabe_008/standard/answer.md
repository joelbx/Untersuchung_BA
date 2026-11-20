Implemented a 5-second error cache in [useLink.ts](/app/applications/drive/src/app/store/_links/useLink.ts). It reuses `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` errors for the same `(shareId, linkId)`; other links and successful fetches are unaffected.

`git diff --check` passed. The targeted Jest test runner started but produced no output, so I stopped it; the test result is unverified.