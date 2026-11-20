Extracted payment verification into `VerifyPayment` and `getDefaultVerifyPayment`, and added `getCreatePaymentToken` to bind a verifier. Updated the payment and signup callers to create their verifier locally. Chargeable tokens return immediately; pending tokens use the injected verifier; initial failure statuses reject. Verification polling now cleans up its timers and listeners when it settles.

**Verification:** 19 relevant tests passed, both component and account TypeScript checks passed, and targeted ESLint passed. Two `CreditsModal` tests still fail because they expect `PaymentMethodID` in a value produced by the unchanged `toTokenPaymentMethod`, which omits that field.

No delegation was used.