VERDICT: ACCEPT
Reviewed subscription expiry utility and all changed cancellation screens. The active term is used in cancellation context or when renewal is disabled; free and renewing behavior remain as specified. No code defects found.
Tests: `yarn workspace @proton/components test --runInBand --runTestsByPath containers/payments/subscription/helpers/payment.test.ts containers/payments/subscription/cancelSubscription/CancelSubscriptionModal.test.tsx containers/payments/subscription/cancellationFlow/config/expirationTime.test.tsx` — 3 suites, 37 tests passed.
Type check: `yarn workspace @proton/components check-types --pretty false` — passed.
Diff check: `git diff --check` — passed.
TEST_ENVIRONMENT_PROBLEM: none.
