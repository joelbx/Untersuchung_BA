# Checkpoint

Task: fix stale bypass-filter entries when marking mail read/unread.

Plan: inspect repository guidance and the mark-as action, reducer, helper, and existing focused tests; implement the requested status-aware bypass add/remove behavior; run relevant existing tests only.

Constraints: use local repository code/tests; do not touch git history, index baseline, harness configuration, credentials, private process files, or evaluator artifacts.

Findings: bypass IDs are derived from `ConversationID` for messages in conversation mode and `ID` otherwise. `Filter.Unread` uses numeric truthiness (`1` unread, `0` read), while `MARK_AS_STATUS` is the `read`/`unread` enum. No focused tests exist for the reducer/helper; the only nearby existing unit test covers element totals.

Implementation complete: mark-as dispatches now include `markAsStatus`; `OptimisticUpdates` carries the optional status; the new helper classifies elements for bypass/removal based on the unread filter; the reducer adds unique derived IDs and removes IDs that now match the filter.

Verification: `yarn workspace proton-mail check-types` passed. `yarn workspace proton-mail test --runTestsByPath src/app/containers/mailbox/tests/Mailbox.elements.test.tsx` passed (12 tests). `git diff --check` passed.
