# Checkpoint

Task: add `isFromProton(element: Element): boolean` for mail messages and conversations.

Implemented:
- Added optional `IsProton` typing to message metadata, conversations, and encrypted search messages.
- Added a strict `IsProton === 1` helper in `elements.ts`.
- Added cases for both element types with values 0 and 1, plus an absent flag.

Verification:
- `yarn workspace proton-mail test --runTestsByPath src/app/helpers/elements.test.ts --coverage=false --watch=false`: exit 0, 22 tests passed.
- `yarn workspace proton-mail check-types --noEmit --incremental false`: exit 0.
- `git diff --check`: exit 0.

Note: `applications/mail/src/app/components/list/VerifiedBadge.tsx` does not exist in this checkout. The requested implementation is the helper; no badge component was added.
