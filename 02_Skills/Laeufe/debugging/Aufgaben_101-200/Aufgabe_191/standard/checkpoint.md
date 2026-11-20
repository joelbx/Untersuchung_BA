# Checkpoint

Task: add registration-token support to InteractiveAuth, including stable and unstable auth types.

Status: implementation complete; relevant tests pass.

Root cause: the installed matrix-js-sdk already defines stable and unstable registration-token AuthType values and adds the session to submitted auth dictionaries. Element's getEntryComponentForLoginType switch omitted both values, sending users to FallbackAuthEntry.

Reproduction: `./node_modules/.bin/jest test/components/structures/InteractiveAuth-test.tsx --runInBand --silent` failed before the fix for both identifiers: no textbox named "Registration token" was present; the only action was "Start authentication".

Changes: added RegistrationTokenAuthEntry, routed both auth types to it, added English strings and tests for stage submission and UI states.

Checks: registration-token and InteractiveAuthDialog Jest suites passed (4 tests); targeted ESLint passed; Prettier check passed; `git diff --check` passed.

TypeScript check: `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with existing errors in untouched SlidingSyncManager.ts, RoomSublist.tsx, useSlidingSyncRoomSearch.ts, SlidingRoomListStore.ts and their tests. Representative errors: `src/SlidingSyncManager.ts(139,13): error TS2345: Argument of type 'Map<any, any>' is not assignable to parameter of type 'MSC3575List[]'.` and `src/SlidingSyncManager.ts(188,37): error TS2339: Property 'getListParams' does not exist on type 'SlidingSync'.` No errors referenced the changed files. Full TypeScript check remains unresolved due to these pre-existing SDK type mismatches.

Constraints: local repository only; no downloads; preserve git history, index, and harness configuration.
