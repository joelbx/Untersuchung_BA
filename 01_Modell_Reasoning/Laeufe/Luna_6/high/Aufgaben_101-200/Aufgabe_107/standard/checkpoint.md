# Checkpoint

Task: Resolve stale bypass filter entries when marking mail elements read/unread.

Implemented status-aware bypass updates:
- The optimistic mark-as action now carries `markAsStatus`.
- `OptimisticUpdates` declares the optional status field.
- `getElementsToBypassFilter` classifies changed elements based on the current unread filter and mark-as status.
- The reducer adds bypass IDs when needed and removes IDs when the active read/unread filter already matches the new status.

Validation: `yarn workspace proton-mail check-types --pretty false` passed. The existing `src/app/helpers/elements.test.ts` suite reported all tests passed, but its Jest process lingered after the pass summary and was interrupted. `git diff --check` passed.
