Refactored Pill into a functional component and added the reusable `usePermalink` hook. Exported `Pill`, `PillType`, `pillRoomNotifPos`, and `pillRoomNotifLen` as named exports, and updated downstream imports.

Verification: ESLint passed, and all 3 existing `pillify` tests passed. `yarn lint:types` is blocked by existing Matrix SDK type errors in unrelated files.