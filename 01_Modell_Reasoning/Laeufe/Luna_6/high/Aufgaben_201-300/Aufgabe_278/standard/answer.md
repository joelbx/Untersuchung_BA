Implemented the mailbox loading and retry changes across the elements hook, actions, reducers, selectors, slice, types, and query helper.

List resets, requests, and page updates now wait until `pendingActions` is zero. Loading reflects the current page and query. Failed requests retry after two seconds; stale responses are rejected and retried after one second.

Verification passed: mail type check, the existing mailbox elements test (12 tests), and `git diff --check`.