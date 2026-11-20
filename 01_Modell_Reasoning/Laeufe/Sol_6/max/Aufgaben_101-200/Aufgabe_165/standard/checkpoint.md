# Checkpoint

- Task: implement `.well-known` `force_disable` policy for new room encryption and UI.
- Repository status at start: clean.
- Added the strict `.well-known` force-disable helper and policy resolution with server precedence.
- Updated room defaults and `CreateRoomDialog` to display and submit the enforced value, with controls disabled while policy is pending.
- Added focused policy and dialog tests. Targeted Jest: 3 suites, 39 tests passed. ESLint, Prettier, and `git diff --check` passed.
- Full TypeScript check reports an unrelated existing error in `src/Unread.ts:167` (`getLastUnthreadedReceiptFor` on `Thread | Room`).
- Existing consumer tests also passed: 3 suites, 28 tests and 1 snapshot. Final diff reviewed.
