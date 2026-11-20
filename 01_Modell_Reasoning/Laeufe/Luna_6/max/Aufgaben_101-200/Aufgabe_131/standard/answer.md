Implemented bounded payment event polling. The hook exports `interval = 5000` and `maxPollingSteps = 5`, polls sequentially, can stop on a matching property/action event, and cleans up timers and subscriptions safely. Chargebee PayPal and new Chargebee card flows now watch for `PaymentMethods` create events.

Updated [usePollEvents.ts](/app/packages/components/payments/client-extensions/usePollEvents.ts), its barrel export, [PayPalModal.tsx](/app/packages/components/containers/payments/PayPalModal.tsx), and [EditCardModal.tsx](/app/packages/components/containers/payments/EditCardModal.tsx).

Verification passed: components type-check, Prettier, and `git diff --check`. The targeted Jest run exited successfully: one suite passed and one was skipped; 4 tests passed and 20 were skipped.