The current-session header has no action trigger. Its only sign-out control is inside expanded device details in [CurrentDeviceSection.tsx](/app/src/components/views/settings/devices/CurrentDeviceSection.tsx).

The likely fix spans these files:

- [CurrentDeviceSection.tsx](/app/src/components/views/settings/devices/CurrentDeviceSection.tsx): add the persistent kebab trigger and localized actions; disable it while loading, without a current device, or during sign-out.
- [SessionManagerTab.tsx](/app/src/components/views/settings/tabs/user/SessionManagerTab.tsx): reuse the existing sign-out flows and pass only `Object.keys(otherDevices)` to the bulk action.
- [ContextMenu.tsx](/app/src/components/structures/ContextMenu.tsx): menu clicks currently stop propagation but do not close the menu. Closing already restores focus to the previously focused trigger.
- New `KebabContextMenu.tsx`: provide the trigger, accessible state, and a menu positioned below the header’s right edge.

[IconizedContextMenu.tsx](/app/src/components/views/context_menus/IconizedContextMenu.tsx) already passes item labels to `MenuItem`, which derives `aria-label` from them; that requirement may need verification rather than a code change. Existing tests cover the underlying sign-out flows, but not the proposed header menu. No project source or tests were changed under the assigned fault-localization scope.