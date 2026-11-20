VERDICT: FIX

The polling cadence is incorrect in [usePollEvents.ts](/app/packages/components/payments/client-extensions/usePollEvents.ts:59). Each new 5000 ms timer starts only after `eventManager.call()` finishes. If a call takes 2 seconds, attempts start at 5, 12, and 19 seconds instead of fixed 5-second intervals. Anchor attempts to the polling schedule while guarding against overlapping calls and duplicate completion.

The focused tests passed, but they use immediately resolved calls and do not cover this delay. Type checking passed. **TEST_ENVIRONMENT_PROBLEM:** none.

- `yarn workspace @proton/components test --runInBand --watch=false payments/client-extensions/usePollEvents.test.ts` — 5 tests passed.
- `yarn workspace @proton/components check-types --pretty false` — passed.

I reviewed the applied patch without changing project code.