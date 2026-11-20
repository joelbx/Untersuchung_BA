# Checkpoint

Task: Fix mailbox elements reload timing, retries for failed/stale responses, and backend operation tracking.

Completed:
- Added `pendingActions` to elements state, lifecycle actions/reducers, and selector.
- Deferred cache reset, list requests, and page updates until no backend actions are pending; the loading effect reruns when the counter changes.
- Passed page and query params into the loading selector and included `shouldSendRequest` in its loading calculation.
- Added API `Stale` metadata, rejected stale results, and scheduled stale retries after 1 second. Generic request failures retry after 2 seconds.
- Registered retry, stale retry, and backend action reducers in the elements slice.

Verification:
- `yarn workspace proton-mail check-types --pretty false` passed.
- Existing mailbox elements test passed: 12 tests.
- `git diff --check` passed.
