# Checkpoint

Task: add bounded event polling after payment method initiation.

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Verification pending.

Verification note: initial combined Jest run failed in two early-completion tests because Jest fake timers hold `queueMicrotask` callbacks; changed deferred unsubscribe to a Promise microtask. Rechecking below.

Final verification:
- `yarn workspace @proton/components test --runInBand --watch=false payments/client-extensions/usePollEvents.test.ts containers/payments/EditCardModal.test.tsx`: exit 0, 2 suites/5 tests passed.
- `yarn workspace @proton/components check-types`: exit 0.
- `yarn prettier --check packages/components/payments/client-extensions/usePollEvents.ts packages/components/payments/client-extensions/usePollEvents.test.ts packages/components/containers/payments/EditCardModal.tsx packages/components/containers/payments/PayPalModal.tsx`: exit 0.
- `yarn workspace @proton/components eslint payments/client-extensions/usePollEvents.ts payments/client-extensions/usePollEvents.test.ts containers/payments/EditCardModal.tsx containers/payments/PayPalModal.tsx --quiet`: exit 0.
- `git diff --check`: exit 0.
