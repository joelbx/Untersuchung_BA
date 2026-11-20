# Pill refactor checkpoint

Implemented functional, named-export Pill and a public `usePermalink` hook. Updated all Pill imports and `@room` helper calls. Added focused Pill tests and updated TextualBody snapshots for the required user-pill href and current-user class.

Checks executed:
- `node_modules/.bin/jest test/utils/pillify-test.tsx --runInBand --silent`: passed (3 tests).
- `node_modules/.bin/jest test/components/views/messages/TextualBody-test.tsx --runInBand --updateSnapshot --silent`: passed (15 tests; 2 snapshots updated).
- `node_modules/.bin/jest test/components/views/elements/Pill-test.tsx --runInBand --silent`: passed (5 tests).
- `node_modules/.bin/eslint src/hooks/usePermalink.tsx src/components/views/elements/Pill.tsx src/components/views/elements/ReplyChain.tsx src/components/views/settings/BridgeTile.tsx src/utils/pillify.tsx`: passed.
- `node_modules/.bin/eslint test/components/views/elements/Pill-test.tsx`: passed.
- `git diff --check`: passed.
- `node_modules/.bin/tsc --noEmit --jsx react`: failed with errors outside changed files. Installed matrix-js-sdk lacks `MSC3903ECDHv2RendezvousChannel`, `PushProcessor.getPushRuleAndKindById`, and multiple `RuleId` poll constants. No Pill or hook type errors were reported. Full project type correctness remains unverified because of those existing dependency errors.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep` for local searches. No dependencies were downloaded.
