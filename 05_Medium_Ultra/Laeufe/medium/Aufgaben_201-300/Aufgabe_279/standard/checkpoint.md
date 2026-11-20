# Payment token verification refactor

Status: complete.

Changes: added injectable VerifyPayment, getDefaultVerifyPayment, and getCreatePaymentToken; migrated all six token creation callers; made process use cancellable timers and clean up listeners; guarded modal and PayPal flows against submitting nonchargeable tokens after polling resolves.

Validation: components and account TypeScript checks passed. Helper, verification modal, and edit card tests passed (25 tests). The broader CreditsModal suite had two unrelated existing expectations for PaymentMethodID in the final token payload; toTokenPaymentMethod does not include that field. Prettier and git diff --check passed.
