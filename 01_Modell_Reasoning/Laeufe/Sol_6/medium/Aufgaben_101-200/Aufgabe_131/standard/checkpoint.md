# Checkpoint

Implemented bounded payment event polling in `packages/components/payments/client-extensions/usePollEvents.ts`. It exports `interval = 5000` and `maxPollingSteps = 5`, supports an optional property and `EVENT_ACTIONS` filter, and cleans up on a matching event, the final attempt, or a call failure. The PayPal V5 add flow now watches `PaymentMethods` create events.

Verification: five focused Jest tests pass; `yarn workspace @proton/components check-types` passes; Prettier check and `git diff --check` pass.
