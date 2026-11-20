Implemented the analytics privacy and initialization changes in [PosthogAnalytics.ts](/app/src/PosthogAnalytics.ts). It now validates configuration, enforces anonymous mode under DNT, gates captures by enabled and initialized state, hashes user and room IDs, and uses the current anonymity state for event and URL handling. Added the requested state accessors and logout reset behavior.

Updated [PosthogAnalytics-test.ts](/app/test/PosthogAnalytics-test.ts) for awaited initialization and DNT behavior.

The focused suite passed: 13 tests. ESLint and `git diff --check` passed. `yarn lint:types` remains blocked by existing dependency and unrelated SDK type errors; it reported none in `PosthogAnalytics.ts`.