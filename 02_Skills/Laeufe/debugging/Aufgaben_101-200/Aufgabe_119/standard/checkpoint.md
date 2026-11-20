# Checkpoint

Task: Refactor Pill and extract usePermalink.

## Investigation and root cause

The class in `src/components/views/elements/Pill.tsx` mixed permalink parsing, profile lookup, hover state, and presentation. Its user branch set `href = null`, dropping a message pill's original URL. Its message path dereferenced `parsePermalink(url).primaryEntityId` even when parsing returned null, so an unrecognised URL threw instead of failing quietly. `load()` also dereferenced `resourceId[0]` for an explicit room type without a URL. The @room token helpers were class statics and all production callers used the default export.

Local comparison: existing hooks use effect/state for async profile data. `getPrimaryPermalinkEntity` is the existing local parser that returns null for unrecognised URLs and handles supported permalink forms. The fix moves entity resolution and profile lookup into `usePermalink`, while the functional `Pill` owns hover and DOM rendering. It preserves the input URL verbatim in message links.

The initial regression test was executed before implementation with `node_modules/.bin/jest --runInBand test/components/views/elements/Pill-test.tsx` and failed as expected: user message href was null instead of the input URL, and an unknown URL threw `TypeError: Cannot read properties of null (reading 'primaryEntityId')` at `Pill.tsx:99`.

## Verification

- `node_modules/.bin/jest --runInBand test/components/views/elements/Pill-test.tsx test/utils/pillify-test.tsx --silent`: passed, 2 suites and 10 tests.
- `node_modules/.bin/eslint src/components/views/elements/Pill.tsx src/hooks/usePermalink.tsx src/utils/pillify.tsx src/components/views/elements/ReplyChain.tsx src/components/views/settings/BridgeTile.tsx test/components/views/elements/Pill-test.tsx`: passed.
- `git diff --check`: passed.
- `node_modules/.bin/tsc --noEmit --jsx react --pretty false`: exit 2. The remaining errors are in untouched files: `LoginWithQR.tsx:20` missing `MSC3903ECDHv2RendezvousChannel`; `Notifications.tsx:489-490` missing `getPushRuleAndKindById`; and `VectorPushRulesDefinitions.ts:136-139,163` missing several poll `RuleId` values. These appear to be existing SDK/API mismatches. No error was reported for the changed files, but a full clean type check cannot be claimed.

`rg` is unavailable (`/bin/bash: rg: command not found`); local find/grep were used. No dependencies downloaded and no git history/index/harness changes made.
