# Checkpoint

Issue: Add Matrix registration-token support to Element Web InteractiveAuth.

Completed: Added RegistrationTokenAuthEntry with token input, help and accessible error text, busy spinner, primary action, Enter/click submission, and protection against duplicate submits. Registered stable and MSC3231 identifiers while submitting the exact server-advertised stage type. The upper InteractiveAuth success callback remains responsible for session/result handling and its existing extra object.

Validation: Focused existing InteractiveAuthDialog Jest test passed (1 test); ESLint passed for the changed component. `yarn tsc --noEmit --jsx react` reported existing Sliding Sync API/type mismatches in unrelated files and no diagnostics in the changed auth component. `git diff --check` passed.

Constraints: Used checked-out repository code and existing tests only. Git history, index baseline, and harness configuration were not changed.
