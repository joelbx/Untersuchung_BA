# Checkpoint

Task: fix mailbox element reload timing, stale responses, and retry behavior.

Root cause: the list effect did not observe backend activity; the loading selector ignored `shouldSendRequest`; `queryElements` dropped the API `Stale` flag, so stale responses reached the fulfilled reducer. Retry dispatch existed, but its action was not registered in the slice.

Changes: added pending action tracking and wired it into label/move/star, mark read/unread, and permanent delete operations; deferred the whole list effect while actions are active. Added stale propagation, a distinct one-second stale retry, two-second failure retry, reducers, and page-aware loading. Added focused tests for lifecycle, loading, stale rejection, and failure retry.

Checks:
- Before fix: `../../node_modules/.bin/jest --runInBand --coverage=false src/app/logic/elements/elementsReload.test.ts` failed as expected (missing backend action and incorrect loading).
- After fix: `../../node_modules/.bin/tsc --noEmit --pretty false` passed.
- After fix: `../../node_modules/.bin/jest --runInBand --coverage=false src/app/logic/elements/elementsReload.test.ts src/app/containers/mailbox/tests/Mailbox.elements.test.tsx` passed (16 tests); Jest noted an existing open handle after completion.
- After final test cleanup: focused Jest test passed (4 tests), TypeScript passed, and `git diff --check` passed.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`), so local `grep` and `find` were used. No downloads or external research.
