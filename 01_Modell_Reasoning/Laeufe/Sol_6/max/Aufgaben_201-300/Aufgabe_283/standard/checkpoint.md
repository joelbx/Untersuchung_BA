# Progress checkpoint

- Added `isFromProton(element: Element): boolean`, returning true only when `IsProton === 1`.
- Added `IsProton` to message, conversation, and encrypted search element types; encrypted search metadata now preserves the flag.
- Updated the list's verified badge to use the helper, and extracted `VerifiedBadge` with a "Verified message" tooltip.
- Verified: mail `elements.test.ts` passed (19 tests), mail TypeScript check passed, Prettier check passed, and `git diff --check` passed.
