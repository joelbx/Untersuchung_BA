Implemented `isFromProton` with a strict `IsProton === 1` check. Message, Conversation, and encrypted search message types now expose the optional 0/1 property. Added the `VerifiedBadge` component with a tooltip and used it in the list layout.

Verification passed: the focused helper suite (23 tests), the mail app typecheck, and `git diff --check`.