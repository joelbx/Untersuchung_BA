# Checkpoint

Task: Refactor payment token verification into injectable functions while preserving token status semantics and modal polling cleanup.

Plan:
1. Inspect payment token helper, target consumers, local instructions, and existing payment tests.
2. Extract `VerifyPayment`, `getDefaultVerifyPayment`, and `getCreatePaymentToken`; update all five consumers.
3. Run relevant existing tests and review the diff.
