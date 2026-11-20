# Checkpoint

Implemented IDN URL conversion in `packages/components/helpers/url.ts` using URL parsing and `punycode.js` for the hostname. The helper preserves the parsed URL components and removes a trailing pathname slash. Added regex based host label extraction and focused helper tests. Updated `useLinkHandler` to convert external links before confirmation or navigation and to notify when a link has no extractable URL or cannot be parsed.

Verification:
- `yarn workspace @proton/components test helpers/url.test.ts --coverage=false --watch=false` — passed (15 tests).
- `yarn workspace @proton/components check-types --pretty false` — passed.
- `yarn workspace @proton/components exec eslint helpers/url.ts helpers/url.test.ts hooks/useLinkHandler.tsx --quiet` — passed.
- `git diff --check` — passed.
