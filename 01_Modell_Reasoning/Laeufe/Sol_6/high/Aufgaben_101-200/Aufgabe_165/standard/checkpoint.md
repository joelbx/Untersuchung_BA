# Checkpoint

Task: implement .well-known `force_disable` encryption policy for new rooms.
Status: implementation complete and verified.
Changes: typed well-known flag, synchronous force-disable helper, shared server/well-known decision helper, room defaults, dialog effective state and pending UI, focused tests.
Verification: 31 focused tests pass; targeted ESLint, Prettier, and git diff checks pass. Full TypeScript check reports an existing unrelated error in src/Unread.ts:167.
