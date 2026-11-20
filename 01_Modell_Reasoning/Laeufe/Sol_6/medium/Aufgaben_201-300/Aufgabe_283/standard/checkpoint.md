# Checkpoint

Task: Add `isFromProton(element: Element): boolean` and use Proton origin for the mail list's verified badge.

Completed:
- Added optional `IsProton` to message, conversation, and encrypted-search element types.
- Added a strict `IsProton === 1` helper and tests for message and conversation values 0 and 1, plus an absent value.
- Added `VerifiedBadge` with a “Verified message” tooltip and used it in the column list.
- Updated the existing badge condition to use `isFromProton` while retaining the DMARC failure check.

Verification:
- `yarn jest --runInBand --coverage=false src/app/helpers/elements.test.ts` passed (22 tests).
- `yarn check-types --pretty false` passed.
- `git diff --check` passed.
