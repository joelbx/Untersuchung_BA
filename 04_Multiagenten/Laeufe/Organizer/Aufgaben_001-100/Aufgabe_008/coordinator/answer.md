Added a five-second error cache to `useLink`, keyed by share and link ID. Fetches that fail with `NOT_FOUND`, `NOT_ALLOWED`, or `INVALID_ID` now reuse the same error during that period; other links and successful fetches continue normally.

The focused Jest suite passed (17 tests), along with the Drive TypeScript and formatting checks. I solved this directly; no delegation was used.