# Checkpoint

Implemented bounded payment event polling in `packages/components/payments/client-extensions/usePollEvents.ts`: 5,000 ms interval, maximum five sequential calls, optional property/action subscription matching, early stop, idempotent in-flight invocation, and timer/subscription cleanup on success or failure. Exported the hook and constants through the client extensions barrel. Wired `PaymentMethods` create-event polling into Chargebee PayPal and new Chargebee card flows.

Verification: `yarn workspace @proton/components check-types` passed; existing `CreditsModal` and `SubscriptionContainer` payment test paths exited successfully (1 test suite passed, 1 skipped; 4 passed, 20 skipped); Prettier check and `git diff --check` passed. No new tests were added.
