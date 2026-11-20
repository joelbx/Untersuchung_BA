# Checkpoint

Task: correct cancellation expiry display for subscriptions with a scheduled plan change.

Changes:
- `subscriptionExpires` accepts an optional cancellation context and uses the active term for cancellation or disabled renewal. Free subscriptions and enabled renewal without cancellation retain their existing behavior.
- Cancellation modal, consumer and business confirmation dates, and the cancellation redirection date use the utility.
- Tests cover active versus upcoming term selection and cancellation confirmation dates.

Verification:
- `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand --runTestsByPath packages/components/containers/payments/subscription/helpers/payment.test.ts packages/components/containers/payments/subscription/cancelSubscription/CancelSubscriptionModal.test.tsx packages/components/containers/payments/subscription/cancellationFlow/config/ExpirationTime.test.tsx` — exit 0; 3 suites, 37 tests passed.
- `./node_modules/.bin/tsc -p packages/components/tsconfig.json --noEmit --pretty false` — exit 0.
- Targeted `eslint --quiet` on all changed TypeScript files — exit 0.
- Targeted `prettier --check` on all changed TypeScript files — exit 0.
- `git diff --check` — exit 0.
