Added `isFromProton(element: Element)`, which returns `true` only when `IsProton === 1` for messages and conversations. I also added the flag to the relevant types, preserved it in encrypted search, and added the specified `VerifiedBadge` tooltip component.

Verification passed: 21 helper tests, the mail type check, targeted ESLint, and `git diff --check`.