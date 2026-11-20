# Checkpoint

Task complete: subscription expiry now supports `{ cancellationContext: true }`. Cancellation context and disabled auto-renew force expiry to use the active subscription term and return `subscriptionExpiresSoon: true`, `renewDisabled: true`, `renewEnabled: false`, the active term end timestamp, and its plan title. Free subscriptions keep their prior result; enabled renewal still uses the upcoming term when present.

Cancellation date displays now use this utility in the B2C and B2B cancellation confirmation configurations, the cancellation redirection modal, and the subscription cancellation confirmation modal.

Validation:
- `payment.test.ts`: 31 tests pass.
- cancellationFlow suite: 3 suites / 19 tests pass.
- `CancelSubscriptionModal.test.tsx`: 5 tests pass, including upcoming term date case.
- Targeted ESLint: no errors; two pre-existing test query warnings in `CancelSubscriptionModal.test.tsx`.
- `git diff --check`: clean.
