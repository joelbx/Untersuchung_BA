Implemented the current-session kebab menu with localized sign-out actions, accessible states, destructive styling, and close-on-click behavior. Bulk sign-out targets only non-current sessions.

The affected tests passed, as did focused ESLint, Stylelint, and `git diff --check`. `yarn lint:types` reports existing Matrix SDK type errors in unrelated files; it reported no errors in the changed files.

Key changes: [KebabContextMenu.tsx](/app/src/components/views/context_menus/KebabContextMenu.tsx), [CurrentDeviceSection.tsx](/app/src/components/views/settings/devices/CurrentDeviceSection.tsx), and [SessionManagerTab.tsx](/app/src/components/views/settings/tabs/user/SessionManagerTab.tsx).