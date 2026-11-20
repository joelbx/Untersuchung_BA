Updated the Drive member view and both copies of its stores so members, internal invitations, and external invitations are kept and read by `shareId`. Added `getExistingEmails` and a regression test for isolation between shares.

Both TypeScript checks passed. The existing Drive share store tests passed (18 tests), the new regression tests passed (3 tests), and ESLint reported no errors.