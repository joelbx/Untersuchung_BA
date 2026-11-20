# Checkpoint

Task: Resolve mailbox element list reload timing, retry, stale response, and pending backend action tracking issues.

Implemented: Added query-aware loading state, pending action tracking and reload gating, distinct delayed retries for failed and stale responses, and stale metadata propagation from the API query. Pending action lifecycle signals bracket mailbox mutations, draft saves, sends/cancellations, deletes, and associated event refreshes. Local list resets retain the pending action count; multi-label requests wait for all sibling requests before releasing the reload guard.

Validation: `yarn workspace proton-mail check-types --pretty false` passed; ESLint passed on changed files; existing mailbox element, label, and event suites passed (29 tests); existing composer sending suite passed (14 tests, 1 skipped).
