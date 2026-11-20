Updated optimistic mark-as handling so actions that match the active Read or Unread filter remove stale IDs from `bypassFilter`; opposite actions add them. The dispatch now carries `markAsStatus`, and the reducer preserves conversation ID handling.

Verification passed: 8 focused tests, the existing filtered mailbox test, Mail’s TypeScript check, and formatting checks.