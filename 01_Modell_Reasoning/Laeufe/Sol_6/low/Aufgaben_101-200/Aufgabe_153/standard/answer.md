Updated both Drive store copies so members, internal invitations, and external invitations are stored by `shareId`. The member views now read and update the current share’s data, and `getExistingEmails` combines addresses from the three lists. Added share isolation tests.

Verification passed: both Drive type checks, 2 new isolation tests, 18 existing share store tests, and `git diff --check`.