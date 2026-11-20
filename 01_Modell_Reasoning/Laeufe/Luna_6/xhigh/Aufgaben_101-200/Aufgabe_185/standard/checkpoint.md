# Checkpoint

Issue: cancellation screens could display the scheduled future plan's expiry instead of the active subscription term's end date.

Changes:
- Added an optional cancellation context to `subscriptionExpires`.
- Free subscriptions retain the existing result. Cancellation context or disabled renewal now reports an expiring subscription using the active term's date and plan title. Enabled renewal without cancellation keeps the existing upcoming-term behavior.
- Routed B2C/B2B confirmation dates, the cancellation modal, and the post-cancellation modal through the expiry utility.
- Updated existing expectations for the active-term date.

Verification:
- Relevant Jest suites: 3 passed, 38 tests passed.
- `@proton/components` type check passed.
- Targeted ESLint passed with two pre-existing testing-library warnings in `CancelSubscriptionModal.test.tsx`.
