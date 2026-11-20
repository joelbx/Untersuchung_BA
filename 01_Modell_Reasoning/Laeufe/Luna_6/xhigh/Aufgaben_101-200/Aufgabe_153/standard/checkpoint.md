# Checkpoint

## Issue
The Drive share member view is mixing member and invitation data across shares. Stores need to isolate data by `shareId`, and a utility must combine existing email addresses from members and both invitation types.

## Work plan
- Inspect the invitation/member stores, view and action call sites, types, and nearby tests.
- Change store APIs/state to key records by share ID while preserving independent internal/external invitations.
- Add `getExistingEmails` in the appropriate share utility module and cover behavior using existing test conventions.
- Run relevant existing tests and report results.

## Progress and verification
- Stores now keep members, internal invitations, and external invitations in separate maps keyed by `shareId`, with per-share getters and updates.
- The Zustand member view selects its data by the active share and applies all mutations to that share. Empty-share checks read current per-share store values.
- Added and adopted `getExistingEmails` in both member views.
- `yarn workspace @proton/drive-store check-types`: passed.
- Targeted ESLint on changed files: passed with `--quiet` (pre-existing hook dependency warnings are omitted).
- Existing `_shares` Jest suite: 7 suites and 28 tests passed.
- `git diff --check`: passed.

## Constraints
Use repository code and existing tests only. Do not change git history, index baseline, or harness configuration.
