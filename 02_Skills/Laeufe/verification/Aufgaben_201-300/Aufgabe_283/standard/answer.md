Added `isFromProton(element: Element)` in [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton === 1` and works for messages and conversations. I also updated the element types and added tests for both values and a missing flag.

Verification: all 22 focused tests passed, the mail type check passed, and `git diff --check` passed.