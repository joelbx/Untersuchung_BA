# Checkpoint

Issue: repair ACP email validation for expired/missing confirmation data.

Completed:
- Confirmation records now use `confirm:byUid:<uid>` plus `confirm:<code>` objects with millisecond `expires` values.
- Pending checks use the explicit timestamp; resend blocks an active confirmation unless forced. Email lookup falls back to pending data.
- Confirmation by code and ACP force validation handle stale records and accounts with no profile email.
- ACP user rows show all four email states and display a pending email when the profile email is empty.
- Account deletion removes the mapped confirmation pair and resend throttle key.
- Same-address email changes are rejected before profile updates; actual email changes replace prior pending confirmations.

Verification:
- ESLint, JavaScript syntax checks, and `git diff --check` pass.
- Focused ACP tests: 6 passing. Focused profile email tests: 2 passing.
- The full user suite has one legacy assertion expecting resend while an unexpired confirmation is pending; current requirements require that call to fail unless forced.

Constraints: local repository code/tests only; preserve git history, index baseline, and harness configuration.
