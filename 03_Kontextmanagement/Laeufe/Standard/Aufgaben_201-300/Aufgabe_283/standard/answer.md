Added [isFromProton](/app/applications/mail/src/app/helpers/elements.ts:44). It returns `true` only when a message or conversation has `IsProton === 1`. I also added the property to the relevant types and created the specified [VerifiedBadge](/app/applications/mail/src/app/components/list/VerifiedBadge.tsx).

Verification passed: 24 focused tests, the mail TypeScript check, and `git diff --check`.