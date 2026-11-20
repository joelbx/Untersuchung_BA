Implemented bounded payment event polling with exported `interval = 5000` and `maxPollingSteps = 5`. The hook can watch for a matching property/action, stops early on a match, and cleans up its timer and subscription safely.

New PayPal and card additions now use the polling hook; card edits retain their immediate refresh.

Validation passed: component type check, ESLint, Prettier, and four existing payment test suites (27 tests).

Changed: [usePollEvents.ts](/app/packages/components/payments/client-extensions/usePollEvents.ts), [PayPalModal.tsx](/app/packages/components/containers/payments/PayPalModal.tsx), [EditCardModal.tsx](/app/packages/components/containers/payments/EditCardModal.tsx).