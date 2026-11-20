# Mailbox element reload fix

- Identified the mailbox hook and element actions, reducers, selectors, slice, types, and query helper.
- Working tree starts clean. Added retry and stale response handling, backend action tracking, context-aware loading, and hooks that track mailbox mutations. Requests that overlap backend changes are discarded and retried after the changes finish. Delayed retries are skipped after page or query changes.
- Verified: TypeScript check, targeted ESLint, and `git diff --check` passed; mailbox elements, labels, events, hotkeys, and element request tests passed (43 tests).
