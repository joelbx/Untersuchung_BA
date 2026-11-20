# PassAliases issue checkpoint

Completed: explicit default-vault lookup and creation; provider state moved to `usePassAliasesSetup`; alias fetch/filter helpers; no-vault initialization and cache clearing; first-alias vault creation; explicit "No aliases" empty state. Existing alias creation continues to refetch with `maxAge: 0`, update counts and memoized items, and copy the email with a success notification.

TDD red checks observed before fixes: helper fetch rejected as unimplemented; hook rejected as unimplemented; bridge lookup rejected due old callback signature; empty-state assertion failed; stale cached aliases remained when no vault existed.

Verification: PassAliases focused suite 4/4 suites, 10/10 tests passed. Components full suite 143 passed, 2 skipped, 904 tests passed, 28 skipped. Pass full suite 81/81 suites, 493/493 tests passed. Components and Pass TypeScript checks passed. Targeted ESLint passed. `git diff --check` passed. Pass suite emitted the existing Browserslist outdated-data warning; no dependencies were downloaded.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); local `find`/`grep` fallback used.
