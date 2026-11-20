VERDICT: FIX
CODE DEFECTS
- src/components/views/context_menus/KebabContextMenu.tsx:68-74 positions the wrapper at the trigger's right edge, but res/css/structures/_ContextualMenu.pcss:43-45 adds `right: 16px` to the actual menu. The menu appears 16px left of the header edge. Give this menu a class with `right: 0` (or equivalent positioning) and verify right-edge alignment.
- src/components/views/context_menus/KebabContextMenu.tsx:43-50 closes clicked options only through ContextMenu's bubbled click; an option that calls stopPropagation leaves aria-expanded true. Call close from the cloned option handler for pointer and keyboard activation, while preserving the option action, so the reusable options API always closes on activation.
TEST_ENVIRONMENT_PROBLEM
- `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with errors in matrix-js-sdk and unrelated existing app/test files, with no diagnostics in modified files. Resolve the local SDK/type mismatch or existing type errors, then rerun.
TESTS EXECUTED
- `./node_modules/.bin/jest --runInBand --watch=false test/components/views/settings/devices/CurrentDeviceSection-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx`: exit 0; 2 suites, 49 tests, 9 snapshots passed. SessionManagerTab emitted React act/fake timer and fetch warnings.
- `./node_modules/.bin/jest --runInBand --watch=false test/components/views/context_menus/ContextMenu-test.tsx`: exit 0; 1 suite, 8 tests passed.
- `./node_modules/.bin/jest --runInBand --watch=false --silent test/components/views/context_menus/SpaceContextMenu-test.tsx`: exit 0; 1 suite, 14 tests, 1 snapshot passed.
No project code or tests were changed in this review.
