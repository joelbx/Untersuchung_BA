# Checkpoint

Implemented registration-token InteractiveAuth support in `src/components/views/auth/InteractiveAuthEntryComponents.tsx`:

- Stable `m.login.registration_token` and MSC3231 `org.matrix.msc3231.login.registration_token` identifiers route to `RegistrationTokenAuthEntry`.
- The entry renders the labeled, auto-focused `registrationTokenField`, required administrator help text, `AccessibleButton` primary action disabled for empty values, and a spinner while busy.
- Enter and clicking the action use the same guarded submit handler; the submitted object contains only `type` (the advertised `loginType`) and `token`.
- Stage errors render with `role="alert"` and the existing `error` style; mount reports `DEFAULT_PHASE`.

Validation: focused ESLint, Prettier, and `git diff --check` pass. `yarn lint:types` cannot pass due to existing unrelated SlidingSync type errors in `SlidingSyncManager.ts`, `RoomSublist.tsx`, `useSlidingSyncRoomSearch.ts`, `SlidingRoomListStore.ts`, and their tests. No existing InteractiveAuth-focused tests were found.
