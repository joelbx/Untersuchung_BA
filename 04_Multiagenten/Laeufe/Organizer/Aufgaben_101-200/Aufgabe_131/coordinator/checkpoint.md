# Checkpoint

Issue resolved: bounded event polling after payment method creation.
Implemented: exported 5000 ms interval and 5 attempt limit in usePollEvents; optional event subscription for a property/action; early stop, timeout stop, late callback guard, and unsubscribe. Card creation and both PayPal creation flows request PaymentMethods CREATE polling. Card editing retains immediate refresh.
Verification: usePollEvents.test.ts (4 tests) and existing EditCardModal.test.tsx (1 test) passed; @proton/components check-types passed; git diff --check passed.
Delegation: none; solved locally.
