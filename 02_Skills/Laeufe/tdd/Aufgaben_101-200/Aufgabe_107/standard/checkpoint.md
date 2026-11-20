# Checkpoint

Task: remove stale bypass filter entries for optimistic mark-as updates.
Approach: inspect local code and tests, add a failing regression test, implement the smallest change, run relevant and project test commands.
Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find`/`grep` for local inspection.

Implementation: added `markAsStatus` to optimistic action payload/type; added `getElementsToBypassFilter`; reducer now adds or removes derived IDs according to the active Unread filter.
TDD: targeted reducer test failed for both stale-ID cases before implementation, then passed (3 tests).
Checks: `yarn workspace proton-mail check-types --noEmit` passed. Prettier check and `git diff --check` passed. Full `yarn workspace proton-mail test --coverage=false` is running; existing suites emit React/jsdom and V8 warnings. Awaiting final result.
Final checks: `yarn workspace proton-mail test --coverage=false` passed (87 suites, 791 tests passed, 1 skipped; 32 snapshots passed). `yarn workspace proton-mail lint` passed. The full suite emitted non-failing React/jsdom, V8, and Jest force-exit warnings.
