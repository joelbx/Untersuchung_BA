# Checkpoint

Task: Resolve move-out decisions using the active element ID and the valid element IDs, suspending evaluation while elements load.

Implementation status: Replaced cache and label membership checks with a mailbox-slice ID membership check. Passed the current IDs and loading state from `MailboxContainer` to both view components; conversation view selects the message ID for always-message labels.

Verification:
- Focused existing tests: 3 suites passed, 30 tests passed.
- Mail workspace TypeScript check passed.
- ESLint passed for all changed TypeScript files.
- Prettier passed for the hook, mailbox container, and updated fixture. The two view files fail Prettier on their unchanged checked-out baseline formatting; no broad formatting was applied.

Implementation and verification complete.
