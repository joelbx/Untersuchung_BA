# Checkpoint

Root cause: `subscriptionExpires` always selects `UpcomingSubscription` when present, and cancellation views independently do the same for their dates. This makes scheduled future term dates leak into cancellation. Current active term is `subscription.PeriodEnd`; upcoming is a separate scheduled term.

Reproduction: `yarn workspace @proton/components test --runInBand --runTestsByPath containers/payments/subscription/helpers/payment.test.ts containers/payments/subscription/cancelSubscription/CancelSubscriptionModal.test.tsx` exited 1. Both new regression tests failed as expected: utility returned null expiry/renew enabled for cancellation, and modal showed June 5 2026 rather than active June 5 2024.

Pattern: existing utility preserves upcoming-term behavior for ordinary subscriptions; free subscriptions have a distinct early return. Implement an optional cancellation boolean and use active term whenever it is true or current renewal is disabled, then route cancellation date displays through the utility.

Implementation: added optional cancellation context to `subscriptionExpires`; it selects current term if that context is true or current `Renew` is disabled, and reports expiry/renewal flags and active plan name accordingly. Cancellation modal, consumer and business confirmation date components, and cancellation redirection use this utility.

Verification: the four-suite relevant Jest run passed (43 tests); the added consumer/business expiration component test passed (2 tests); the focused utility rerun passed (29 tests); `yarn workspace @proton/components check-types --pretty false` exited 0; `git diff --check` exited 0.
