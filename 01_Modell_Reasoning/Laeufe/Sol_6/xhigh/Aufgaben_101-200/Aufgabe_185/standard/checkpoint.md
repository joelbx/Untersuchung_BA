# Subscription cancellation expiry fix

Status: implemented and verified.

- `subscriptionExpires` accepts an optional cancellation context. Cancellation or disabled renewal selects the active term's end timestamp and title with expiring/renewal flags; free and normal renewal behavior are retained.
- Cancellation confirmation, consumer and business reminder dates, post-cancellation redirection and reminder, and the expiring dashboard date use the utility.
- Focused Jest suites passed: 63 tests across 5 suites.
- `yarn workspace @proton/components check-types --noEmit --pretty false` passed.
- `git diff --check` passed.
