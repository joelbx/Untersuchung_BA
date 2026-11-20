VERDICT: FIX

The applied patch passes the focused tests, but two requirements remain unmet:

- [KebabContextMenu.tsx](/app/src/components/views/context_menus/KebabContextMenu.tsx:68) places the menu at the trigger’s right edge, while the shared [menu CSS](/app/res/css/structures/_ContextualMenu.pcss:43) adds a 16px right inset. Override that inset for this menu so its right edge aligns with the header.
- [KebabContextMenu.tsx](/app/src/components/views/context_menus/KebabContextMenu.tsx:43) relies on click bubbling to close a clicked option. A supplied option that stops propagation leaves the menu open and `aria-expanded` true. Close from the option’s activation handler for clicks as well as keyboard activation.

**Tests run**

- `./node_modules/.bin/jest --runInBand --watch=false test/components/views/settings/devices/CurrentDeviceSection-test.tsx test/components/views/settings/tabs/user/SessionManagerTab-test.tsx` — passed: 49 tests, 9 snapshots.
- `./node_modules/.bin/jest --runInBand --watch=false test/components/views/context_menus/ContextMenu-test.tsx` — passed: 8 tests.
- `./node_modules/.bin/jest --runInBand --watch=false --silent test/components/views/context_menus/SpaceContextMenu-test.tsx` — passed: 14 tests, 1 snapshot.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/tsc --noEmit --jsx react` exited 2 with errors in `matrix-js-sdk` and unrelated app and test files; it reported none in the modified files. Resolve the local SDK/type errors and rerun the check.

This was a review only; I made no project code or test changes.