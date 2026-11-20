# Checkpoint

Task complete: bounded event polling after new payment methods are initiated.

Changes:
- `usePollEvents` exports `interval = 5000` and `maxPollingSteps = 5`, calls the event manager at most five times, and optionally watches a property/action pair. It stops early on a matching event and cleans up the timer and subscription on every completion path.
- New Chargebee PayPal and card payment methods request a `PaymentMethods` / `EVENT_ACTIONS.CREATE` watch. Background polling errors are handled by the calling flows.
- Added hook tests for interval/count, irrelevant events, early completion, exhaustion, synchronous subscription events, and events during an active call.

Checks executed successfully:
- `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand packages/components/payments/client-extensions/usePollEvents.test.ts packages/components/containers/payments/PayPalView.test.tsx` (2 suites, 9 tests passed)
- `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand packages/components/containers/payments/EditCardModal.test.tsx` (1 test passed; existing placeholder)
- `./node_modules/.bin/tsc --noEmit --project packages/components/tsconfig.json --pretty false`
- `./node_modules/.bin/prettier --check packages/components/payments/client-extensions/usePollEvents.ts packages/components/payments/client-extensions/usePollEvents.test.ts packages/components/containers/payments/EditCardModal.tsx packages/components/containers/payments/PayPalModal.tsx`
- `git diff --check`
