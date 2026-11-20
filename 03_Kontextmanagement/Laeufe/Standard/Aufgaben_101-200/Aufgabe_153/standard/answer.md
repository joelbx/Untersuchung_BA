Fixed the Drive member view so members, internal invitations, and external invitations are stored and displayed by share ID. Updates to one share no longer replace another share’s data. Added the `getExistingEmails` utility and regression tests for share isolation.

Verification passed: both Drive type checks, 3 new regression tests, 18 existing share store tests, and `git diff --check`.