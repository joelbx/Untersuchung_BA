# Checkpoint

Task: accessible room-share and settings external links.

Root cause: ShareDialog rendered a raw permalink without a descriptive title. ProfileSettings rendered a separate icon-only anchor beside an ambiguously named text link. Other settings external anchors duplicated target/rel markup and had no nonvisual new-tab cue.

Changes: added ExternalLink with native anchor props, secure new-tab defaults, hidden accessible new-tab text, and an aria-hidden CSS-mask icon; imported its SCSS globally. Migrated settings external anchors, removed ProfileSettings's separate image link, improved generic external link text, and added localized strings. ShareDialog now titles permalinks according to room, message, user, or community target.

Verification:
- Initial focused Jest test failed as expected because ExternalLink did not exist.
- `./node_modules/.bin/jest --runInBand test/components/views/elements/ExternalLink-test.tsx test/i18n-test/languageHandler-test.js` passed: 2 suites, 12 tests.
- Targeted `eslint --max-warnings 0` on edited TS/TSX files passed.
- Targeted `stylelint` on edited SCSS, `git diff --check`, and JSON parse of en_EN.json passed.
- `./node_modules/.bin/tsc --noEmit --jsx react` failed (exit 2) with six errors in untouched `src/components/structures/ThreadView.tsx` and `src/stores/notifications/ThreadNotificationState.ts` about absent `ThreadEvent.ViewThread`/`NewReply` and a call with 2 arguments where 1 is expected. No errors were reported in edited files. This pre-existing SDK/type mismatch leaves full-project type checking unverified.
