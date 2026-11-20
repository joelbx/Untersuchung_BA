# Checkpoint

Task: Preserve assistant HTML formatting, repair nested lists, and scope links/images by messageID.

Status: Implementation complete. The composer message's localID is passed through preparation, rendering, and editor insertion. URL maps store messageID and formatting attributes; restoration removes unknown or cross-message links/images while preserving link text. Assistant Markdown conversion enables lists and HTML attributes, repairs nested list DOM structure, and preserves ordered list markers.

Checks:
- `node_modules/.bin/jest --runInBand --forceExit --coverage=false --config applications/mail/jest.config.js applications/mail/src/app/helpers/assistant/url.test.ts applications/mail/src/app/helpers/assistant/markdown.test.ts`: passed, 2 suites / 7 tests.
- `node_modules/.bin/jest --runInBand --forceExit --coverage=false --config applications/mail/jest.config.js applications/mail/src/app/helpers/textToHtml.test.ts applications/mail/src/app/helpers/message/messageContent.test.ts applications/mail/src/app/helpers/composer/contentFromComposerMessage.test.ts`: passed, 3 suites / 11 tests.
- `node_modules/.bin/prettier --check applications/mail/src/app/helpers/assistant/{markdown,markdown.test,url.test}.ts applications/mail/src/app/helpers/textToHtml.ts`: passed.
- `git diff --check`: passed.
- `node_modules/.bin/tsc --noEmit --project applications/mail/tsconfig.json --pretty false`: failed with TS2345 at `packages/crypto/lib/worker/api.ts:579`; `openpgp.PartialConfig` and nested `pmcrypto/node_modules/openpgp.PartialConfig` are incompatible. No diagnostics referenced edited mail files. Full app type-check status remains uncertain due to that unrelated dependency type error.
