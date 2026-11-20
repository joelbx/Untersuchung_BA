# Checkpoint

Investigated payment-method event polling. `rg` is unavailable in this environment, so local searches used `grep`/`find`.

Root cause: `packages/components/payments/client-extensions/usePollEvents.ts` only waits and calls the event manager five times; it never subscribes, so it cannot stop on a matching payment-method event or unsubscribe. The PayPal V5 add flow already invokes this hook. A new focused hook test fails as expected: after the first 5000 ms call, `subscribe` was called 0 times (expected 1). Command: `./node_modules/.bin/jest --config packages/components/jest.config.js --runInBand packages/components/payments/client-extensions/usePollEvents.test.tsx` (exit 1).

Working pattern: the event manager exposes `call()` and `subscribe(listener) -> unsubscribe`; its notifications carry an event response with arrays such as `PaymentMethods` and `Action` fields. Hypothesis: adding a subscription for the requested property/action and a single completion path will allow early stop and cleanup while preserving five delayed calls without a selector.

Implemented the hypothesis in `usePollEvents`: exported `interval` and `maxPollingSteps`, optional `property`/`action` matching, one cleanup path, and no further scheduled calls after completion. Wired card creation and PayPal V4/V5 creation to watch `PaymentMethods`/`EVENT_ACTIONS.CREATE`.

Verification: focused hook test now passes (4 cases: early match and irrelevant events, interval/maximum, exhaustion and late event, event during an in-flight call). Existing `EditCardModal.test.tsx` and `PayPalView.test.tsx` also passed: 3 suites, 8 tests, exit 0. Final `./node_modules/.bin/tsc --noEmit -p packages/components/tsconfig.json --pretty false`, `./node_modules/.bin/prettier --check` on edited source/test files, and `git diff --check` all exited 0.
