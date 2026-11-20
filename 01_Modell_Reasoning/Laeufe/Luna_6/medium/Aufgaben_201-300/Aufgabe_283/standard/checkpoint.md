# Checkpoint

Task: add a shared `isFromProton` helper for Message and Conversation elements.

Implemented `isFromProton(element: Element): boolean` in `applications/mail/src/app/helpers/elements.ts`. It returns true exactly when `IsProton === 1`. Added tests for values 1 and 0 on Message and Conversation objects.

Verification: `yarn workspace proton-mail test --runTestsByPath src/app/helpers/elements.test.ts --runInBand` passed.
