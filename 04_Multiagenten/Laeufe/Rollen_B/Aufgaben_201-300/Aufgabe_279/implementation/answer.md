Payment token creation now accepts an injected verification function. The default verifier owns the modal flow, and all payment consumers, including the additional `single-signup/Step1` caller found during type checking, use the bound token creator.

Chargeable tokens return immediately, pending tokens enter verification, and terminal failures reject. Polling now stops and releases its timer and listeners when verification finishes or is canceled; the modal submits a token only after a chargeable result.

Validation passed: 18 helper and modal tests, TypeScript checks for components and account, and `git diff --check`.