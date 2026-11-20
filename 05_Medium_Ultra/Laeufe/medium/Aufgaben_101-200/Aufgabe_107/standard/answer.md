Updated the optimistic mark-as flow to pass `markAsStatus`. The reducer now adds IDs to `bypassFilter` when the new status needs to bypass the active filter and removes stale IDs when it matches the filter.

Mail’s existing element helper tests pass (5/5). TypeScript, ESLint, Prettier, and `git diff --check` also pass.