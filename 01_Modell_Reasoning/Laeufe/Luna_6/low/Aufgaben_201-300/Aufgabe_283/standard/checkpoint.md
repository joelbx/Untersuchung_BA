# Checkpoint

Task: add a shared `isFromProton` helper for Message and Conversation mail elements.

Implemented `isFromProton(element: Element): boolean` in `applications/mail/src/app/helpers/elements.ts`. It uses strict comparison with `1`, so Message and Conversation elements follow the same evaluation. Added coverage for both element kinds with `IsProton` values `1` and `0` in `elements.test.ts`.

Verification: `yarn workspace proton-mail test --runTestsByPath src/app/helpers/elements.test.ts` passed. The initial attempt with workspace name `mail` failed because the actual workspace is `proton-mail`; no repository changes resulted from that attempt.
