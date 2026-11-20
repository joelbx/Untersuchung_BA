# Checkpoint

Implemented hostname text extraction and hostname-only Punycode URL conversion in `packages/components/helpers/url.ts`. Updated `useLinkHandler` to use that conversion for confirmation links and to notify when a link URL has no extractable hostname.

Validation: `yarn workspace @proton/components test --runTestsByPath helpers/url.test.ts` passed; `git diff --check` passed. Existing URL test suite does not currently cover the new helper behavior.
