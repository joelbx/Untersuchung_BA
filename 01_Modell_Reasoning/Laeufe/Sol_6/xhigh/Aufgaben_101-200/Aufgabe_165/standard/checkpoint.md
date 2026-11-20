# Progress checkpoint

- Task: implement .well-known `force_disable` for new room encryption and UI.
- Initial state: working tree clean. Inspecting repository guidance and relevant code.
- Next: trace existing policy/default handling, implement helper and dialog integration, run existing tests.
- Implemented strict .well-known force-disable helper, shared server/.well-known policy resolver, and dialog lock/value handling.
- Added focused policy and dialog tests. Running repository test/type/format checks now.
- Focused Jest suites passed: 25/25 tests.
- ESLint, Prettier and git diff whitespace checks passed.
- First full TypeScript run found one new dialog state type error (fixed) and an unrelated existing error at src/Unread.ts:167. Final typecheck is still running.
- Final TypeScript check: only src/Unread.ts:167 error remains; no errors in edited files.
- Work complete; changes left in checked-out files for coordinator export.
