# Checkpoint

Task: Add `isFromProton` for mail elements and use it for the verified message badge.

Implemented: `IsProton` in MessageMetadata, Conversation, and ESMessage metadata; `isFromProton` helper; preserved the flag when building encrypted search records; a shared VerifiedBadge with tooltip in both list layouts; list badge decision now uses the flag. Added message and conversation cases for 1, 0, and missing flags.

Verification: `elements.test.ts` passed (22 tests); mail `check-types` passed; targeted ESLint passed; Prettier check passed; `git diff --check` passed.
