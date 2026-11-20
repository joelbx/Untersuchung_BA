Updated the mail bypass filter logic so optimistic mark-as actions add IDs when the new status needs to bypass the active filter and remove stale IDs when it matches the filter. The dispatch now passes `markAsStatus`, and the reducer handles message and conversation IDs.

Verification passed: 8 new tests, 5 existing filter tests, the mail TypeScript check, and `git diff --check`.