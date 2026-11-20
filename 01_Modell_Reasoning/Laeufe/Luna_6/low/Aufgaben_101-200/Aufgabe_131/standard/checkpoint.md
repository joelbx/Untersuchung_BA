# Checkpoint

Implemented bounded polling in `packages/components/payments/client-extensions/usePollEvents.ts`.

- Exposes `interval = 5000` and `maxPollingSteps = 5`.
- Performs at most five calls, waiting one interval before each call.
- Optionally subscribes for a property/action match and unsubscribes on a match or completion.
- Ignores late notifications after completion and makes completion idempotent.
- Preserves existing no-argument call sites.

Verification: the focused Jest invocation found no matching hook test. The component TypeScript check reported one implicit-any issue, which was fixed; rerunning the check completed with exit code 0.
