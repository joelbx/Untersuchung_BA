Updated optimistic mark-as handling so the reducer adds IDs to `bypassFilter` when the new status conflicts with the active Unread filter, and removes stale IDs when it matches. The dispatch now passes `markAsStatus`, and a new helper covers that decision.

Both relevant Jest suites passed: 10 tests total. `git diff --check` passed. The full TypeScript check was stopped before it finished.