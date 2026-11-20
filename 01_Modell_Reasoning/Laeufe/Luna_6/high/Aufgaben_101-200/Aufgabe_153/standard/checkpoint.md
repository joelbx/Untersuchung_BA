# Checkpoint

Task complete: member and invitation data are isolated by shareId, the member view reads and writes only its current share, and `getExistingEmails` combines member, internal invitation, and external invitation emails.

Verification passed:
- `yarn workspace @proton/drive-store check-types`
- `yarn workspace @proton/drive-store test --runInBand store/_shares/useShareActions.test.ts` (5 tests)
- `git diff --check`

No existing test directly covers the Zustand share stores.
