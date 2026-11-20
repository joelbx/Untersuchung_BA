Task: implement IDN URL punycode conversion and apply it in useLinkHandler.
Status: completed.
Changes: added getHostnameWithRegex and punycodeUrl in packages/components/helpers/url.ts; replaced broad link encoding with hostname-only conversion for external HTTP(S) links; missing href now triggers an error notification. Added focused helper and hook tests.
TDD: new helper tests failed because functions were absent; new hook tests failed because query URL text was punycoded and missing href gave no notification. Both passed after implementation.
Verification: full components Jest suite passed (59 passed, 2 skipped; 275 tests passed, 10 skipped). TypeScript `./node_modules/.bin/tsc --noEmit -p packages/components/tsconfig.json` passed. Focused Jest run after formatting passed (2 suites, 16 tests). Prettier check, eslint on changed files, and git diff --check passed. No dependencies downloaded. `rg` unavailable; used find/grep.
