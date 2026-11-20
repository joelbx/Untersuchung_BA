Added [VerifiedBadge](/app/applications/mail/src/app/components/list/VerifiedBadge.tsx) with a “Verified message” tooltip and updated the list to show it when `isFromProton(element)` is true, subject to the existing recipient and DMARC checks.

The reviewer’s checks all passed: 22 helper tests, the mail type check, and `git diff --check`. No remaining failures or test environment problems.