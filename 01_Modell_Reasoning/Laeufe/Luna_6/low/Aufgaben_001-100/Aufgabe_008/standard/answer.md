Updated [useLink.ts](/app/applications/drive/src/app/store/_links/useLink.ts:21) to cache `NOT_FOUND`, `NOT_ALLOWED`, and `INVALID_ID` fetch errors for five seconds, keyed by share and link IDs. Repeated failures for that key reuse the cached error; other links continue fetching normally.

The focused Jest run did not produce output and was interrupted, so the tests remain unverified.