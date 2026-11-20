VERDICT: ACCEPT

The patch uses the active term’s end date in cancellation screens through [subscriptionExpires](/app/packages/components/containers/payments/subscription/helpers/payment.ts). I found no correctness or regression issue. No project code was changed during review.

- `yarn workspace @proton/components test --runInBand --runTestsByPath containers/payments/subscription/helpers/payment.test.ts containers/payments/subscription/cancelSubscription/CancelSubscriptionModal.test.tsx containers/payments/subscription/cancellationFlow/config/expirationTime.test.tsx` — 3 suites, 37 tests passed.
- `yarn workspace @proton/components check-types --pretty false` — passed.
- `git diff --check` — passed.

TEST_ENVIRONMENT_PROBLEM: none. No correction is needed.