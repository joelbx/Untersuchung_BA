Added `isFromProton(element: Element)` in [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton === 1`, using the same check for messages and conversations. I also added `IsProton` to the relevant types and tests for both values.

Verification passed: 21 mail helper tests, the mail TypeScript check, and `git diff --check`.