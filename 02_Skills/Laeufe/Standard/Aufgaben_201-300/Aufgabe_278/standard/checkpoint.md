# Checkpoint

Resolved mailbox element loading timing and retry behavior.

Changes:
- Track pending backend operations in the elements slice and preserve the count across list resets.
- Defer list requests until the count reaches zero; use page and params in the loading selector.
- Retry failed queries after 2 seconds and stale responses after 1 second without committing stale data.
- Track label, move, mark, star, undo, and empty-label backend operations through event synchronization.
- Added focused tests for action counting, reset preservation, stale responses, and failed requests.

Verification:
- `yarn workspace proton-mail check-types` passed.
- `yarn workspace proton-mail test elementsLoading.test.ts Mailbox.labels.test.tsx --coverage=false --forceExit` passed (11 tests).
- `yarn workspace proton-mail test elementsLoading.test.ts Mailbox.labels.test.tsx Mailbox.elements.test.tsx --coverage=false --forceExit` passed (23 tests) before the final empty-label error-path cleanup; the final cleanup was covered by the 11-test rerun.
- `git diff --check` passed.

Local tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`. No dependency downloads.
