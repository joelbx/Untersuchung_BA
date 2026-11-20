# Checkpoint

Task: Add `.well-known` `force_disable` policy for new room encryption and wire it through room creation UI.
Status: Complete. Implemented policy type, synchronous helper, shared async policy decision, default behavior, and dialog integration. Focused Jest tests pass (26 tests across two files). Targeted ESLint, Prettier, and git diff checks pass. TypeScript check reports only pre-existing `src/Unread.ts:167` error.
Constraints: Used local repository and existing tests only; git history, index, and harness configuration unchanged.
