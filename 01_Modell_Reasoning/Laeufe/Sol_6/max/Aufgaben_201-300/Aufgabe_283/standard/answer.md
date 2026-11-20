Added [`isFromProton(element: Element)`](/app/applications/mail/src/app/helpers/elements.ts:43). It returns `true` only when `IsProton` is `1` for a message or conversation. The flag is now typed and preserved in encrypted search results.

The mail list uses that check for its verified badge, rendered by the new [`VerifiedBadge`](/app/applications/mail/src/app/components/list/VerifiedBadge.tsx) with a “Verified message” tooltip.

Validation passed: 19 existing element tests, the mail TypeScript check, Prettier, and `git diff --check`.