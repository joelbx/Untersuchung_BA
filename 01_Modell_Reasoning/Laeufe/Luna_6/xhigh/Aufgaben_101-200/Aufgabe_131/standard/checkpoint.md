# Checkpoint

- Implemented exported `interval` (5000 ms) and `maxPollingSteps` (5) in the payment event polling hook.
- Added optional property/action subscription matching, early completion, interval cancellation, idempotent unsubscribe, and guards against late events/calls.
- Connected polling to new PayPal and card payment method flows; existing card edits keep the immediate event refresh.
- Validation passed: component TypeScript check; focused existing payment tests (4 suites, 27 tests); ESLint; Prettier; `git diff --check`.
