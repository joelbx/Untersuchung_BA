# Checkpoint

Issue: Drive member view mixed people across shares.

Root cause: The Zustand members, internal invitations, and external invitations stores each used a single global array. The view read those arrays before fetching the current share, so data from another share appeared and writes replaced unrelated share data. The application and `drive-store` package duplicate these files.

Reproduction: Added `member-isolation.test.ts` in both copies. Before the fix, the application test failed with `TypeError: store.getMembers is not a function` and `TypeError: store.getInvitations is not a function`, demonstrating the absence of share-specific reads.

Fix: Stores now key arrays by share ID, expose share-specific getters returning empty arrays for missing shares, and scope each mutation to its share. The view selects only the resolved share ID and passes the ID to every write. A pure `getExistingEmails` utility combines all three email sources. Aborted fetches cannot update the view after navigation.

Verification completed:
- Application isolation tests: 3 passed.
- Package isolation tests: 3 passed.
- Existing application `shares.store.test.ts` plus initial isolation tests: 20 passed.
- Package `tsc --noEmit --pretty false`: passed.
- Application `tsc --noEmit --pretty false`: final rerun passed.
- `git diff --check`: passed.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); used local `find`/`grep`. No downloads.
