# Checkpoint

Implemented the Pill refactor:
- Replaced the class component with the named functional `Pill` export and named utility helpers.
- Added `src/hooks/usePermalink.tsx` for permalink type/entity resolution, room/member/profile data, avatars, display text, and user view actions.
- Updated `ReplyChain`, `BridgeTile`, and pillification to use named exports.

Verification:
- `yarn test test/utils/pillify-test.tsx --runInBand` passed (3 tests).
- ESLint, Prettier check, and `git diff --check` passed for the changed code.
- `yarn lint:types` reached unrelated existing Matrix SDK API mismatch errors in `LoginWithQR.tsx`, `Notifications.tsx`, and `VectorPushRulesDefinitions.ts`; it reported no errors in the changed files.
