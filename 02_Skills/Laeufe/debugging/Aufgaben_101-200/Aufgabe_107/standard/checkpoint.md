# Checkpoint

Task: remove stale bypass filter entries after mark-as actions.

Status: implementation complete. `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.

Repository baseline: `6ff80e3`; working tree initially clean.

Root cause: `optimisticUpdates` appended every marked element's ID to `bypassFilter` without considering whether its new status matched the active unread filter. The selector accepts any bypassed ID, so stale entries kept elements visible.

Reproduction: added reducer tests. Before the fix, three cases failed as expected: matching unread/read filters retained message IDs, and conversation mode retained the conversation ID.

Fix: pass `markAsStatus` from the optimistic hook, type it in `OptimisticUpdates`, classify elements in `getElementsToBypassFilter`, and add or remove the derived IDs in the reducer only when bypass and status are present.

Verification:
- `../../node_modules/.bin/jest --runInBand --coverage=false src/app/logic/elements/elementsReducers.test.ts src/app/logic/elements/helpers/elementTotal.test.ts` from `applications/mail`: 2 suites, 10 tests passed.
- `../../node_modules/.bin/tsc --noEmit --pretty false` from `applications/mail`: exit 0.
- `../../node_modules/.bin/prettier --check src/app/hooks/optimistic/useOptimisticMarkAs.ts src/app/logic/elements/elementsTypes.ts src/app/logic/elements/elementsReducers.ts src/app/logic/elements/helpers/elementBypassFilters.ts src/app/logic/elements/elementsReducers.test.ts` from `applications/mail`: exit 0.
- `git diff --check`: exit 0.
