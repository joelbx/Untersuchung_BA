# Checkpoint

- Task: make move-out decisions depend on active element ID, valid element IDs, and loading state in both views.
- Initial status: repository clean; `rg` is unavailable (`/bin/bash: rg: command not found`), so use `find` and `grep` for local inspection.
- `./node_modules/.bin/jest --config applications/mail/jest.config.js --runInBand --coverage=false applications/mail/src/app/hooks/useShouldMoveOut.test.ts applications/mail/src/app/components/conversation/ConversationView.test.tsx`: passed, 2 suites and 16 tests (exit 0).
- `git diff --check`: passed (exit 0).
- `./node_modules/.bin/tsc --noEmit -p applications/mail/tsconfig.json`: passed (exit 0).
- Prettier check of six touched files exited 1 because `ConversationView.tsx` and `MessageOnlyView.tsx` contain pre-existing formatting differences outside the edits (for example `{scrollTo}` and JSX indentation). The changed hook, hook test, container, and conversation test passed that check.
