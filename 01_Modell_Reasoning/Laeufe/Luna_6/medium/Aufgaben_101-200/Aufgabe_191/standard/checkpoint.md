# Checkpoint

Implemented registration-token support for both `m.login.registration_token` and `org.matrix.msc3231.login.registration_token`. The dedicated UI has an auto-focused labeled field, help text, disabled empty-state primary action, Enter/click form submission, spinner while busy, and accessible error display. It submits the advertised login type with the entered token, leaving session handling to InteractiveAuth.

Verification:
- `yarn eslint src/components/views/auth/InteractiveAuthEntryComponents.tsx` passed.
- `yarn test --runInBand test/components/views/dialogs/InteractiveAuthDialog-test.tsx` passed (1 test).
- `yarn tsc --noEmit --jsx react` reports existing SlidingSync-related type errors outside the changed file; it reported no errors in the changed file.
- `git diff --check` passed.
