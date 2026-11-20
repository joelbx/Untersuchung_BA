Updated the optimistic mark-as flow so elements are added to `bypassFilter` when their new status conflicts with the active Read or Unread filter, and removed when their status matches it. The action now carries `markAsStatus`, and the reducer uses the new `getElementsToBypassFilter` helper.

Validation passed: 13 focused tests, TypeScript, ESLint, Prettier, and `git diff --check`.