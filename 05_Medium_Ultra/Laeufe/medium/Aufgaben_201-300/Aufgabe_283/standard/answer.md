Added `isFromProton(element: Element)` in [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton === 1` for both messages and conversations. I updated the element types and added tests for values `1`, `0`, and absent.

Verification passed: 25 helper tests, the mail TypeScript check, Prettier, and `git diff --check`.