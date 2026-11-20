Fixed the Drive member view so it reads members, internal invitations, and external invitations for the current `shareId`. Each store now keeps shares separate, and updates to one share leave the others intact. Added `getExistingEmails` and a two-share regression test.

Verification passed: 21 Jest tests, TypeScript type checking, formatting, and `git diff --check`.