Implemented the PostHog privacy and lifecycle changes in [PosthogAnalytics.ts](/app/src/PosthogAnalytics.ts). Initialization now validates configuration and honors DNT; tracking, identification, room events, and URL redaction follow the current anonymity state. Added the requested state accessors and `logout()`.

Updated the existing tests to await async initialization in [PosthogAnalytics-test.ts](/app/test/PosthogAnalytics-test.ts).

The focused analytics suite passes (13 tests), and ESLint passes for the implementation. The project-wide TypeScript check remains blocked by existing dependency and unrelated project errors.